import pygame
import random
pygame.init()
s_colorchange=pygame.USEREVENT+1
bg_colorchange=pygame.USEREVENT+2
cyan=pygame.Color("cyan")
lightblue=pygame.Color("lightblue")
darkblue=pygame.Color("darkblue")

pink=pygame.Color("pink")
lavender=pygame.Color("lavender")
yellow=pygame.Color("yellow")
white=pygame.Color("white")
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit=False
        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[0]=-self.velocity[0]
            boundary_hit=True
        if self.rect.top<=0 or self.rect.bottom>=400:
            self.velocity[1]=-self.velocity[1]
            boundary_hit=True