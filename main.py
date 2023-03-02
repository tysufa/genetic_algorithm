import pygame

pygame.init()

w_size = (720, 480)

window = pygame.display.set_mode(w_size)

continuer = True
gravity = False

clock = pygame.time.Clock()

player_rect = pygame.Rect(w_size[0]/2, w_size[1]/2 - 40, 20, 40)

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    window.fill("black")

    pygame.draw.rect(window, "red", player_rect)

    pygame.display.flip()
    clock.tick(60)
