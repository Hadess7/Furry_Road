import pygame
from random import choice



#set sprite
all_car = ['assets/cars/truck.png',"assets/cars/Audi.png", "assets/cars/Black_viper.png", "assets/cars/Car.png", "assets/cars/Mini_truck.png", "assets/cars/Mini_van.png", "assets/cars/taxi.png", "assets/cars/Ambulance.png", "assets/cars/Police.png"]

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        pygame.init()
        super().__init__()
        self.image = pygame.transform.rotate(pygame.image.load(choice(all_car)), 180) 
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = speed

    
    def update(self, h):
        self.rect.centery += self.speed
        if self.rect.top > h:
            self.kill()

    def get_rect(self):
        return self.rect