import pygame
import game

def set_car():

    #crea generique d'une fenetre
    pygame.init()
    h = pygame.display.Info().current_h - 100
    l = 800
    bg = pygame.transform.scale(pygame.image.load('assets/road.png'), (l, h))
    pygame.display.set_caption("Furry Road - choix de la voiture")
    pygame.display.set_icon(pygame.image.load("assets/road_icon.ico"))
    pygame.mixer_music.load("assets/menu_music.mp3")
    pygame.mixer_music.play(-1)
    screen = pygame.display.set_mode((l, h))
    bg_pos_y = 0
    bg_speed = 1

    #crea d'une classe bouton
    class Bouton(pygame.sprite.Sprite):
        def __init__(self, x, y, image, action):
            super().__init__()
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.action = action
        
        def update(self):
            souris = pygame.mouse.get_pos()
            clic = pygame.mouse.get_pressed()[0]
            if self.rect.collidepoint(souris):
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
                if clic:
                    pygame.quit()
                    game.play(self.action)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)

    #groupe
    boutons = pygame.sprite.Group()

    #tests
    y1 = h // 2 - h // 4
    y2 = h // 2 + h // 4
    x1 = l // 4
    x2 = l // 2
    x3 = l // 2 + l // 4
    lst_butons = [
        Bouton(x1, y1, pygame.image.load("assets/cars/Audi.png"), "assets/cars/Audi.png"),
        Bouton(x2, y1, pygame.image.load("assets/cars/Black_viper.png"), "assets/cars/Black_viper.png"),
        Bouton(x3, y1, pygame.image.load("assets/cars/Car.png"), "assets/cars/Car.png"),
        Bouton(x1, y2, pygame.image.load("assets/cars/Mini_truck.png"), "assets/cars/Mini_truck.png"),
        Bouton(x2, y2, pygame.image.load("assets/cars/Mini_van.png"), "assets/cars/Mini_van.png"),
        Bouton(x3, y2, pygame.image.load("assets/cars/taxi.png"), "assets/cars/taxi.png")
        ]


    for bt in lst_butons:
        boutons.add(bt)

    #boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        bg_pos_y += bg_speed
        if bg_pos_y > h:
            bg_pos_y = 0

        #update
        boutons.update()

        #Affichage
        screen.blit(bg, (0, bg_pos_y))
        screen.blit(bg, (0, bg_pos_y - h))
        boutons.draw(screen)
        pygame.mouse.get_pos()
        pygame.display.update()