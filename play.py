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

##### irene_upgrade ######
money = int(input("Enter your money: "))

machine_criteria = { 
    "B": "Criteria - Cooking process speed up to 40s",
    "C": "Criteria - Cooking process speed up to 30s "}

def confirm_upgrade(machine_options):
    print("Criteria of the available upgrade options:")
    for machine in machine_options:
        print(f"Machine {machine}: {machine_criteria[machine]}")

    confirm = input("If sure, please type YES/NO: ").upper()
    if confirm == "YES":
        if len(machine_options) == 1:
            print(f"You have successfully upgraded your machine. Your current machine is {machine_options[0]}.")
        else:
            chosen_machine = input(f"Please type your choice ({'/'.join(machine_options)}): ").upper()
            if chosen_machine in machine_options:
                print(f"You have successfully upgraded your machine. Your current machine is {chosen_machine}.")
            else:
                print("Invalid answer!!!")
    elif confirm == "NO":
        print("Thank you! ^_^")
    else:
        print("Invalid answer!!!")

if 500 <= money <= 800:
    print("You can only upgrade to machine B. Do you want to upgrade your current machine to machine B?")
    confirm_upgrade(["B"])
elif 800 <= money <= 1500:
    print("You can choose to upgrade to machine B or C. Do you want to upgrade your current machine?")
    confirm_upgrade(["B", "C"])
elif 1500 <= money <= 2000:
    print("You can choose to upgrade to machine B, C, or D. Do you want to upgrade your current machine?")
    confirm_upgrade(["B", "C", "D"])
elif money > 2200:
    print("You can choose to upgrade to machine B, C, D, or E. Do you want to upgrade your current machine?")
    confirm_upgrade(["B", "C", "D", "E"])
else:
    print("Oops, you are unable to upgrade any machine since your money is not enough!")
##### end #####

#draw text display
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(str(text), True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

class MachineButton():
    def __init__(self, x, y, image_path, scale):
        self.image = pygame.image.load(image_path)
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect(topleft = (x, y)) #set button position

    def draw(self, screen):
        screen.blit(self.image, self.rect) #draw button on screen
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos) #check if the mouse position is inside the button's rect

class YesButton():
    def __init__(self, x, y, image_path, scale):
        self.image = pygame.image.load(image_path)
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect(topleft = (x, y)) #set button position

    def draw(self, screen):
        screen.blit(self.image, self.rect) #draw button on screen
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos) #check if the mouse position is inside the button's rect

class NoButton():
    def __init__(self, x, y, image_path, scale):
        self.image = pygame.image.load(image_path)
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect(topleft = (x, y)) #set button position

    def draw(self, screen):
        screen.blit(self.image, self.rect) #draw button on screen
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos) #check if the mouse position is inside the button's rect

class UpgradeButton():
    def __init__(self, x, y, image_path, scale):
        self.image = pygame.image.load(image_path)
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect(topleft = (x, y)) #set button position

    def draw(self, screen):
        screen.blit(self.image, self.rect) #draw button on screen
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos) #check if the mouse position is inside the button's rect

# Set up the main window
screen = pygame.display.set_mode((1400, 750))
pygame.display.set_caption("Pop-up Example")

#font
font = pygame.font.SysFont("freesansbold.ttf", 26)

#rectangle to display money
input_rect = pygame.Rect(740,125, 200, 33)
color = pygame.Color("slategray")

# Load the background image
background = pygame.image.load("picture/background with logo.png")
background = pygame.transform.scale(background, (1400, 750))

#load machine button images
machineA_img = pygame.image.load("picture/machineA.png").convert_alpha()
lock_machineB_img = pygame.image.load("picture/lockMachineB.png").convert_alpha()
lock_machineC_img = pygame.image.load("picture/lockMachineC.png").convert_alpha()

# Button setup
upgrade_btn = UpgradeButton(30, 460, "picture/upgrade-button.png",0.25)
default_machineA_button = MachineButton(600, 190, "picture/machineA.png", 0.6)
lock_machineB_button = MachineButton(780, 190, "picture/lockMachineB.png", 0.18)
lock_machineC_button = MachineButton(950,190, "picture/lockMachineC.png", 0.18)
yes_button =  YesButton(550,460, "picture/yesButton.png", 0.4)
no_button =  NoButton(680,463, "picture/noButton.png", 0.38)

#machine criteria
machine_criteria = { 
    "B": "Criteria - Cooking process speed up to 40s",
    "C": "Criteria - Cooking process speed up to 30s ",
}

# Pop-up 1st window size (big)
popup_width = 800
popup_height = 600
popup_rect = pygame.Rect(400, 90, popup_width, popup_height)

# Pop-up 2nd window size (medium)
popup2_width = 750
popup2_height = 300
popup2_rect = pygame.Rect(423, 380, popup2_width, popup2_height)

# Pop-up 3nd window size (small)
popup3_width = 720
popup3_height = 160
popup3_rect = pygame.Rect(438, 500, popup3_width, popup3_height)

# Main loop
show_popup = False
show_popup2 = False
show_popup3 = False
money = 3000

def check_money(money):
    if 600 <= money <= 1500:
        return ["B"]
    elif money > 1500:
        return ["B", "C"]
    else:
        return []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if upgrade_btn.is_clicked(event.pos): #check if the button is clicked
                show_popup = not show_popup
            elif lock_machineB_button.is_clicked(event.pos):
                show_popup2 = not show_popup2
            elif lock_machineC_button.is_clicked(event.pos):
                show_popup2 = not show_popup2
            elif yes_button.is_clicked(event.pos):
                show_popup3 = not show_popup3
            elif no_button.is_clicked(event.pos):
                show_popup3 = not show_popup3


    # Draw background
    screen.blit(background, (0, 0))

    # Draw button
    upgrade_btn.draw(screen)

    # Draw popup if button clicked
    if show_popup:
        pygame.draw.rect(screen, (255, 204, 229), popup_rect)
        pygame.draw.rect(screen, (148, 5, 100), popup_rect, 3)  # Popup border
        pygame.draw.rect(screen, color, input_rect)

        draw_text("Money: ", font, "black", screen, 700, 140)
        draw_text("Machine Types: ", font, "black", screen, 510, 250)
        draw_text("Default", font, "black", screen, 660, 315)
        draw_text("Machine B", font, "black", screen, 840, 315)
        draw_text("Machine C", font, "black", screen, 1010, 315)
        draw_text("Machine Features - B: Features - Cooking process speed up to 40s", font, "red", screen, 714, 340)
        draw_text("- C: Features - Cooking process speed up to 30s", font, "red", screen, 788, 360)

        default_machineA_button.draw(screen)
        lock_machineB_button.draw(screen)
        lock_machineC_button.draw(screen)

        if show_popup2:
            available_upgrades = check_money(money)
            pygame.draw.rect(screen, (222, 201, 235), popup2_rect)

            if "B" in available_upgrades:
                draw_text("Instructions: ", font, "black", screen, 500, 400)
                draw_text("- You are eligible to upgrade your machine to machine B. ", font, "black", screen, 670, 425)
                draw_text("- Do you wanna upgrade your machine now?", font, "black", screen, 617, 450)
                yes_button.draw(screen)
                no_button.draw(screen)
            if yes_button.is_clicked:
                pygame.draw.rect(screen,(201, 148, 220), popup3_rect)
                draw_text("You have successfully upgraded your machine!", font, "black", screen, 800, 580)
            elif no_button.draw.is_clicked:
                pygame.draw.rect(screen,(201, 148, 220), popup3_rect)
                draw_text("Thank you!", font, "black", screen, 800, 580)

            else:
                draw_text("You are eligible to upgrade your machine to machine B or C.", font, "black", screen, 500, 500)
                draw_text("Do you wanna upgrade your machine now?", font, "black", screen, 500, 550)
                yes_button.draw(screen)
                no_button.draw(screen)
                if yes_button.draw(screen):
                    pygame.draw.rect(screen,(201, 148, 220), popup3_rect)
                    draw_text("Machine B or C?", font, "black", screen, 800, 580)
                    b_button.draw(screen)
                    c_button.draw(screen)
                    if  b_button.draw(screen):
                        draw_text("You have successfully upgraded your machine to machine B!", font, "black", screen, 800, 580)
                    elif c_button.draw(screen):
                        draw_text("You have successfully upgraded your machine to machine C!", font, "black", screen, 800, 580)
                elif no_button.draw(screen):
                    pygame.draw.rect(screen,(201, 148, 220), popup3_rect)
                    draw_text("Thank you!", font, "black", screen, 800, 580) 
            
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
