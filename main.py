import pygame
import os
import random

pygame.init()

win_w = 700
win_h = 500
fps = 60

window = pygame.display.set_mode((win_w, win_h))
clock = pygame.time.Clock()
background = pygame.image.load("country-platform-preview.png")
background = pygame.transform.scale(background, (win_w, win_h))

pygame.mixer_music.load("awesomeness.wav")
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
            

        if (keys[pygame.K_d]) and (self.rect.x <= 1145):
            self.rect.x += self.speed
            #self.image = hero
            #self.image.set_colorkey(0)
            
        if keys[pygame.K_SPACE]:
            self.isJump = True
            

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
            if not any(block.rect.colliderect(self.rect.move(0, 1)) for block in blocks):
                self.rect.y += 5  # Скорость спуска
            # Проверяем, что игрок не спускается ниже, чем верхняя граница блока или платформы
                for block in blocks:
                    if self.rect.colliderect(block.rect) and self.rect.bottom > block.rect.top:
                        self.rect.bottom = block.rect.top

class Block(GameSprite):
    def __init__(self, x, y, w, h, image):
        super().__init__(x, y, w, h, image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
# Создаем экземпляры блоков и добавляем их в список blocks
block_img = pygame.image.load("block.png")
block1 = Block(200, 350, 50, 50, block_img)
block2 = Block(290, 290, 50, 50, block_img)
block3 = Block(380, 230, 50, 50, block_img)
block4 = Block(470, 170, 50, 50, block_img)
blocks = [block1, block2, block3, block4]




player1 = pygame.image.load("1.png")
hero = Player(10,350, 50, 50, player1, 3)


game = True
while game:

    window.blit(background, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    hero.update()
    hero.move()

    for block in blocks:
        block.update()
        window.blit(block.image, (block.rect.x, block.rect.y))
        keys = pygame.key.get_pressed()
        if hero.rect.colliderect(block.rect):
            if hero.rect.bottom >= block.rect.top and hero.rect.top < block.rect.top:
                hero.rect.bottom = block.rect.top
                hero.isJump = False
                hero.jumpCount = 10


    pygame.display.update()
    clock.tick(fps)

pygame.quit()
