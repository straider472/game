import pygame
import random
from parametrs import *

class Player(pygame.sprite.Sprite):
    'Класс, описывающий главного героя'
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(background_player)
        self.image = pygame.transform.smoothscale(self.image, (100, 100))
        self.rect = self.image.get_rect()  # прямоугольник спрайта
        self.rect.center = (WIDTH / 2, HEIGHT / 2)  # место создания спрайта
        self.direction = "RIGHT"

    def update(self):  # метод обновления
        if self.direction == "LEFT":
            self.rect.right -= 10
        elif self.direction == "TOP":
            self.rect.top -= 10
        elif self.direction == "RIGHT":
            self.rect.right += 10
        elif self.direction == "BOTTOM":
            self.rect.top += 10

        # обработка выхода за границы экрана
        if self.rect.right > WIDTH or self.rect.right < 0\
                or self.rect.top > HEIGHT or self.rect.top < 0:
            if self.rect.right > WIDTH:
                self.rect.right = 0
            elif self.rect.right < 0:
                self.rect.right = WIDTH
            elif self.rect.top > HEIGHT:
                self.rect.top = 0
            elif self.rect.top < 0:
                self.rect.top = HEIGHT

class Coin(pygame.sprite.Sprite):
    'Класс, описывающий спрайт монетки'

    def __init__(self):  # конструктор класса
        pygame.sprite.Sprite.__init__(self)  # реализация базового конструктора класса
        self.image = pygame.image.load(background_coin)
        self.image = pygame.transform.smoothscale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.right = random.randint(40, 760)
        self.rect.top = random.randint(40, 760)

    def update(self):
        self.rect.right = random.randint(40, 760)
        self.rect.top = random.randint(40, 760)

class Thorn(pygame.sprite.Sprite):
    'Класс, описывающий спрайт шипов'

    def __init__(self):  # конструктор класса
        pygame.sprite.Sprite.__init__(self)  # реализация базового конструктора класса
        self.image = pygame.image.load(background_thorn)
        self.image = pygame.transform.smoothscale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.right = random.randint(40, 740)
        self.rect.top = random.randint(40, 740)

    def update(self):
        pass

class Mushroom(pygame.sprite.Sprite):
    'Класс, описывающий спрайт гриба'

    list_directions = ["LEFT", "TOP", "RIGHT", "BOTTOM"]
    def __init__(self):  # конструктор класса
        pygame.sprite.Sprite.__init__(self)  # реализация базового конструктора класса
        self.image = pygame.image.load(background_mushroom)
        self.image = pygame.transform.smoothscale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.right = random.randint(100, 700)
        self.rect.top = random.randint(100, 700)
        self.direction = self.list_directions[random.randint(0, 3)]
    def update(self):
            if self.direction == "LEFT":
                self.rect.right -= 5
            elif self.direction == "TOP":
                self.rect.top -= 5
            elif self.direction == "RIGHT":
                self.rect.right += 5
            elif self.direction == "BOTTOM":
                self.rect.top += 5

            # обработка выхода за границы экрана
            if self.rect.right > WIDTH or self.rect.right < 0 \
                    or self.rect.top > HEIGHT or self.rect.top < 0:
                if self.rect.right > WIDTH:
                    self.rect.right = 0
                elif self.rect.right < 0:
                    self.rect.right = WIDTH
                elif self.rect.top > HEIGHT:
                    self.rect.top = 0
                elif self.rect.top < 0:
                    self.rect.top = HEIGHT