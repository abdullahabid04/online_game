import pygame

from network import Network
from Requirements import WIDTH, HEIGHT


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("G A M E")
icon = pygame.image.load('images/bg.png')
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', 32)


def draw_win(win, play1, play2):
    win.fill((255, 255, 255))
    play1.draw(win)
    play2.draw(win)
    pygame.display.update()


def start():
    run = True
    clock = pygame.time.Clock()
    net = Network()
    p1 = net.get_p()

    while run:
        clock.tick(60)
        p2 = net.send(p1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        p1.move()
        draw_win(window, p1, p2)


if __name__ == '__main__':
    start()
