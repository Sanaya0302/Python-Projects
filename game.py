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
    def move(self,x_change,y_change):
        self.rect.x=max(0,min(self.rect.x+x_change,screen_width - self.rect.width))
        self.rect.y=max(0,min(self.rect.y+y_change,screen_height - self.rect.height))
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Move the rectangle using arrow keys")
group=pygame.sprite.Group()
sprite1=Player(pygame.Color("black"),20,30)
sprite1.rect.x,sprite1.rect.y=random.randint(0,screen_width-sprite1.rect.width),random.randint(0,screen_height-sprite1.rect.height)
group.add(sprite1)
sprite2=Player(pygame.Color("red"),20,30)
sprite2.rect.x,sprite2.rect.y=random.randint(0,screen_width-sprite2.rect.width),random.randint(0,screen_height-sprite2.rect.height)
group.add(sprite2)
running,won=True,False
clock=pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if not won:
        keys=pygame.key.get_pressed()
        x_change=(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*speed    
        y_change=(keys[pygame.K_DOWN]-keys[pygame.K_UP])*speed
        sprite1.move(x_change,y_change)
        if pygame.sprite.collide_rect(sprite1,sprite2):
            won=True
    screen.blit(bg_image,(0,0))
    group.draw(screen)
    if won:
        text=font.render("You Win!",True,pygame.Color("black"))
        screen.blit(text,((screen_width - text.get_width())//2,(screen_height - text.get_height())//2))
    pygame.display.flip()
    clock.tick(90)
pygame.quit()