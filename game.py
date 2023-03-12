import pygame
import player
import car
from random import choice, randint

def play(voiture = ""):
    pygame.init()

    #set size ecrant
    screen_info = pygame.display.Info()
    l = 800
    h = screen_info.current_h - 100

    #importation des images et redimension si besoin
    road = pygame.image.load("assets/road.png")
    road = pygame.transform.scale(road, (l, h))

    #set fps
    fps = 60

    #crea de la fenetre
    screen = pygame.display.set_mode((l, h))
    pygame.display.set_caption("Furry Road")
    pygame.display.set_icon(pygame.image.load('assets/road_icon.png'))

    #importation des music et lancement du son
    pygame.mixer_music.load("assets/play_music.mp3")
    pygame.mixer_music.play(-1)

    #set vitesse mouvance fond
    bg_pos_y = 0
    bg_speed = 20

    #instances
    p = player.Player(700, h, voiture)

    #sprite grp
    player_grp = pygame.sprite.Group(p)
    car_grp = pygame.sprite.Group()

    #crea d'une liste avec les collisions
    car_rect = list()

    #crea font
    font = pygame.font.Font(None, 20)

    #fonction
    def spawn_car():
        x_lst = list()
        for _ in range(randint(2, 3)):
            x = choice([100, 300, 500, 700])
            while x in x_lst:
                x = choice([100, 300, 500, 700])
            x_lst.append(x)
            #instance dune voiture
            c = car.Car(x, randint(-256, 0), randint(20, 25))
            #ajout de la voiture au grp
            car_grp.add(c)
            
    #set custom event
    SPAWN = pygame.USEREVENT + 1

    #set timer pour spawn
    pygame.time.set_timer(SPAWN, 2000)

    #boucle principale
    clock = pygame.time.Clock()
    while True:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    p.right()
                elif event.key == pygame.K_LEFT:
                    p.left()

            if event.type == SPAWN:
                spawn_car()

        #deplacement bg
        bg_pos_y += bg_speed
        if bg_pos_y > h:
            bg_pos_y = 0
        
        #update
        car_grp.update(h)
        player_grp.update(car_grp.sprites())

        #text
        s = round(p.get_score())
        score = font.render("Score: " + str(s), True, (255, 255, 255))
    
        #Affichage
        screen.blit(road, (0, bg_pos_y))
        screen.blit(road, (0, bg_pos_y - h))
        screen.blit(score, (40, 10))
        player_grp.draw(screen)
        car_grp.draw(screen)
        pygame.display.update()

        clock.tick(fps)