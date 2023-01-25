import pygame
from utils import type_text
from constants import WIDTH_GAME, HEIGHT_GAME

def start_pause(screen):
    paused: bool = True
    clock = pygame.time.Clock()
    rect = pygame.Surface((WIDTH_GAME, HEIGHT_GAME))
    rect.set_alpha(127)
    screen.blit(rect, (0, 0))
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        type_text("Paused. Press ENTER to continue", WIDTH_GAME // 2, WIDTH_GAME // 2, screen)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False
        pygame.display.update()
        clock.tick(60)