import random
import pygame
import Constant as c

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("space/PNG/Default/enemy_B.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.snd_hit = pygame.mixer.Sound('Audio/footstep_carpet_004.ogg')
        self.speed_x = random.uniform(-1, 1)  # Set a speed in x-direction
        self.hp = 3
        self.rect_y = random.uniform(4, 10)  # Use uniform for a float value
        self.is_invincible = False
        self.is_destroyed = False
        self.last_speed_increase_time = pygame.time.get_ticks()

    def update(self):
        # Move horizontally within the screen boundaries
        self.rect.x += self.speed_x

        # Check if the enemy is going out of bounds on the right
        if self.rect.right > c.DISPLAY_WIDTH:
            self.rect.right = c.DISPLAY_WIDTH  # Set to the right boundary

        # Check if the enemy is going out of bounds on the left
        elif self.rect.left < 0:
            self.rect.left = 0  # Set to the left boundary

        self.rect.y += self.rect_y  # Move vertically

        # Check if 10 seconds have passed since the last speed increase
        current_time = pygame.time.get_ticks()
        if current_time - self.last_speed_increase_time >= 10000:  # 10000 milliseconds = 10 seconds
            self.speed_x = 5  # Increase speed randomly
            self.last_speed_increase_time = current_time  # Update the last speed increase time

    def get_hit(self):
        self.snd_hit.play()
        if not self.is_invincible:
            self.hp -= 1
            if self.hp <= 0:
                self.is_invincible = True
                self.is_destroyed = True
                self.kill()
            else:
                pass
