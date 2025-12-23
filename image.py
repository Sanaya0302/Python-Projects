import pygame
pygame.init()
width,height=500,500
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("My first game window")
bg=pygame.transform.scale(pygame.image.load("images.jpg").convert(),(width,height))
girl=pygame.transform.scale(pygame.image.load("girl1.png").convert_alpha(),(200,200))
rect=girl.get_rect(center=(width//2,height//2-30))
text=pygame.font.Font(None,36).render("Hello World",True,pygame.Color("black"))
trect=text.get_rect(center=(width//2,height//2+110))
def gamel():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        screen.blit(bg,(0,0))
        screen.blit(girl,rect)
        screen.blit(text,trect)
        pygame.display.flip()
        clock.tick(30)
    pygame.QUIT()
if __name__=='__main__':
    gamel()