import pygame
from Ship import Ship
from Constant import DISPLAY_SIZE, DISPLAY_WIDTH, DISPLAY_HEIGHT
from background import BG
from bullet import Bullet
from enemy_spawner import EnemySpawner
from particle_spawner import ParticleSpawner
import os

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
pygame.font.init()

# Font Setup
font = pygame.font.Font(None, 36)


# Load the best score from the file
def load_best_score():
    if os.path.exists("best_score.txt"):
        try:
            with open("best_score.txt", "r") as file:
                return int(file.read())
        except ValueError:
            print("Invalid best score format in the file.")
    return 0


# Save the best score to the file
def save_best_score(best_score):
    with open("best_score.txt", "w") as file:
        file.write(str(best_score))


# Display Setup
display = pygame.display.set_mode(DISPLAY_SIZE)
fps = 60
clock = pygame.time.Clock()
black = (0, 0, 0)

# Object Setup
bg = BG()
bg_group = pygame.sprite.Group(bg)
player = Ship()
sprite_group = pygame.sprite.Group(player)
enemy_spawner = EnemySpawner()
particle_spawner = ParticleSpawner()

# Music Setup
pygame.mixer.music.load('Audio/F-Zero-Big-Blue-_Remix_.ogg')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(1)

# Initialize player score, best score, and remaining lives
player_score = 0
best_score = load_best_score()
remaining_lives = player.hp  # Assuming player.hp represents the initial number of lives

running = True
game_over = False

while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.target_vel_x = -player.speed
            elif event.key == pygame.K_d:
                player.target_vel_x = player.speed


            if event.key == pygame.K_SPACE:
                player.shoot()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.target_vel_x = 0

    # Smoothing the controls
    player.vel_x += (player.target_vel_x - player.vel_x) * 0.1

    bg_group.update()
    sprite_group.update()
    enemy_spawner.update()
    particle_spawner.update()

    # Check Collision
    collided = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, False)
    for bullet, enemy in collided.items():
        enemy[0].get_hit()
        player_score += 10
        particle_spawner.spawn_particles((enemy[0].rect.x, enemy[0].rect.y))  # Spawn particles when enemy is hit

    collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.enemy_group, False, False)
    for player, enemy in collided.items():
        if not enemy[0].is_invincible:
            player.get_hit()
            remaining_lives = player.hp  # Update remaining lives when the player is hit
        enemy[0].hp = 0
        enemy[0].get_hit()
        particle_spawner.spawn_particles((player.rect.x, player.rect.y))  # Spawn particles when player is hit

    best_score = max(player_score, best_score)

    display.fill(black)
    bg_group.draw(display)
    sprite_group.draw(display)
    player.bullets.draw(display)
    enemy_spawner.enemy_group.draw(display)
    particle_spawner.particle_group.draw(display)

    # Render and display the score, best score, and remaining lives
    score_text = font.render("Score: {}".format(player_score), True, (255, 255, 255))
    best_score_text = font.render("Best Score: {}".format(best_score), True, (255, 255, 255))
    lives_text = font.render("Lives: {}".format(remaining_lives), True, (255, 255, 255))

    display.blit(score_text, (10, 10))
    display.blit(best_score_text, (DISPLAY_WIDTH - best_score_text.get_width() - 10, 10))
    display.blit(lives_text, (10, DISPLAY_HEIGHT - lives_text.get_height() - 10))

    if not player.is_alive and not game_over:
        game_over = True
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2))
        display.blit(game_over_text, text_rect)
        pygame.display.update()
        pygame.time.delay(3000)
        running = False

    pygame.display.update()

    save_best_score(best_score)

pygame.quit()
quit()
