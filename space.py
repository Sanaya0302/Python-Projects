import math
import random
import pygame
screen_width = 800
screen_height = 600
player_start_x=370
player_start_y=380
enemy_start_y_min=50
enemy_start_y_max=150
enemy_speed_x=4
enemy_speed_y=40
bullet_speed_y=10
collision_distance=27
pygame.init()
screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)
bg_image = pygame.transform.scale(pygame.image.load("space.jpeg"), (screen_width, screen_height))
player_x=player_start_x
player_y=player_start_y
player_img=pygame.image.load("ship.png")
player_x_change=0
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, screen_width - 64))
    enemyY.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemyX_change.append(enemy_speed_x)
    enemyY_change.append(enemy_speed_y)
bullet =pygame.image.load("bullet.png")
bulletX=0
bulletY=player_start_y
bulletX_change=0
bulletY_change=bullet_speed_y
bullet_state="ready"
score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
textX=10
textY=10
over_font=pygame.font.Font("freesansbold.ttf",64)
def show_score(x,y):
    score=font.render("Score : "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))
def player(x,y):
    screen.blit(player_img,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet,(x+16,y+10))
def is_collision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    return distance<collision_distance
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(bg_image,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_x_change=-5
            if event.key==pygame.K_RIGHT:
                player_x_change=5
            if event.key==pygame.K_SPACE:
                if bullet_state=="ready":
                    bulletX=player_x
                    fire_bullet(bulletX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                player_x_change=0
    player_x+=player_x_change
    if player_x<=0:
        player_x=0
    elif player_x>=screen_width-64:
        player_x=screen_width-64
    for i in range(num_of_enemies):
        if enemyY[i]>440:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over_text()
            break
        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i]=enemy_speed_x
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=screen_width-64:
            enemyX_change[i]=-enemy_speed_x
            enemyY[i]+=enemyY_change[i]
        collision=is_collision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY=player_start_y
            bullet_state="ready"
            score_value+=1
            enemyX[i]=random.randint(0, screen_width - 64)
            enemyY[i]=random.randint(enemy_start_y_min, enemy_start_y_max)
        enemy(enemyX[i],enemyY[i],i)
    if bulletY<=0:
        bulletY=player_start_y
        bullet_state="ready"
    if bullet_state=="fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
    player(player_x,player_y)
    show_score(textX,textY)
    pygame.display.update()