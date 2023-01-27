import pygame
import random
from field import arr
from utils import check_time
from datetime import datetime
from constants import WIDTH_GAME
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
        print(groups)
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
        self.going = True
        self.vector = random.choice(["right", "left"])
        self.tp = True
        self.collide_with_energazed = False
        self.last_spawn_time = datetime.now()
        self.fear = True
        self.start = True
        self.time_to_tp = 10 ** 6 // 2
        self.type_time_for_tp = "microseconds"
        self.counter = 0
        self.last_check_time = datetime.now()

    def output(self):
        self.screen.blit(self.image, self.rect)
    
    def collide_with_walls(self):
        x_top_right, y_top_right = self.rect.topright
        x_bottom_left, y_bottom_left = self.rect.bottomleft
        print(x_top_right, y_bottom_left)
        return True if (x_top_right) % 16 == 0 and (y_bottom_left) % 16 == 0 else False

    def update(self, pacman, array):
        # (self.collide_with_walls())
        # sleep(0.5)
        # print()
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
        if check_time(self.last_spawn_time, self.time_to_tp, self.type_time_for_tp):
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
                    # if self.rect.x <= 0:
                    #     self.rect.x = self.screen_rect.right
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
                pass

            print(dirs)
            print(can_go)
            print(self.rect.x)
            if len((((dirs)))) >= 2:# self.dir
                self.going = False

            if not self.going:
                self.going = True   
                if (self.fear):
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
                    # self.going = True
                elif len(can_go) > 2:
                    self.mark_target(pacman)
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
                    choose = min(distances, key=lambda x: x[0])
                    self.vector = choose[1]
                    self.dir = vector_to_dir[choose[1]]
                else:
                    for new_vector in can_go:
                        if antonims[new_vector] != self.vector: 
                            print(new_vector)
                            self.vector = new_vector
                            self.dir = vector_to_dir[new_vector]
                            break
            print(self.vector)
            if self.vector == "right":
                self.rect.x += 2
                if self.rect.x > WIDTH_GAME:
                    self.rect.x = self.screen_rect.left
            if self.vector == "left":
                self.rect.x -= 2
                if self.rect.x <= 0:
                    # print(1)
                    self.rect.x = WIDTH_GAME
            if self.vector == "top":
                self.rect.y -= 2
            if self.vector == "bottom":
                self.rect.y += 2
                
                
    def mark_target(self, pacman):
        if self.counter % 2:
            # self.counter += 1
            self.target_x = pacman.rect.x
            self.target_y = pacman.rect.y
            if check_time(self.last_check_time, 6, "seconds"):
                self.last_check_time = datetime.now()
                self.counter += 1       
        elif not self.counter % 2:
            # self.counter += 1
            self.target_x = 16 * 23
            self.target_y = 16 * 0
            # self.last_check_time = datetime.now()
            if check_time(self.last_check_time, 10, "seconds"):
                self.last_check_time = datetime.now()
                self.counter += 1






class Pink(Red):
    def __init__(self, screen, *groups):
        super().__init__(screen, groups)
        self.image = pygame.transform.scale(pygame.image.load('data/images/ghosts_images/pink.png'), (16, 16))
        self.IMAGE_CONST = self.image.copy()
        self.time_to_tp = 7
        self.type_time_for_tp = "seconds"


    def mark_target(self, pacman):
        self.target_x = pacman.rect.x
        self.target_y = pacman.rect.y
        if pacman.direction == 0:
            self.target_x = min(WIDTH_GAME, self.target_x + 16 * 4)
        elif pacman.direction == 1:
            self.target_x = max(0, self.target_x - 16 * 4)
        if pacman.direction == 2:
            self.target_y = max(0, self.target_y - 16 * 4)
        elif pacman.direction == 3:
            self.target_y = min(WIDTH_GAME,  self.target_y + 16 * 4)
        


class Blue(Red):
    def __init__(self, screen, red_ghost: Red, *groups):
        print(screen, red_ghost, groups)
        super().__init__(screen, groups)
        self.time_to_tp = 7
        self.type_time_for_tp = "seconds"
        self.image = pygame.transform.scale(pygame.image.load('data/images/ghosts_images/blue.png'), (16, 16))
        self.IMAGE_CONST = self.image.copy()
        self.red_ghost = red_ghost
    

    def mark_target(self, pacman):
        self.target_x = pacman.rect.x + 2 * 16 * ((self.red_ghost.rect.x // 16) - (pacman.rect.x // 16))
        self.target_y = pacman.rect.y + 2 * 16 * ((self.red_ghost.rect.y // 16) - (pacman.rect.y // 16))



class Orange(Red):
    def __init__(self, screen, *groups):
        super().__init__(screen, groups)
        self.image = pygame.transform.scale(pygame.image.load('data/images/ghosts_images/orange.png'), (16, 16))
        self.IMAGE_CONST = self.image.copy()
        self.time_to_tp = 6
        self.type_time_for_tp = "seconds"

    def mark_target(self, pacman):
        distance_to_pacman = math.sqrt((self.rect.x - pacman.rect.x) ** 2 + (self.rect.y - pacman.rect.x) ** 2)
        if distance_to_pacman >= 8:
            self.target_x = pacman.rect.x
            self.target_y = pacman.rect.y
        else:
            self.target_x = 0            
            self.target_y = 512




    

