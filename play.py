#start
import pygame
import sys
import os.path
from pygame import mixer

pygame.init()

mixer.music.load('music.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.5)

screen_height=750
screen_width=1400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('World Restaurant')

white = (255,255,255)
black = (0,0,0)
grey = (200,200,200)
red = (255, 0, 0)

#first page
font = pygame.font.Font('freesansbold.ttf', 50)
base_font = pygame.font.Font(None, 55)

input_rect = pygame.Rect(550, 350, 250, 50)
color_active = pygame.Color('antiquewhite4')
color_passive = pygame.Color('gray5')
color_fill = pygame.Color('white')
color = color_passive

clock = pygame.time.Clock()

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(str(text), True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def show_name_from_file(restaurant_name):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        bg_img = pygame.image.load("bcg.png").convert()
        screen.blit(bg_img, (0, 0))

        result_text = str(lines[0])
        result_text1 = str(lines[0])
        count = list(result_text)
        if len(count) > int(18):
            result_text = font.render(f"Welcome back to ", True, white)
            result_text_rect = result_text.get_rect(center=(700, 280))
            screen.blit(result_text, result_text_rect)

            result_text1 = font.render(f"{restaurant_name} Restaurant!", True, white)
            result_text_rect1 = result_text1.get_rect(center=(700, 380))
            screen.blit(result_text1, result_text_rect1)          
        else:
            result_text = font.render(f"Welcome back to {restaurant_name} Restaurant!", True, white)
            result_text_rect = result_text.get_rect(center=(700, 750//2))
            screen.blit(result_text, result_text_rect)

        pygame.display.flip()
        clock.tick(60)

def show_restaurant_name(restaurant_name):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        bg_img = pygame.image.load("bcg.png").convert()
        screen.blit(bg_img, (0, 0))

        count = list(restaurant_name)

        if len(count) > int(25):
            result_text = font.render(f"Welcome to", True, white)
            result_text_rect = result_text.get_rect(center=(700, 280))
            screen.blit(result_text, result_text_rect)

            result_text1 = font.render(f"{restaurant_name} Restaurant!", True, white)
            result_text_rect1 = result_text1.get_rect(center=(700, 380))
            screen.blit(result_text1, result_text_rect1)
        else:
            result_text = font.render(f"Welcome to {restaurant_name} Restaurant!", True, white)
            result_text_rect = result_text.get_rect(center=(700, 750//2))
            screen.blit(result_text, result_text_rect)

        pygame.display.flip()
        clock.tick(60)

def get_restaurant_name():
    text = font.render("What's name of the restaurant?: ", True, white)
    textRect = text.get_rect()
    textRect.center = (700, 150)
    user_text = ''
    active = False

    while True:
        bg_img = pygame.image.load("bcg.png").convert()
        screen.blit(bg_img, (0, 0))

        screen.blit(text, textRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        list1=[]
                        list1.append(user_text)
                        if list1[0] == '':
                            draw_text("Don't leave it blank, please try again", font, "red", screen, 700, 350)
                            pygame.display.flip()
                            pygame.time.wait(2000)
                            get_restaurant_name()
                        else:
                            f = open("name.txt", "a")
                            f.write(f'{user_text}')
                            f.close()
                            show_restaurant_name(user_text)
                    else:
                        if event.unicode.isalnum():
                            user_text += event.unicode

        if active:
            color = color_active
        else:
            color = color_passive

        pygame.draw.rect(screen, color_fill, input_rect)
        pygame.draw.rect(screen, color, input_rect, 2)

        text_surface = base_font.render(user_text, True, (0, 0, 0))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(250, text_surface.get_width() + 10)

        pygame.display.flip()
        clock.tick(60)

path = './name.txt'
check_file = os.path.isfile(path)

if check_file == True:
    f = open("name.txt", "r") 
    lines = f.readlines()
    show_name_from_file(lines[0].strip())
else:
    f = open("name.txt","x")
    get_restaurant_name()

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