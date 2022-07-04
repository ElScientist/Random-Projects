import pygame

pygame.init();
screen = pygame.display.set_mode([600, 600]);

keep_going = True;
RED = (255, 0, 0);
BLUE = (0, 0, 255);
GREEN = (0, 255, 0);
YELLOW = (255, 200, 0);
PINK = (255, 0, 100);
PURPLE = (150, 0, 150);
ORANGE = (255, 100, 0);
radius = 50

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False;
    for x in range (600):
        pygame.draw.circle(screen, RED, (x, x), 10);
        pygame.draw.circle(screen, GREEN, (x+100, x), 10);
        pygame.draw.circle(screen, BLUE, (x-100, x), 10);
        pygame.draw.circle(screen, YELLOW, (x+200, x), 10);
        pygame.draw.circle(screen, ORANGE, (x+300, x), 10);
        pygame.draw.circle(screen, PINK, (x-200, x), 10);
        pygame.draw.circle(screen, PURPLE, (x-300, x), 10);
        pygame.display.update();

pygame.quit();
