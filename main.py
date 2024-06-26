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

class Button:
    def __init__(self, x, y, w, h, image1, image2):
        self.rect = pygame.Rect(x, y, w, h)
        self.image1 = pygame.transform.scale(image1, (w, h))
        self.image2 = pygame.transform.scale(image2, (w, h))
        self.image = self.image1

    def reset(self, x, y):
        self.animate(x, y)
        window.blit(self.image, (self.rect.x, self.rect.y))

    def animate(self, x, y):
        if self.rect.collidepoint(x, y):
            self.image = self.image2
        else:
            self.image = self.image1
        
play_img = pygame.image.load("Play (1).png")
options_img = pygame.image.load("options.png")
quit_img = pygame.image.load("Quit.png")
quit_img2 = pygame.image.load("Quit2.png")
update_img = pygame.image.load("Update.png")



btn_play = Button(win_w//2-100, (win_h-10)//5, 200, 50, play_img, play_img)
btn_options = Button(win_w//2-100, (win_h-10)//5*2, 200, 50, options_img, options_img)
btn_quit = Button(win_w//2-100, (win_h-10)//5*3, 200, 50, quit_img, quit_img2)

btn_menu = Button(win_w//2-100, (win_h-10)//2, 200, 50, update_img, update_img)
btn_menu2 = Button(0, 0, 50, 20, update_img, update_img)

game = True

screen = "menu"

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
        else:
            if not self.onBlock:
                self.rect.y += 5
#            if not any(block.rect.colliderect(self.rect.move(0, 1)) for block in blocks):
#                self.rect.y += 5  # Скорость спуска
    # Проверяем, что игрок не спускается ниже, чем верхняя граница блока или платформы
#               for block in blocks:
                    #if self.rect.colliderect(block.rect) and self.rect.bottom > block.rect.top:
                    #    self.rect.bottom = block.rect.top
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > win_h - self.rect.height - 95:  # Отступ от нижней границы окна
            self.rect.y = win_h - self.rect.height - 95
        
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > win_w - self.rect.width - 10:
            self.rect.x = win_w - self.rect.width - 10
    def collide_block(self):
        for block in blocks:
            if self .rect.bottom >= block.rect.top-55 and self.rect.bottom< block.rect.top +5 and self.rect.right > block.rect.left and self.rect.x < block.rect.right:
                self.rect.bottom = block.rect.y - 50
                self.onBlock = True
                return
        self.onBlock = False    
        


# Создаем экземпляры блоков и добавляем их в список blocks
coin_img = pygame.image.load("coin.png")
block_img = pygame.image.load("block.png")
block1 = GameSprite(190, 350, 50, 50, block_img)
block2 = GameSprite(280, 290, 50, 50, block_img)
block3 = GameSprite(370, 230, 50, 50, block_img)
block4 = GameSprite(460, 170, 50, 50, block_img)
block5 = GameSprite(550, 120, 50, 50, block_img)
block6 = GameSprite(600, 120, 50, 50, block_img)
block7 = GameSprite(650, 120, 50, 50, block_img)
coin = GameSprite(650, 70, 50, 50, coin_img)
coin2 = GameSprite(600, 120, 50, 50, coin_img)
coin_img = pygame.image.load("coin.png")
blocks = [block1, block2, block3, block4,block5,block6,block7]
coins = [coin]



player1 = pygame.image.load("1.png")
hero = Player(10,350, 50, 50, player1, 3)

game = True
game_over = False
while game:

    window.blit(background, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    mouse_x, mouse_y = pygame.mouse.get_pos()


    if screen == "menu":
        window.blit(background, (0, 0))
        btn_play.reset(mouse_x, mouse_y)
        btn_options.reset(mouse_x, mouse_y)
        btn_quit.reset(mouse_x, mouse_y)
        

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = e.pos
                if btn_options.rect.collidepoint(x, y):
                    screen = "options"
                elif btn_play.rect.collidepoint(x, y):

                    screen = "play"
                elif btn_quit.rect.collidepoint(x, y):

                    game = False

             
    elif screen == "options":
        window.blit(background, (0, 0))
        btn_menu.reset(mouse_x, mouse_y)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = e.pos
                if btn_menu.rect.collidepoint(x, y):

                    screen = "menu"


    if screen == "play":
        window.blit(background, (0, 0))
        btn_menu2.reset(mouse_x, mouse_y)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = e.pos
                if btn_menu2.rect.collidepoint(x, y):

                    screen = "menu"
        hero.collide_block()
        hero.update()
        hero.move()
        coin.update()
    
    
        for block in blocks:
            block.update()
    
    
        for coin in coins:
            coin.update()
            if hero.rect.colliderect(coin.rect):
                coins.remove(coin) 
    
    
    
        if hero.rect.collidepoint(coin.rect.center):  # Проверка столкновения с монеткой
            game_over = True
        if game_over:
            window.blit(font2.render("Победа!", True, (0,191,255)), (250, 20))


    clock.tick(fps)
    pygame.display.update()
pygame.quit()
