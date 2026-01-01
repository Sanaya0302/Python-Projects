import pygame
def main():
    pygame.init()
    width,height=500,500
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption("Color changing sprite!!!!!!")
    colours={
        'red':pygame.Color('red')
        ,'yellow':pygame.Color('yellow')
        ,'green':pygame.Color('green')
        ,'blue':pygame.Color('blue')
        ,'white':pygame.Color('white')}
    current=colours['white']
    x,y= 30,30
    w,h= 60,60
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x-=3
        if pressed[pygame.K_RIGHT]: x+=3
        if pressed[pygame.K_UP]: y-=3
        if pressed[pygame.K_DOWN]: y+=3
        x=min(max(0,x),width-w)
        y=min(max(0,y),height-h)
        if x==0:
            current=colours['blue']
        elif x==width-w:
            current=colours['red']
        elif y==0:
            current=colours['yellow']
        elif y==height-h:
            current=colours['green']
        else:
            current=colours['white']    
        screen.fill((0,0,0))
        pygame.draw.rect(screen,current,(x,y,w,h))
        pygame.display.flip()
        clock.tick(90)
    pygame.QUIT()
if __name__=='__main__':
    main()
