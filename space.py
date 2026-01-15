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
    