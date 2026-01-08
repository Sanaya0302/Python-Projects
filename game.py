import pygame
import random
screen_width,screen_height=500,400
speed=5
font_size=72
pygame.init()
bg_image=pygame.transform.scale(pygame.image.load("bg.jpeg"),(screen_width,screen_height))
font=pygame.font.SysFont("Times New Roman",font_size)
class Player(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(pygame.Color("black"))
        pygame.draw.rect(self.image,color,(0,0,width,height))
        self.rect=self.image.get_rect()
    def move(self,x,y):
        self.rect.x=max(min(0,self.rect.x+x*speed),screen_width - self.rect.width)
        self.rect.y=max(min(0,self.rect.y+y*speed),screen_height - self.rect.height)