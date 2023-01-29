import pygame


class Button:
    def __init__(self, text, x_pos, y_pos, enabled, font, screen, width):
        self.width = width
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.font = font
        self.draw(screen)

    def draw(self, screen):
        button_text = self.font.render(self.text, True, 'white')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, 65))
        pygame.draw.rect(screen, 'black', button_rect, 0, 5)
        pygame.draw.rect(screen, 'white', button_rect, 2, 5)
        screen.blit(button_text, (self.x_pos + 3, self.y_pos + 3))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, 65))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False