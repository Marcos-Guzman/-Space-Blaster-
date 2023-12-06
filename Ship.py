import pygame
import Constant as c
from bullet import Bullet
from hud import HUD

scale = 1

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.image = pygame.image.load('space/PNG/Default/ship_sidesA.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() / scale), int(self.image.get_height() / scale)))
        self.rect = self.image.get_rect()
        self.rect.x = (c.DISPLAY_WIDTH - self.rect.width) // 2  # Center the ship horizontally
        self.rect.y = (c.DISPLAY_HEIGHT - self.rect.height)  # Center the ship vertically
        self.bullets = pygame.sprite.Group()
        self.snd_shoot = pygame.mixer.Sound('Audio/footstep_carpet_001.ogg')
        self.HUD = HUD()
        self.hud_group = pygame.sprite.Group()
        self.hud_group.add(self.HUD)
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.hp = 3
        self.is_alive = True
        self.target_vel_x = 0  # New attribute for target velocity in x-axis
        self.target_vel_y = 0  # New attribute for target velocity in y-axis

    def update(self):
        self.bullets.update()
        self.hud_group.update()
        for bullet in self.bullets:
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)

        # Update the ship's position based on velocity
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Ensure the ship stays within the screen boundaries
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > c.DISPLAY_WIDTH - self.rect.width:
            self.rect.x = c.DISPLAY_WIDTH - self.rect.width

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > c.DISPLAY_HEIGHT - self.rect.height:
            self.rect.y = c.DISPLAY_HEIGHT - self.rect.height

    def shoot(self):
        self.snd_shoot.play()
        new_bullet = Bullet()
        new_bullet.rect.x = self.rect.x + (self.rect.width // 2) - 1
        new_bullet.rect.y = self.rect.y
        self.bullets.add(new_bullet)

    def get_hit(self):
        self.hp -= 1
        if self.hp == 0:
            self.is_alive = False
            self.kill()
        print(self.hp)
