import pygame
import random


#Initialize the pygame 
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800, 600))

#Background
background = pygame.image.load("background.png")

#Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)


#Enemy
enemyImg= pygame.image.load('alien.png')
enemyX= random.randint(0, 800)
enemyY= random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40


#Player
playerImg = pygame.image.load('spaceship2.png')
playerX = 370
playerY = 520
playerX_change = 0

def player(x , y):
    screen.blit(playerImg, (x, y))

def enemy(x , y):
    screen.blit(enemyImg, (x, y))

#Game loop
running = True
while running:

    #RGB color red    
    screen.fill((0, 0, 0))

    #Background image
    screen.blit(background, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #if keystroke is pressed check whethere it is LEFT or RIGHT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    playerX += playerX_change
    
    #Boundary restrictions for player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change
    
    #Boundary restrictions/movement for enemy
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change 

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

