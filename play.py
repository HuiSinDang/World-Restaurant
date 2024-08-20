#start

import pygame
import sys

pygame.init()

screen_height=750
screen_width=1400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Menu Button')

#load button images
menu_img = pygame.image.load('menu.png').convert_alpha()

#button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] ==0:
            self.clicked = False

    #draw button on the screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        return action

#create button instances
menu_button = Button(100, 200, menu_img, 0.8)

run = True
while run:

    screen.fill((202, 228, 241))

    if menu_button.draw():
        print('MENU')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
sys.exit()