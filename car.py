import pygame
import math
from pygame.locals import *
from pygame.math import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WHITE = [255, 255, 255]

def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect

class Car(pygame.sprite.Sprite):
    
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('car_'+color+'.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(SCREEN_WIDTH/20), int(SCREEN_HEIGHT/20)))
        self.image = pygame.transform.rotate(self.image, 90)
        self.original_image = self.image    
    
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect()
        self.rect[0] = 50 
        self.rect[1] = 100 
        
        self.position = Vector2((self.rect[0], self.rect[1]))
        self.direction = Vector2(1, 0)
        
        self.speed = 0
        self.angle_speed = 0
        self.angle = 0
        #self.image, self.rect = rot_center(self.image, self.rect, 90)
        
    def update(self):
        if(self.angle_speed != 0):
            self.direction.rotate_ip(self.angle_speed)
            self.angle += self.angle_speed
            self.image = pygame.transform.rotate(self.original_image, -self.angle)
            self.rect = self.image.get_rect(center = self.rect.center)
        self.position += self.direction * self.speed
        self.rect.center = self.position
        
        #print(pygame.Surface.get_at((self.rect[0], self.rect[1])))
class Background(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pista.png')
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        #self.mask = pygame.mask.from_threshold(self.image, pygame.Color('black'))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
def clear_callback(surf, rect):
    color = 255, 255, 255
    surf.fill(color, rect)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)

background_group = pygame.sprite.Group()
BACKGROUND = Background()
background_group.add(BACKGROUND)

car_group = pygame.sprite.Group()
car = Car('red')
car_group.add(car)



clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                car.speed += 1
            elif event.key == pygame.K_DOWN:
                car.speed -= 1
            elif event.key == pygame.K_LEFT:
                car.angle_speed = -3
            elif event.key == pygame.K_RIGHT:
                car.angle_speed = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                car.angle_speed = 0
            elif event.key == pygame.K_RIGHT:
                car.angle_speed = 0
    clear_callback(screen, car.rect)
    screen.blit(BACKGROUND.image, (0, 0))
    car_group.update()
    car_group.draw(screen)


 
    pygame.display.update()
   

    if(pygame.sprite.groupcollide(car_group, background_group, False, False, pygame.sprite.collide_mask)):
        print("GAME OVER")
        break

pygame.quit()
