import pygame
import time
from helper import *
from Levels.level_1 import start_level
from parametrs import *


# игровое окно
pygame.init()  # запуск pygame
pygame.mixer.init()  # запуск работы звука
pygame.display.set_caption("Моя первая игра")  # заголовок
pygame.display.set_icon(icon)

start_level()  # запуск первого уровня

