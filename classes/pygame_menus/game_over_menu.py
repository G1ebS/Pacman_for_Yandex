import pygame
from classes.menu_classes.background import Background
from classes.menu_classes.button import Button
'''
function for game over screen
'''


def game_over_screen():
    pygame.init()
    pygame.font.init()
    WIDTH = 800
    HEIGHT = 600
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    fps = 60
    timer = pygame.time.Clock()
    font = pygame.font.Font("data/fonts/Pixeboy-z8XGD.ttf", 70)
    font2 = pygame.font.Font('data/fonts/Pixeboy-z8XGD.ttf', 150)
    pygame.display.set_caption("Pacman")

    global game_over
    game_over = True
    BG = Background('data/images/background_images/backgroundpicture.jpg', [0, 0])
    while game_over:
        pygame.display.set_caption("Game Over")
        game_over_message = "Game Over"
        ts = font2.render(game_over_message, False, (255, 255, 255))
        screen.fill([255, 255, 255])
        screen.blit(BG.image, BG.rect)
        timer.tick(fps)
        my_button1 = Button('Record', 275, 530, True, font, screen, 250)
        my_button2 = Button('  Menu', 540, 530, True, font, screen, 250)
        my_button3 = Button('Retry', 10, 530, True, font, screen, 250)
        screen.blit(ts, (110, 100))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'stop'
            if pygame.mouse.get_pressed()[0]:
                if my_button2.check_click():
                    pygame.quit()
                    return 'menu'
                if my_button3.check_click():
                    pygame.quit()
                    return 'retry'
                if my_button1.check_click():
                    pygame.quit()
                    return 'record'
