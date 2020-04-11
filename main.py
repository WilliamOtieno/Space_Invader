import pygame

#Initialize the pygame 
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #RGB color red    
    screen.fill((0, 0, 0))
    pygame.display.update()

