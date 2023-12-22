import pygame
from settings import x, y

#Das spiel intialisieren
pygame.init()

#Titel und Fenster Größe
screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("Modify the Code of this Game")

player = pygame.Rect((400, 300, 50, 50))
playertwo = pygame.Rect((400, 300, 50, 50))

#Die spiel Schleife
run = True
while run:

    screen.fill((0, 0, 0,))

    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (122, 3, 50), playertwo)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)

    elif key[pygame.K_LEFT] == True:
        playertwo.move_ip(-1, 0)
    elif key[pygame.K_RIGHT] == True:
        playertwo.move_ip(1, 0)
    elif key[pygame.K_UP] == True:
        playertwo.move_ip(0, -1)
    elif key[pygame.K_DOWN] == True:
        playertwo.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()