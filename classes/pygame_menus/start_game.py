import sys
from classes.menu_classes.button import Button
from classes.menu_classes.background import Background
import pygame



def start():
    pygame.init()
    pygame.font.init()
    WIDTH = 800
    HEIGHT = 600
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    fps = 60
    timer = pygame.time.Clock()
    pygame.display.set_caption("Pacman")
    pygame.display.set_caption("Menu")
    run = True
    font = pygame.font.Font("data/fonts/Pixeboy-z8XGD.ttf", 50)
    font2 = pygame.font.Font("data/fonts/Pixeboy-z8XGD.ttf", 165)
    BG = Background('data/images/background_images/backgroundpicture.jpg', [0, 0])

    while run:
        title = "Pacman"
        ts1 = font2.render(title, False, (255, 255, 255))
        screen.blit(BG.image, BG.rect)

        timer.tick(fps)
        my_button1 = Button('      Exit', 5, 530, True, font, screen, 190)
        my_button2 = Button('   Rating', 207, 530, True, font, screen, 190)
        my_button3 = Button('Settings', 409, 530, True, font, screen, 190)
        my_button4 = Button('    Start', 611, 530, True, font, screen, 190)
        my_button5 = Button('   Editor', (WIDTH - 190) // 2, 455, True, font, screen, 190)

        screen.blit(ts1, (90, 50))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if pygame.mouse.get_pressed()[0]:
                if my_button1.check_click():
                    run = False
                    pygame.quit()
                    return 'exit'
                elif my_button4.check_click():
                    run = False
                    pygame.quit()
                    return 'game'
                elif my_button2.check_click():
                    pygame.quit()
                    return 'leaderboard'
                elif my_button3.check_click():
                    pygame.quit()
                    return 'settings'
                elif my_button5.check_click():
                    pygame.quit()
                    return 'editor'


if __name__ == '__main__':
    start()