import pygame
import os
import random

pygame.init()

win_w = 700
win_h = 500
fps = 60

window = pygame.display.set_mode((win_w, win_h))
clock = pygame.time.Clock()
background = pygame.image.load("img/country-platform-preview.png")
background = pygame.transform.scale(background, (win_w, win_h))

pygame.mixer_music.load("img/awesomeness.wav")
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.2)



class GameSprite:
    def __init__(self, x, y, w, h, image):
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.transform.scale(image, (w, h))
        self.image = image
    
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        print(self.rect.x,self.rect.y)



class Player(GameSprite):

    def __init__(self,x, y, w, h, image, speed):
        super().__init__(x, y, w, h, image)
        self.speed = speed
        self.image = image
        #self.image.set_colorkey(0)
        self.isJump = False
        self.jumpCount = 10

    def move(self):
        keys = pygame.key.get_pressed()
        
        if (keys[pygame.K_a]) and (self.rect.x >= 0):
            self.rect.x -= self.speed
            #self.image = 
            #self.image.set_colorkey(0)
            print(2)

        if (keys[pygame.K_d]) and (self.rect.x <= 1145):
            self.rect.x += self.speed
            #self.image = hero
            #self.image.set_colorkey(0)
            print(3)
        if keys[pygame.K_SPACE]:
            self.isJump = True
            print(1)

        if self.isJump:

            if self.jumpCount >= -10:

                if self.jumpCount < 0:
                    self.rect.y += (self.jumpCount ** 2) / 2
                else:
                    self.rect.y -= (self.jumpCount ** 2) / 2

                self.jumpCount -= 1

            else:
                self.isJump = False
                self.jumpCount = 10


player1 = pygame.image.load("img/1.png")
hero = Player(400,0, 50, 50, player1, 5)


game = True
while game:

    window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    hero.update()
    hero.move()
    

    pygame.display.flip()
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
