import pygame
from constants import PATH_TO_FONT
from datetime import datetime


"""
Checking if a certain time has passed
"""


def check_time(time, seconds, unit="seconds"):
    if unit == "seconds":
        if (datetime.now() - time).seconds >= seconds:
            return True
    elif unit == "microseconds":
        if (datetime.now() - time).microseconds >= seconds:
            return True

    return False


def type_text(
    message: str,
    x: int,
    y: int,
    display_to_type: pygame.Surface,
    font_size=30,
    font_type=PATH_TO_FONT,
    font_color=(0, 56, 124),
    position="center",
):
    font_to_print = pygame.font.Font(font_type, font_size)
    text = font_to_print.render(message, True, font_color)
    place = text.get_rect(center=(x, y))
    if position == "left_edge":
        place = text.get_rect(topleft=(x, y))
    # else:
    display_to_type.blit(text, place)
