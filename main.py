import pygame
import sys

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


class Pers(GameSprite):
    def __init__(self, x, y, w, h, image, speed):
        super().__init__(x, y, w, h, image)
        self.speed = speed

    def move(self, key_left, key_right):
        k = pygame.key.get_pressed()
        if k[key_right]:
            if self.rect.right <= win_w:
                self.rect.x += self.speed 
        elif k[key_left]:
            if self.rect.left >= 0:
                self.rect.x -= self.speed


animation_set = [pygame.image.load(f"{i}.png") for i in range(1, 4)]

current_frame = 0
frame_counter = 0
player = Pers(100, 100, 50, 50, pygame.image.load("1.png"), 5)

game = True
while game:

    window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    player.move(pygame.K_LEFT, pygame.K_RIGHT)
    player.update()

    frame_counter += 1
    if frame_counter >= fps:
        frame_counter = 0
        current_frame = (current_frame + 1) % len(animation_set)

    window.blit(animation_set[current_frame], (player.rect.x, player.rect.y))

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
sys.exit()
