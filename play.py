#start
import pygame
import sys
import os.path
import datetime
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

            f.close()   
        else:
            result_text = font.render(f"Welcome back to {restaurant_name} Restaurant!", True, white)
            result_text_rect = result_text.get_rect(center=(700, 750//2))
            screen.blit(result_text, result_text_rect)

            f.close()

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
                        count = list(user_text)
                        if list1[0] == '':
                            draw_text("Don't leave it blank, please try again", font, "red", screen, 700, 350)
                            pygame.display.flip()
                            pygame.time.wait(2000)
                            get_restaurant_name()
                        elif len(count) > int(24):
                            draw_text("Sorry, your name is too long,it is ", font, "red", screen, 700, 350)
                            draw_text("limited to 24 words, pls try again", font, "red", screen, 700, 450)
                            pygame.display.flip()
                            pygame.time.wait(2000)
                            get_restaurant_name()
                        else:
                            f = open("name.txt","x")
                            fdate = open("date.txt", "x")

                            f = open("name.txt", "a")
                            f.write(f'{user_text}')
                            f.close()

                            fdate = open("date.txt","a")
                            fdate.write(f'{other_StyleTime}')
                            fdate.close()
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

def show_logo():
    bg_img = pygame.image.load("logo.png").convert()
    screen.blit(bg_img, (0, 0))

    pygame.display.flip()
    pygame.time.wait(2000)


path = './name.txt'
check_file = os.path.isfile(path)
now = datetime.datetime.now()
other_StyleTime = now.strftime("%Y-%m-%d")

show_logo()

if check_file == True:
    f = open("name.txt", "r") 
    lines = f.readlines()
    show_name_from_file(lines[0].strip())
else:
    get_restaurant_name()
    

#load button images
menu_img = pygame.image.load("picture/menu.png").convert_alpha()

#food image
#Level 1(Malaysia)-Nasi Lemak-Roti Canai-Satay
nasilemak = pygame.image.load('picture/nasilemak.png')
nasilemak = pygame.transform.scale(nasilemak, (100,100))

roticanai = pygame.image.load('picture/roticanai.png')
roticanai = pygame.transform.scale(roticanai, (100,100))

satay = pygame.image.load('picture/satay.png')
satay = pygame.transform.scale(satay, (100,100))

#Level 2(Korea)-Corndog(Cheese/Origin)-Kimchi-Tokbokki
corndogcheese = pygame.image.load('picture/corndogcheese.png')
corndogcheese = pygame.transform.scale(corndogcheese, (100,100))

corndog = pygame.image.load('picture/corndog.png')
corndog = pygame.transform.scale(corndog, (100,100))

kimchi = pygame.image.load('picture/kimchi.png')
kimchi = pygame.transform.scale(kimchi, (100,100))

tokbokki = pygame.image.load('picture/tokbokki.png')
tokbokki = pygame.transform.scale(tokbokki, (100,100))

#Level 3(China)-Dumpling-Mooncake-DimSum
dumpling = pygame.image.load('picture/dumpling.png')
dumpling = pygame.transform.scale(dumpling, (100,100))

mooncake = pygame.image.load('picture/mooncake.png')
mooncake = pygame.transform.scale(mooncake, (100,100))

dimsum = pygame.image.load('picture/dimsum.png')
dimsum = pygame.transform.scale(dimsum, (100,100))

#nasilemaktelur_x = screen_width // 2-50   (position, last edit,exp)
#nasilemaktelur_y = screen_height // 2-50  (position, last edit,exp)

#font

#option box(put food's image init)

# Draw text display 
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(str(text), True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

class Button():
    def __init__(self, x, y, image_path, scale):
        self.image = pygame.image.load(image_path)
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect(topleft = (x, y)) 

    def draw(self, screen):
        screen.blit(self.image, self.rect) 
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos) 

#font
font = pygame.font.SysFont("freesansbold.ttf", 26)

# Rectangle to display money
input_rect = pygame.Rect(740,125, 200, 33)

# Rectangle to display machine types (prepare file)
inputMA_rect = pygame.Rect(350,310, 200, 33)
inputMB_rect = pygame.Rect(640,310, 200, 33)
inputMC_rect = pygame.Rect(930,310, 200, 33)

# Load the background image
background = pygame.image.load("mainBG.jpg")
background = pygame.transform.scale(background, (1400, 750))

# Load the small image
coin1_img =  pygame.image.load("coin.png")
coin1_img = pygame.transform.scale(coin1_img, (25, 25))
coin2_img =  pygame.image.load("coin.png")
coin2_img = pygame.transform.scale(coin2_img, (25, 25))
oriMachineA = pygame.image.load("ori-machineA.png")
oriMachineA = pygame.transform.scale(oriMachineA, (248, 238))
oriMachineB = pygame.image.load("ori-machineB.png")
oriMachineB = pygame.transform.scale(oriMachineB, (200, 187))
oriMachineC = pygame.image.load("ori-machineC.png")
oriMachineC = pygame.transform.scale(oriMachineC, (200, 187))

# All button setup in upgrading machine
upgrade_btn = Button(30, 460, "upgrade-button.png",0.8)
default_machineA_button = Button(600, 190, "machineA.png", 0.6)
lock_machineB_button = Button(780, 190, "lockMachineB.png", 0.18)
lock_machineC_button = Button(950,190, "lockMachineC.png", 0.18)
yes_button = Button (490, 480, "yesButton.png", 0.4)
no_button = Button (610, 482, "noButton.png", 0.38)
B_button = Button (490, 550, "alphabetB.png", 0.32)
C_button = Button (570, 550, "alphabetC.png", 0.32)
close_button = Button(1173, 70, "close_windowBtn.png", 0.1)
menuA_button = Button(300, 115, "menu.png", 0.13)
menuB_button = Button(619, 113, "menu.png", 0.13)
menuC_button = Button(917, 110, "menu.png", 0.13)

# Machine criteria
machine_criteria = { 
    "B": "Criteria - Cooking process speed up to 40s",
    "C": "Criteria - Cooking process speed up to 30s",
}

# Define the cost for each machine upgrade
upgrade_costs = {
    "B": 1800,  
    "C": 4000   
}

# Pop-up window sizes
popup_rect = pygame.Rect(400, 90, 800, 600)
popup2_rect = pygame.Rect(423, 380, 750, 280)

# Main loop in upgrading machine
show_popup = False
show_popup2 = False
selected_upgrade = None
selecting_machine = False
not_enough_money = False  
message_timer = 0  
money = 2500

def check_money(money):
    if 1800 <= money < 4000:
        return ["B"]
    elif money >= 4000:
        return ["B", "C"]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if close_button.is_clicked(event.pos):
                show_popup = False
                show_popup2 = False
            elif upgrade_btn.is_clicked(event.pos): 
                show_popup = True
            elif lock_machineB_button.is_clicked(event.pos) or lock_machineC_button.is_clicked(event.pos):
                show_popup2 = True
            elif yes_button.is_clicked(event.pos):
                if upgrade_costs["B"] <= money < upgrade_costs["C"]:
                    selected_upgrade = "B" 
                    message_timer = 180
                    money -= upgrade_costs["B"]
                    selecting_machine = False
                    show_popup = True
                    show_popup2 = True
                elif money >= upgrade_costs["C"]:
                    show_popup = True
                    show_popup2 = True
                    selecting_machine = True
                else:
                    not_enough_money = True  
                    show_popup2 = True
                    message_timer = 180
            elif no_button.is_clicked(event.pos):
                show_popup2 = False  

            elif B_button.is_clicked(event.pos):
                if money >= upgrade_costs["B"]:
                    selected_upgrade = "B"
                    message_timer = 180
                    money -= upgrade_costs["B"]
                    selected_upgrade = False 
                    show_popup = True
                    show_popup2 = True
                else:
                    not_enough_money = True
                    message_timer = 120  

            elif C_button.is_clicked(event.pos):
                if money >= upgrade_costs["C"]:
                    selected_upgrade = "C"
                    message_timer = 180
                    money -= upgrade_costs["C"]
                    selecting_machine = False 
                    show_popup = True
                    show_popup2 = True
                else:
                    not_enough_money = True
                    message_timer = 180  
            elif menuA_button.is_clicked(event.pos) or menuB_button.is_clicked(event.pos) or menuC_button.is_clicked(event.pos):
                show_popup = True
    # Draw background
    screen.blit(background, (0, 0))
    screen.blit(oriMachineA,(330,100))
    screen.blit(oriMachineB,(640,120))
    screen.blit(oriMachineC,(930,120))

    pygame.draw.rect(screen, (7,0,63), inputMA_rect)
    draw_text("Default- Machine A", font, "white", screen, 450, 330)
    
    pygame.draw.rect(screen, (7,0,63), inputMB_rect)
    draw_text("Machine B", font, "white", screen, 740, 330)

    pygame.draw.rect(screen, (7,0,63), inputMC_rect)
    draw_text("Machine C", font, "white", screen, 1030, 330)

    upgrade_btn.draw(screen)
    menuA_button.draw(screen)
    menuB_button.draw(screen)
    menuC_button.draw(screen)

    if show_popup:
        pygame.draw.rect(screen, (255, 201, 254), popup_rect)
        pygame.draw.rect(screen, (148, 5, 100), popup_rect, 5)  # Popup border
        screen.blit(coin1_img,(800, 302))
        screen.blit(coin1_img,(973, 303))
        pygame.draw.rect(screen, (162, 164, 164), input_rect)

        draw_text("Money: ", font, "black", screen, 700, 140)
        draw_text(money, font, "navyblue", screen, 836, 142)
        draw_text("Machine Types: ", font, "black", screen, 510, 250)
        draw_text("1800", font, "black", screen, 847, 315)
        draw_text("4000", font, "black", screen, 1020, 315)
        draw_text("Default", font, "black", screen, 660, 315)
        draw_text("Machine B", font, "black", screen, 840, 337)
        draw_text("Machine C", font, "black", screen, 1013, 336)
        draw_text("Machine Features - B: Cooking process speed up to 40s", font, "black", screen, 714, 359)
        draw_text("- C: Cooking process speed up to 30s", font, "black", screen, 788, 380)

        default_machineA_button.draw(screen)
        lock_machineB_button.draw(screen)
        lock_machineC_button.draw(screen)
        close_button.draw(screen)
    
    if show_popup2:
        pygame.draw.rect(screen, (243, 191, 215), popup2_rect)
        draw_text("INSTRUCTIONS: ", font, "black", screen, 520, 440)
        draw_text("1. Do you want to upgrade your machine?", font, "black", screen, 614, 467)
        yes_button.draw(screen)
        no_button.draw(screen)

    if selecting_machine:
        draw_text("2. Select your machine:", font, "black", screen, 543, 538)
        B_button.draw(screen)
        C_button.draw(screen)

    if selected_upgrade:
        draw_text(f"Machine upgraded to {selected_upgrade}!", font, "navyblue", screen, 800, 630)
        message_timer -= 1  
        if message_timer == 0:
            selected_upgrade = False
    
    if not_enough_money:
        draw_text("You do not have enough money!", font, "red", screen, 800, 630)
        message_timer -= 1  
        if message_timer == 0:
            not_enough_money = False 
            selecting_machine = False
        
    pygame.display.update()

pygame.quit()
sys.exit()
