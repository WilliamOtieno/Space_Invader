import pygame
import random
import math


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
enemyImg = []
enemyImg= []
enemyX= []
enemyY= []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

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

score = 0

def player(x , y):
    screen.blit(playerImg, (x, y))

def enemy(x , y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


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
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        #Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i]= random.randint(0, 800)
            enemyY[i]= random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    #Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change 
    
    

    player(playerX, playerY)
    
    pygame.display.update()

