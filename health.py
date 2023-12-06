import pygame
import Constant as c


class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        super(HealthBar,self).__init__()
        self.image = pygame.image.load('space/PNG/Default/icon_crossSmall.png').convert()
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y