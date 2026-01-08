import pygame
pygame.init()
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        self.image=pygame.Surface((40,40))
        self.image.fill(color)
        self.rect=self.image.get_rect(topleft=(x,y))
    def update(self):
        k=pygame.key.get_pressed()
        if k[pygame.K_LEFT]:
            self.rect.x-=5
        if k[pygame.K_RIGHT]:
            self.rect.x+=5 
        if k[pygame.K_UP]:
            self.rect.x-=5 
        if k[pygame.K_DOWN]:
            self.rect.x+=5
screen=pygame.display.set_mode((500,400))
clock=pygame.time.Clock()
Sp1=Sprite(pygame.Color("cyan"),100,100) 
Sp2=Sprite(pygame.Color("red"),300,200)          
sprites=pygame.sprite.Group(Sp1,Sp2)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit
            quit()
    Sp1.update()
    screen.fill(pygame.Color("black"))
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)