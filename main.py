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

#Bullet
#Ready means you cant see the bullet on the screen
#Fire means the bullet is currently moving 
bulletImg= pygame.image.load('bullet.png')
bulletX= 0
bulletY= 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready" 

#Player
playerImg = pygame.image.load('spaceship2.png')
playerX = 370
playerY = 520
playerX_change = 0

def player(x , y):
    screen.blit(playerImg, (x, y))

def enemy(x , y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

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
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX 
                fire_bullet(bulletX, bulletY)

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

    #Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change 

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

