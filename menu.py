import pygame
import pygame_gui
import game
import car
import choice_car
from random import randint, choice

def menu(score = 0):
    # Initialisation de Pygame
    pygame.init()

    # set taille fen
    screen_info = pygame.display.Info()
    h = screen_info.current_h - 100
    l = 800

    #importation des images et redimension si besoin
    road = pygame.image.load("assets/road.png")
    road = pygame.transform.scale(road, (l, h))
    icon = pygame.image.load('assets/road_icon.png')

    #importation des music et lancement du son
    pygame.mixer_music.load("assets/menu_music.mp3")
    pygame.mixer_music.play(-1)

    #crea de la fen
    screen = pygame.display.set_mode((l, h))
    pygame.display.set_caption("Furry Road")
    pygame.display.set_icon(icon)

     #vitesse bg
    bg_speed = 1
    bg_pos_y = 0

    # Configuration du gestionnaire d'interface graphiquemanager = pygame_gui.UIManager((l, h))
    manager = pygame_gui.UIManager((l, h))

    # Création des boutons
    button_play = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((l//2 - 100, h//2 - 50), (200, 50)),
        text='Jouer',
        manager=manager
    )

    button_car = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((l//2 - 100, h//2), (200, 50)),
        text='Choisir la voiture',
        manager=manager
    )

    button_quit = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((l//2 - 100, h//2 + 50), (200, 50)),
        text='Quitter',
        manager=manager
    )

    #crea font
    font = pygame.font.Font(None, 50)

    #gestion best_score
    with open("assets/score.txt", "r") as f:
        best_score = int(f.read())
    
    if score > best_score:
        with open('assets/score.txt', 'w') as f:
            best_score = score
            f.write(str(score))
            f.close()

    #grp de sprite
    cars = pygame.sprite.Group()

    def spawn_car():
        #instance dune voiture
        c = car.Car(choice([100, 300, 500, 700]) ,0 , 2)
        #ajout de la voiture au grp
        cars.add(c)

    SPAWN = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN, 8000)

    # Boucle de jeu
    running = True
    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == SPAWN:
                spawn_car()

            # Gestion des événements d'interface graphique
            manager.process_events(event)

            # Gestion des événements des boutons
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_play:
                        pygame.quit()
                        game.play()
                    elif event.ui_element == button_quit:
                        running = False
                    elif event.ui_element == button_car:
                        pygame.quit()
                        choice_car.set_car()

        #deplacement bg
        bg_pos_y += bg_speed
        if bg_pos_y > h:
            bg_pos_y = 0

        #update
        cars.update(h)

        #text
        s = font.render("Score: " + str(score), True, (0, 0, 0))
        bs = font.render("Meilleur score: " + str(best_score), True, (0, 0, 0))

        # Mise à jour de l'affichage
        manager.update(pygame.time.get_ticks() / 1000.0)
        screen.blit(road, (0, bg_pos_y))
        screen.blit(road, (0, bg_pos_y - h))
        cars.draw(screen)
        screen.blit(bs, (270, h // 4 - 50))
        screen.blit(s, (340, h // 4))
        manager.draw_ui(screen)
        pygame.display.update()

    # Fermeture de Pygame
    pygame.quit()