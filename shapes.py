import pygame
def main():
    pygame.init()
    width,height=500,500
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption("My first game screen!")
    color={
        'yellow':pygame.Color('yellow')}
    current=color['yellow']
    screen.fill((0,0,0))
    rect=250,250
    pygame.draw.rect(screen,current(rect,30,30))
main()
