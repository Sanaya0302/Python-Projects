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
        if boundary_hit:
            pygame.event.post(pygame.event.Event(s_colorchange))
            pygame.event.post(pygame.event.Event(bg_colorchange))
    def color_change(self):
        self.image.fill(random.choice([pink,lavender,yellow,white]))        
    def bg_change(self):
        global bg_colorchanging
        bg_colorchanging=random.choice([cyan,lightblue,darkblue])        
all_sprite=pygame.sprite.Group()
Sprite1=Sprite(white,20,30)
Sprite1.rect.x=random.randint(0,480)
Sprite1.rect.y=random.randint(0,370)
all_sprite.add(Sprite1)
clock=pygame.time.Clock()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==s_colorchange:
            Sprite1.color_change()
        elif event.type==bg_colorchange:
            Sprite1.bg_change()
    all_sprite.update()
    Screen.fill(bg_colorchanging)

