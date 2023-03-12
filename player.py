import pygame
from pygame.locals import *
from random import choice
import menu

all_car = ["Audi.png", "Black_viper.png", "Car.png", "Mini_truck.png", "Mini_van.png", "taxi.png"]

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, name_car = ""):
        pygame.init()

        #chargment image
        if name_car != "":
            sprite = pygame.image.load(name_car)
        else:
            sprite = pygame.image.load("assets/cars/" + choice(all_car))
        
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y - 20
        self.score = 0

    def right(self):
        if self.rect.centerx < 700:
                self.rect.centerx += 200

    def left(self):
        if self.rect.centerx > 200:
                self.rect.centerx -= 200
    
    def get_rect(self):
        return self.rect
    
    def get_image(self):
        return self.image

    def update(self, liste):
        self.score += 1 / 60
        for sprite in liste:
            if self.rect.colliderect(sprite.get_rect()):
                pygame.quit()
                menu.menu(round(self.score))

    def get_score(self):
        return self.score