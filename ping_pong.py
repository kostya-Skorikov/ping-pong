from pygame import*
from pygame import *
from random import randint

init()
window = display.set_mode((700, 500)) 
display.set_caption('пин-понг') 
clock = time.Clock() 
background = transform.scale(image.load('fon.jpg'), (700, 500)) 


class GameSprite(sprite.Sprite):
    def __init__(self, image_load, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(image_load), (65, 65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Players(GameSprite):

    player_1_coords(350,10)
    player_1_coords(350,490)

    keys_pressed = key.get_pressed()

    if keys_pressed[K_UP]:
        player_2_coords[1] -= 5

    if keys_pressed[K_DOWN]:
        player_2_coords[1] += 5

    
    if keys_pressed[K_w]:
        player_1_coords[1] -= 5

    if keys_pressed[K_s]:
        player_1_coords[1] += 5


        
game = True

while game:
    window.blit(background, (0, 0)) 
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)

quit()


