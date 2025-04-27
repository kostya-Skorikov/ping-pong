import pygame
from pygame import *
from random import choice

WIDTH, HEIGHT = 700, 500

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Пин-понг') 
clock = pygame.time.Clock() 

player_width = 10  
player_height = 100 
ball_size = 30  

class GameSprite(sprite.Sprite):
    def __init__(self, image_load, speed, x, y):
        super().__init__()
        self.image = transform.scale(pygame.image.load(image_load), (player_width, player_height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, image_load, speed, x, y):
        super().__init__(image_load, speed, x, y)

    def update(self):
        keys_pressed = key.get_pressed()
        if self.rect.x == 10:
            if keys_pressed[K_w] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys_pressed[K_s] and self.rect.y < window.get_height() - self.rect.height:
                self.rect.y += self.speed
        if self.rect.x == WIDTH - player_width - 10:
            if keys_pressed[K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys_pressed[K_DOWN] and self.rect.y < window.get_height() - self.rect.height:
                self.rect.y += self.speed

class Ball(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Surface((ball_size, ball_size), SRCALPHA)
        draw.circle(self.image, (255, 255, 255), (ball_size // 2, ball_size // 2), ball_size // 2)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.dx = choice([-5, 5])  
        self.dy = choice([-5, 5])  

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy *= -1
        
        if sprite.collide_rect(self, player_1) or sprite.collide_rect(self, player_2):
            self.dx *= -1  

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.dx = choice([-5, 5])  
        self.dy = choice([-5, 5])  

game = True

player_1 = Player('player.png', 5 ,10 , HEIGHT // 2 - player_height // 2)   
player_2 = Player('player.png', 5 , WIDTH - player_width - 10 , HEIGHT // 2 - player_height // 2)   
ball = Ball()

score_1 = score_2 = 0

font = pygame.font.Font(None, 36)

while game:
    window.fill((0, 0, 0))  
    for e in event.get():
        if e.type == QUIT:
            game = False

    player_1.update()
    player_2.update()
    ball.update()   

    player_1.reset()
    player_2.reset()
    window.blit(ball.image, ball.rect)

    if ball.rect.left <= 0:
        score_2 += 1
        print("Игрок 2 набрал очко!")
        ball.reset()   
    
    if ball.rect.right >= WIDTH:
        score_1 += 1
        print("Игрок 1 набрал очко!")
        ball.reset()   
    
    score_text = font.render(f"Игрок 1: {score_1} | Игрок 2: {score_2}", True, (255,255,255))
    window.blit(score_text,(WIDTH//4 ,10))

    pygame.display.update()  
    clock.tick(60)

pygame.quit()
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


