import pygame
import random
from field import arr
from utils import check_time
from datetime import datetime
import math
from time import sleep

antonims = {"left": "right", "right": "left", "top": "bottom", "bottom": "top"}
vector_to_dir = {"left": "x", "right": "x", "bottom": "y", "top": "y"}


'''
4 classes for ghost.
Now it is +-copy-paste, but in future it is easier to do ghost algorithm, like in original pacman
'''


class Red(pygame.sprite.Sprite):
    target_x: int
    target_y: int
    def __init__(self, screen, *groups):
        super().__init__(groups)
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('data/images/ghosts_images/red.png'), (16, 16))
        self.fear_image = pygame.transform.scale(pygame.image.load('data/images/ghosts_images/ghost_in_fear.png'), (16, 16))
        self.IMAGE_CONST = self.image.copy()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = 13 * 16 + 8 # 48
        self.rect.y = 15 * 16 # 32
        self.direction = 1
        self.velocity = 0
        self.vector = 0
        self.dir = ""
        self.last = "right"
        self.going = True
        self.vector = random.choice(["right", "left"])
        self.tp = True
        self.collide_with_energazed = False
        self.last_spawn_time = datetime.now()
        self.fear = False
        self.start = True

    def output(self):
        self.screen.blit(self.image, self.rect)
    
    def collide_with_walls(self):
        x_top_right, y_top_right = self.rect.topright
        x_bottom_left, y_bottom_left = self.rect.bottomleft
        print(x_top_right, y_bottom_left)
        return True if (x_top_right) % 16 == 0 and (y_bottom_left) % 16 == 0 else False

    def update(self, pacman, array):
        (self.collide_with_walls())
        # sleep(0.5)
        print()
        field = arr
        if array:
            field = array
        if pacman.energized and not self.fear:
            self.image = self.fear_image
            self.fear = True
        elif not pacman.energized and self.fear:
            self.fear = False
            self.image = self.IMAGE_CONST
        if self.collide_with_energazed:
            self.kill()
        if check_time(self.last_spawn_time, 10 ** 6 // 2, "microseconds"):
            if self.tp:
                self.rect.x -= 8
                self.rect.y -= 16 * 3
                self.tp = False
        if not self.tp:
            # if self.rect.x != 16 * 13 and self.rect.y != 16 * 12 and self.start:
            #     print(0)
            #     self.start = False
            can_go = []
            dirs = set()
            try:
                if field[self.rect.centery // 16][(self.rect.right + 1) // 16] % 100 == 0 and self.rect.top % 16 == 0:  #
                    # if self.vector == "right":
                    #     self.rect.x += 2
                    can_go.append("right")
                    dirs.add("x")
                if field[self.rect.centery // 16][(self.rect.left - 2) // 16] % 100 == 0 and self.rect.top % 16 == 0:  #
                    # if self.vector == "left":
                    #     self.rect.x -= 2
                    # self.rect.centerx -= 2
                    can_go.append("left")
                    dirs.add("x")
                    if self.rect.x < 0:
                        self.rect.x = self.screen_rect.right
                if field[(self.rect.top - 2) // 16][self.rect.centerx // 16] % 100 == 0 and self.rect.right % 16 == 0:  #
                    # if self.vector == "top":
                    #     self.rect.y -= 2
                    # self.rect.centery -= 2
                    can_go.append("top")
                    dirs.add("y")
                if field[(self.rect.bottom + 1) // 16][self.rect.centerx // 16] % 100 == 0 and self.rect.right % 16 == 0:  #
                    # if self.vector == "bottom":
                    #     self.rect.y += 2
                    # self.rect.centery += 2
                    can_go.append("bottom")
                    dirs.add("y")
                can_go = list(set(can_go))
            except IndexError:
                self.rect.x = self.screen_rect.left

            # from time import sleep
            print(dirs)
            print(can_go)
            print(self.rect.top)
            if len((((dirs)))) >= 2:# self.dir
                self.going = False

            if not self.going:
                print(self.vector)
                self.going = True   
                print(self.vector)
                if (self.fear):
                    print(1)
                    print(self.fear, self.start)
                    print(can_go)
                    self.going = True
                    new_vector = random.choice(can_go)
                    self.vector = new_vector
                    if dir == "left":
                        self.dir = "x"
                    elif dir == "right":
                        self.dir = "x"
                    elif dir == "top":
                        self.dir = "y"
                    elif dir == "bottom":
                        self.dir = "y"
                    print(2)
                    # self.going = True
                elif len(can_go) > 2:
                    print(can_go)
                    self.mark_target(pacman)
                    print("i")
                    distances = list()
                    for new_vector in can_go:
                        current_x = self.rect.x
                        current_y = self.rect.y
                        if new_vector == "left" and self.vector != "right":
                            distances.append((math.sqrt(((current_x - 2) - self.target_x) ** 2 + (current_y - self.target_y) ** 2), "left"))
                        if new_vector == "right" and self.vector != "left":
                            distances.append((math.sqrt(((current_x + 2) - self.target_x) ** 2 + (current_y - self.target_y) ** 2), "right"))
                        if new_vector == "top" and self.vector != "bottom":
                            distances.append((math.sqrt(((current_x) - self.target_x) ** 2 + ((current_y - 2) - self.target_y) ** 2), "top"))
                        if new_vector == "bottom" and self.vector != "top":
                            distances.append((math.sqrt(((current_x) - self.target_x) ** 2 + ((current_y + 2) - self.target_y) ** 2), "bottom"))
                    print(distances)
                    choose = min(distances, key=lambda x: x[0])
                    self.vector = choose[1]
                    self.dir = vector_to_dir[choose[1]]
                    print(self.vector)
                else:
                    print("e")
                    print(can_go)
                    print(self.vector)
                    for new_vector in can_go:
                        if antonims[new_vector] != self.vector: 
                            print(new_vector)
                            self.vector = new_vector
                            self.dir = vector_to_dir[new_vector]
                            break
            if self.vector == "right":
                self.rect.x += 2
            if self.vector == "left":
                self.rect.x -= 2
            if self.vector == "top":
                self.rect.y -= 2
            if self.vector == "bottom":
                self.rect.y += 2
                
                
    def mark_target(self, pacman):
        self.target_x = pacman.rect.x
        self.target_y = pacman.rect.y


class Blue(pygame.sprite.Sprite):
    def __init__(self, screen, *groups):
        super().__init__(groups)
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('data/images/ghosts_images/blue.png'), (16, 16))
        self.fear_image = pygame.transform.scale(pygame.image.load('data/images/ghosts_images/ghost_in_fear.png'), (16, 16))
        self.IMAGE_CONST = self.image.copy()

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = 13 * 16 + 8 # 48
        self.rect.y = 15 * 16 # 32
        self.direction = 1
        self.velocity = 0
        self.vector = 0
        self.dir = ""
        self.last = "right"
        self.going = False
        self.vector = ""
        self.tp = True
        self.collide_with_energazed = False
        self.last_spawn_time = datetime.now()
        self.fear = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update(self, pacman, array):
        field = arr
        if array:
            field = array
        if pacman.energized and not self.fear:
            self.image = self.fear_image
            self.fear = True
        elif not pacman.energized and self.fear:
            self.fear = False
            self.image = self.IMAGE_CONST
        if self.collide_with_energazed:
            self.kill()
        if check_time(self.last_spawn_time, 5):
            if self.tp:
                self.rect.x -= 8
                self.rect.y -= 16 * 3
                self.tp = False
        if not self.tp:
            can_go = []
            dirs = set()
            try:
                if field[self.rect.centery // 16][(self.rect.right + 1) // 16] % 100 == 0 and self.rect.top % 16 == 0:  #
                    if self.vector == "right":
                        self.rect.x += 2
                    can_go.append("right")
                    dirs.add("x")
                if field[self.rect.centery // 16][(self.rect.left - 2) // 16] % 100 == 0 and self.rect.top % 16 == 0:  #
                    if self.vector == "left":
                        self.rect.x -= 2
                    # self.rect.centerx -= 2
                    can_go.append("left")
                    dirs.add("x")
                    if self.rect.x < 0:
                        self.rect.x = self.screen_rect.right
                if field[(self.rect.top - 2) // 16][self.rect.centerx // 16] % 100 == 0 and self.rect.right % 16 == 0:  #
                    if self.vector == "top":
                        self.rect.y -= 2
                    # self.rect.centery -= 2
                    can_go.append("top")
                    dirs.add("y")
                if field[(self.rect.bottom + 1) // 16][self.rect.centerx // 16] % 100 == 0 and self.rect.right % 16 == 0:  #
                    if self.vector == "bottom":
                        self.rect.y += 2
                    # self.rect.centery += 2
                    can_go.append("bottom")
                    dirs.add("y")
                can_go = list(set(can_go))
            except IndexError:
                self.rect.x = self.screen_rect.left

            # from time import sleep
            if len((list(set(self.dir).union(dirs)))) >= 2:
                self.going = False

            if not self.going:
                self.going = True
                dir = random.choice(can_go)
                self.vector = dir
                if dir == "left":
                    self.dir = "x"
                elif dir == "right":
                    self.dir = "x"
                elif dir == "top":
                    self.dir = "y"
                elif dir == "bottom":
                    self.dir = "y"


class Orange(pygame.sprite.Sprite):
    def __init__(self, screen, *groups):
        super().__init__(groups)
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('data/images/ghosts_images/orange.png'), (16, 16))
        self.fear_image = pygame.transform.scale(pygame.image.load('data/images/ghosts_images/ghost_in_fear.png'), (16, 16))
        self.IMAGE_CONST = self.image.copy()

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = 13 * 16 + 8 # 48
        self.rect.y = 15 * 16 # 32
        self.direction = 1
        self.velocity = 0
        self.vector = 0
        self.dir = ""
        self.last = "right"
        self.going = False
        self.vector = ""
        self.tp = True
        self.collide_with_energazed = False
        self.last_spawn_time = datetime.now()
        self.fear = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update(self, pacman, array):
        field = arr
        if array:
            field = array
        if pacman.energized and not self.fear:
            self.image = self.fear_image
            self.fear = True
        elif not pacman.energized and self.fear:
            self.fear = False
            self.image = self.IMAGE_CONST
        if self.collide_with_energazed:
            self.kill()
        if check_time(self.last_spawn_time, 6):
            if self.tp:
                self.rect.x -= 8
                self.rect.y -= 16 * 3
                self.tp = False
        if not self.tp:
            can_go = []
            dirs = set()
            try:
                if field[self.rect.centery // 16][(self.rect.right + 1) // 16] % 100 == 0 and self.rect.top % 16 == 0:  #
                    if self.vector == "right":
                        self.rect.x += 2
                    can_go.append("right")
                    dirs.add("x")
                if field[self.rect.centery // 16][(self.rect.left - 2) // 16] % 100 == 0 and self.rect.top % 16 == 0:  #
                    if self.vector == "left":
                        self.rect.x -= 2
                    # self.rect.centerx -= 2
                    can_go.append("left")
                    dirs.add("x")
                    if self.rect.x < 0:
                        self.rect.x = self.screen_rect.right
                if field[(self.rect.top - 2) // 16][self.rect.centerx // 16] % 100 == 0 and self.rect.right % 16 == 0:  #
                    if self.vector == "top":
                        self.rect.y -= 2
                    # self.rect.centery -= 2
                    can_go.append("top")
                    dirs.add("y")
                if field[(self.rect.bottom + 1) // 16][self.rect.centerx // 16] % 100 == 0 and self.rect.right % 16 == 0:  #
                    if self.vector == "bottom":
                        self.rect.y += 2
                    # self.rect.centery += 2
                    can_go.append("bottom")
                    dirs.add("y")
                can_go = list(set(can_go))
            except IndexError:
                self.rect.x = self.screen_rect.left

        # from time import sleep
            if len((list(set(self.dir).union(dirs)))) >= 2:
                self.going = False

            if not self.going:
                self.going = True
                dir = random.choice(can_go)
                self.vector = dir
                if dir == "left":
                    self.dir = "x"
                elif dir == "right":
                    self.dir = "x"
                elif dir == "top":
                    self.dir = "y"
                elif dir == "bottom":
                    self.dir = "y"


class Pink(pygame.sprite.Sprite):
    def __init__(self, screen, *groups):
        super().__init__(groups)
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('data/images/ghosts_images/pink.png'), (16, 16))
        self.fear_image = pygame.transform.scale(pygame.image.load('data/images/ghosts_images/ghost_in_fear.png'), (16, 16))
        self.IMAGE_CONST = self.image.copy()

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = 13 * 16 + 8 # 48
        self.rect.y = 15 * 16 # 32
        self.direction = 1
        self.velocity = 0
        self.vector = 0
        self.dir = ""
        self.last = "right"
        self.going = False
        self.vector = ""
        self.tp = True
        self.collide_with_energazed = False
        self.last_spawn_time = datetime.now()
        self.fear = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update(self, pacman, array):
        field = arr
        if array:
            field = array
        if pacman.energized and not self.fear:
            self.image = self.fear_image
            self.fear = True
        elif not pacman.energized and self.fear:
            self.fear = False
            self.image = self.IMAGE_CONST
        if self.collide_with_energazed:
            self.kill()
        if check_time(self.last_spawn_time, 7):
            if self.tp:
                self.rect.x -= 8
                self.rect.y -= 16 * 3
                self.tp = False
        if not self.tp:
            can_go = []
            dirs = set()
            try:

                if field[self.rect.centery // 16][(self.rect.right + 1) // 16] % 100 == 0 and self.rect.top % 16 == 0:  #
                    if self.vector == "right":
                        self.rect.x += 2
                    can_go.append("right")
                    dirs.add("x")
                if field[self.rect.centery // 16][(self.rect.left - 2) // 16] % 100 == 0 and self.rect.top % 16 == 0:  #
                    if self.vector == "left":
                        self.rect.x -= 2
                    # self.rect.centerx -= 2
                    can_go.append("left")
                    dirs.add("x")
                    if self.rect.x < 0:
                        self.rect.x = self.screen_rect.right
                if field[(self.rect.top - 2) // 16][self.rect.centerx // 16] % 100 == 0 and self.rect.right % 16 == 0:  #
                    if self.vector == "top":
                        self.rect.y -= 2
                    # self.rect.centery -= 2
                    can_go.append("top")
                    dirs.add("y")
                if field[(self.rect.bottom + 1) // 16][self.rect.centerx // 16] % 100 == 0 and self.rect.right % 16 == 0:  #
                    if self.vector == "bottom":
                        self.rect.y += 2
                    # self.rect.centery += 2
                    can_go.append("bottom")
                    dirs.add("y")
                can_go = list(set(can_go))
            except IndexError:
                self.rect.x = self.screen_rect.left

            # from time import sleep
            if len((list(set(self.dir).union(dirs)))) >= 2:
                self.going = False

            if not self.going:
                self.going = True
                dir = random.choice(can_go)
                self.vector = dir
                if dir == "left":
                    self.dir = "x"
                elif dir == "right":
                    self.dir = "x"
                elif dir == "top":
                    self.dir = "y"
                elif dir == "bottom":
                    self.dir = "y"