#start

import pygame
import sys

pygame.init()

screen_height=750
screen_width=1400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Menu Button')

white = (255,255,255)
black = (0,0,0)
grey = (200,200,200)

#load button images
menu_img = pygame.image.load('menu.png').convert_alpha()


#food image
#Level 1(Malaysia)-Nasi Lemak(telur/ayam)-Roti Canai-Ice Syrup
nasilemaktelur_TA = pygame.image.load('Mini IT Project/project picture/nl_telur.png')
nasilemaktelur_TA = pygame.transform.scale(nasilemaktelur_TA, (100,100))

nasilemakayam_TA = pygame.image.load('Mini IT Project/project picture/nl_ayam.png')
nasilemakayam_TA = pygame.transform.scale(nasilemakayam_TA, (100,100))

roticanai_TA = pygame.image.load('Mini IT Project/project picture/rc_bungkus.png')
roticanai_TA = pygame.transform.scale(roticanai_TA, (100,100))

icesyrup_TA = pygame.image.load('Mini IT Project/project picture/syrup ice bungkus.png')
icesyrup_TA = pygame.transform.scale(icesyrup_TA, (100,100))

#Level 2(Korea)-Corndog(Cheese/Origin)-Kimchi-Tokbokki
corndogcheese_TA = pygame.image.load('')
corndogcheese_TA = pygame.transform.scale(corndogcheese_TA, (100,100))

corndogorigin_TA = pygame.image.load('')
corndogorigin_TA = pygame.transform.scale(corndogorigin_TA, (100,100))

kimchi_TA = pygame.image.load('')
kimchi_TA = pygame.transform.scale(kimchi_TA, (100,100))

tokbokki_TA = pygame.image.load('')
tokbokki_TA = pygame.transform.scale(tokbokki_TA, (100,100))

#Level 3(China)-Dumpling-Mooncake-DimSum
dumpling_TA = pygame.image.load('')
dumpling_TA = pygame.transform.scale(dumpling_TA, (100,100))

mooncake_TA = pygame.image.load('')
mooncake_TA = pygame.transform.scale(mooncake_TA, (100,100))

dimsum_TA = pygame.image.load('')
dimsum_TA = pygame.transform.scale(dimsum_TA, (100,100))

#nasilemaktelur_x = screen_width // 2-50   (position, last edit,exp)
#nasilemaktelur_y = screen_height // 2-50  (position, last edit,exp)

#font

#option box(put food's image init)

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