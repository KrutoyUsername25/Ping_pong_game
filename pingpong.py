from pygame import *
from random import *
from time import time as time1
font.init()
#?mixer.init()
#!music = mixer.music.load('space.ogg')
clock = time.Clock()
window = display.set_mode((700, 500))
display.set_caption('Пинг понг')
background = transform.scale(image.load('9hq.webp'), (700, 500))
game = True
font2 = font.SysFont('Arial', 36)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, rect_x, rect_y, speed, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y <= 350:
            self.rect.y += self.speed
    def update2(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y <= 350:
            self.rect.y += self.speed

speed_x = 3
speed_y = 3
racket = Player('racket.png', 5, 180, 15, 50, 150)
racket1 = Player('racket.png', 650, 180, 15, 50, 150)
ball = GameSprite('pingball.png', 300, 220, 15, 80, 80)
wintext1 = font2.render('Победил игрок: номер 1', True, (0, 0, 0))
wintext2 = font2.render('Победил игрок: номер 2', True, (0, 0, 0))
game_stop = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if game_stop != True:
        window.blit(background, (0, 0))
        ball.reset()
        racket.reset()
        racket1.reset()
        racket.update()
        racket1.update2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(ball, racket) or sprite.collide_rect(ball, racket1):
            speed_x *= -1
        if ball.rect.y >= 420 or ball.rect.y <= 0:
            speed_y *= -1
        if ball.rect.x < 0:
            window.blit(wintext2, (250, 220))
            game_stop = True
        elif ball.rect.x >= 700:
            window.blit(wintext1, (250, 200))
            game_stop = True
    display.update()
    clock.tick(60)