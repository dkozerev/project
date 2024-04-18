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

font1 = pygame.font.SysFont("Arial", 20)
font2 = pygame.font.SysFont("Arial", 50)


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
        if self.rect.y < 0:
                self.rect.y = 0
        elif self.rect.y > win_h - self.rect.height - 95:  # Отступ от нижней границы окна
            self.rect.y = win_h - self.rect.height - 95
    
class Block(GameSprite):
    def __init__(self, x, y, w, h, image):
        super().__init__(x, y, w, h, image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    







# Создаем экземпляры блоков и добавляем их в список blocks
coin_img = pygame.image.load("coin.png")
block_img = pygame.image.load("block.png")
block1 = Block(190, 350, 50, 50, block_img)
block2 = Block(280, 290, 50, 50, block_img)
block3 = Block(370, 230, 50, 50, block_img)
block4 = Block(460, 170, 50, 50, block_img)
block5 = Block(550, 120, 50, 50, block_img)
block6 = Block(600, 120, 50, 50, block_img)
block7 = Block(650, 120, 50, 50, block_img)
coin = Block(650, 70, 50, 50, coin_img)
blocks = [block1, block2, block3, block4,block5,block6,block7,coin]




player1 = pygame.image.load("1.png")
hero = Player(10,350, 50, 50, player1, 3)

game = True
game_over = False
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
    if hero.rect.collidepoint(coin.rect.center):  # Проверка столкновения с монеткой
        game_over = True
    if game_over:
        window.blit(font2.render("Победа!", True, (0, 255, 0)), (250, 250))

    clock.tick(fps)
    pygame.display.update()
pygame.quit()
