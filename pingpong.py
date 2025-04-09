from pygame import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup

mixer.init()

game = True
win = display.set_mode((700, 500))
mixer.music.load("good_music.mp3")
win_height = 500
win_width = 700
display.set_caption("Весёлый Пинг-Понг 1vs1")
background = transform.scale(image.load("tennis_back.png"), (700, 500))
mixer.music.play(-1)
mixer.music.set_volume(0.5)

clock = time.Clock()
FPS = 60
finish = 0
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
        self.speed = player_speed

    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 370:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

player_l = Player("palka0.png", 30, 5, 50, 125, 5)
player_r = Player("palka0.png", 620, 365, 50, 125, 5)

while game:
    win.blit(background, (0, 0))
    for a in event.get():
        if a.type == QUIT:
            game = False
    if finish != 1 and finish != -1:
        win.blit(background, (0,0))
        player_l.update_l()
        player_r.update_r()
        player_l.reset()
        player_r.reset()

    clock.tick(FPS)
    display.update()