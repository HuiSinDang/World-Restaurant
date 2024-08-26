#start
import pygame
import sys
import time
import os.path
import datetime
from pygame import mixer

pygame.init()

mixer.music.load('./picture/music.mp3')
mixer.music.play(-1)
mixer.music.set_volume(1)
click_sfx = pygame.mixer.Sound("./picture/click.wav")

screen_height=750
screen_width=1400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('World Restaurant')
screen.set_alpha(None)

screen_rect = screen.get_rect()
screen_rect.x = 200
screen_rect.y = 150
surface = pygame.Surface((900,500),pygame.SRCALPHA)
pygame.draw.rect(surface,(231, 175, 195  ,200),surface.get_rect(),0)

white = (255,255,255)
black = (0,0,0)
grey = (200,200,200)
red = (255, 0, 0)

#login
font = pygame.font.Font('freesansbold.ttf', 50)
base_font = pygame.font.Font(None, 55)
main_font = pygame.font.SysFont("cambria", 45)

input_rect = pygame.Rect(550, 350, 250, 50)
color_active = pygame.Color('antiquewhite4')
color_passive = pygame.Color('gray5')
color_fill = pygame.Color('white')
color = color_passive

clock = pygame.time.Clock()

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

# Rectangle to display money
inputmoney_rect = pygame.Rect(740,125, 200, 33)

# Rectangle to display machine types (prepare file)
inputMA_rect = pygame.Rect(350,310, 200, 33)
inputMB_rect = pygame.Rect(640,310, 200, 33)
inputMC_rect = pygame.Rect(930,310, 200, 33)

popup_rect = pygame.Rect(400, 90, 800, 600)
popup2_rect = pygame.Rect(423, 380, 750, 280)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(str(text), True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

class Button():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if self.rect.collidepoint(position):
            click_sfx.play()
            return True
        return False

# Initialize the button
button_surface = pygame.image.load("./picture/close_windowBtn.png")
button_surface = pygame.transform.scale(button_surface, (75, 75))
button = Button(button_surface, 1100, 150, "")

resetbutton_surface = pygame.image.load("./picture/reset_btn.png")
resetbutton_surface = pygame.transform.scale(resetbutton_surface, (250, 250))
resetbutton = Button(resetbutton_surface, 600, 575, "Reset Name")

backbutton_surface = pygame.image.load("./picture/back_btn.png")
backbutton_surfacebutton_surface = pygame.transform.scale(backbutton_surface, (150, 150))
backbutton = Button(backbutton_surface, 75, 75, "")

profilebutton_surface = pygame.image.load("./picture/profile_btn.png")
profilebutton_surfacebutton_surface = pygame.transform.scale(profilebutton_surface, (100, 100))
profilebutton = Button(profilebutton_surface, 75, 75, "")

upgrade_btn = pygame.image.load("./pictureupgrade-button.png")
upgrade_btn = pygame.transform.scale(upgrade_btn, (110, 110))
upgrade_btn= Button(upgrade_btn, 76, 430, "")

default_machineA_button = pygame.image.load("./picture/ori-machineA.png")
default_machineA_button = pygame.transform.scale(default_machineA_button, (210, 240))
default_machineA_button = Button(default_machineA_button, 420, 260, "")

lock_machineB_button = pygame.image.load("./picture/ori-MachineB.png")
lock_machineB_button = pygame.transform.scale(lock_machineB_button, (210, 180))
lock_machineB_button = Button(lock_machineB_button, 740, 255, "")

lock_machineC_button = pygame.image.load("./picture/ori-MachineC.png")
lock_machineC_button = pygame.transform.scale(lock_machineC_button, (210, 180))
lock_machineC_button = Button(lock_machineC_button, 1050, 255, "")

yes_button = pygame.image.load("./picture/yesButton.png")
yes_button = pygame.transform.scale(yes_button, (250, 250))
yes_button = Button(yes_button, 550,460, "")

no_button = pygame.image.load("./picture/noButton.png")
no_button = pygame.transform.scale(no_button, (250, 250))
no_button = Button(no_button, 680,463, "")

close_button = pygame.image.load("./picture/close_windowBtn.png")
close_button = pygame.transform.scale(close_button, (75, 75))
close_button = Button(close_button, 1173, 70, "")

menu_button = pygame.image.load("./picture/menu.png")
menu_button = pygame.transform.scale(menu_button, (110,100))
menu_button = Button(menu_button, 76, 250, "")

setting_button = pygame.image.load("./picture/setting.png")
setting_button = pygame.transform.scale(setting_button, (120, 120))
setting_button = Button(setting_button, 73, 620, "")

# Main loop
show_popup = False
show_popup2 = False
show_popup3 = False
show_popup4 = False
selected_upgrade = None
selecting_machine = False
not_enough_money = False  # indicate not enough money
message_timer = 0  # Timer to show messages temporarily
money = 4000
unlocked_machine = set() # Set to track unlocked machines


def rename():
    text = font.render("What's name of your restaurant?: ", True, white)
    textRect = text.get_rect()
    textRect.center = (700, 150)
    user_text = ''
    active = False

    while True:
        bg_img = pygame.image.load("./picture/bcg.png").convert()
        screen.blit(bg_img, (0, 0))

        screen.blit(text, textRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if backbutton.checkForInput(pygame.mouse.get_pos()):
                    profile()
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
                            rename()
                        elif len(count) > int(24):
                            draw_text("Sorry, your name is too long,it is ", font, "red", screen, 700, 350)
                            draw_text("limited to 24 words, pls try again", font, "red", screen, 700, 450)
                            pygame.display.flip()
                            pygame.time.wait(2000)
                            rename()
                        else:
                            f = open("name.txt","w")
                            f.write(f'{user_text}')
                            f.close()
                            profile()
                    else:
                        if event.unicode.isalnum():
                            user_text += event.unicode

        if active:
            color = color_active
        else:
            color = color_passive

        pygame.draw.rect(screen, color_fill, input_rect)
        pygame.draw.rect(screen, color, input_rect, 2)

        text_surface = base_font.render(user_text, True, black)
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(250, text_surface.get_width() + 10)

        backbutton.update()
        pygame.display.flip()
        clock.tick(60)


def profile():
    while True:
        bg_img = pygame.image.load("./picture/lobby.jpg").convert()
        screen.blit(bg_img, (0, 0))
        screen.blit(surface,screen_rect)

        draw_text("Profile", font, "black", screen, 650, 200)

        f = open("name.txt","r")
        lines = f.readlines()
        name = lines[0].strip()
        count = list(name)

        fdate = open("date.txt","r")
        firstdate = fdate.readlines()
        date = firstdate[0].strip()

        path = './totalearned.txt'
        check_file = os.path.isfile(path)

        if len(count) > int(14):
            draw_text(f"Name: {name} ", font, "black", screen, 650, 300)
            draw_text(f"Restaurant", font, "black", screen, 650, 350)
            draw_text(f"Opened in: {date}", font, "black",screen,650, 425)
            if check_file :
                y= open("totalearned.txt", 'r')
                totalmoney = [int(i) for i in y.read().split("\n")]
                y.close()
                total = sum(totalmoney)
                draw_text(f"Total earned money: $ {total}", font, "black",screen,650, 500)
            else:
                draw_text(f"Total earned money: $ 0", font, "black",screen,650, 500)
        else:
            draw_text(f"Name: {name} Restaurant", font, "black", screen, 650, 300)
            draw_text(f"Opened in: {date}", font, "black",screen,650, 400)
            if check_file :
                y= open("totalearned.txt", 'r')
                totalmoney = [int(i) for i in y.read().split("\n")]
                y.close()
                total = sum(totalmoney)
                draw_text(f"Total earned money: $ {total}", font, "black",screen,650, 500)
            else:
                draw_text(f"Total earned money: $ 0", font, "black",screen,650, 500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.checkForInput(pygame.mouse.get_pos()):
                    main()
                if resetbutton.checkForInput(pygame.mouse.get_pos()):
                    rename()
                if profilebutton.checkForInput(pygame.mouse.get_pos()):
                    profile()

        button.update()
        resetbutton.update()
        profilebutton.update()
        upgrade_btn.update()

        pygame.display.flip()
    
def main():

    while True:
        bg_img = pygame.image.load("./picture/lobby.jpg").convert()
        screen.blit(bg_img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if profilebutton.checkForInput(pygame.mouse.get_pos()):
                    profile()

        profilebutton.update()
        upgrade_btn.update()
        default_machineA_button.update()
        lock_machineB_button.update()
        lock_machineC_button.update()
        menu_button.update()
        menuB_button.update()
        menuC_button.update()

        pygame.display.flip()


def show_name_from_file(restaurant_name):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        bg_img = pygame.image.load("./picture/bcg.png").convert()
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
        pygame.time.wait(2000)
        main()        
        clock.tick(60)

def show_restaurant_name(restaurant_name):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        bg_img = pygame.image.load("./picture/bcg.png").convert()
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
        pygame.time.wait(2000)
        main()
        clock.tick(60)

def get_restaurant_name():
    text = font.render("What's name of your restaurant?: ", True, white)
    textRect = text.get_rect()
    textRect.center = (700, 150)
    user_text = ''
    active = False

    while True:
        bg_img = pygame.image.load("./picture/bcg.png").convert()
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
    bg_img = pygame.image.load("./picture/logo.png").convert()
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
menu_img = pygame.image.load("./picture/menu.png").convert_alpha()

#food image
#Level 1(Malaysia)-Nasi Lemak-Roti Canai-Satay
nasilemak = pygame.image.load('./picture/nasilemak.png')
nasilemak = pygame.transform.scale(nasilemak, (100,100))

roticanai = pygame.image.load('./picture/roticanai.png')
roticanai = pygame.transform.scale(roticanai, (100,100))

satay = pygame.image.load('./picture/satay.png')
satay = pygame.transform.scale(satay, (100,100))

#Level 2(Korea)-Corndog(Cheese/Origin)-Kimchi-Tokbokki
corndogcheese = pygame.image.load('./picture/corndogcheese.png')
corndogcheese = pygame.transform.scale(corndogcheese, (100,100))

corndog = pygame.image.load('./picture/corndog.png')
corndog = pygame.transform.scale(corndog, (100,100))

kimchi = pygame.image.load('./picture/kimchi.png')
kimchi = pygame.transform.scale(kimchi, (100,100))

tokbokki = pygame.image.load('./picture/tokbokki.png')
tokbokki = pygame.transform.scale(tokbokki, (100,100))

#Level 3(China)-Dumpling-Mooncake-DimSum
dumpling = pygame.image.load('./picture/dumpling.png')
dumpling = pygame.transform.scale(dumpling, (100,100))

mooncake = pygame.image.load('./picture/mooncake.png')
mooncake = pygame.transform.scale(mooncake, (100,100))

dimsum = pygame.image.load('./picture/dimsum.png')
dimsum = pygame.transform.scale(dimsum, (100,100))

#noticeboard(intro)
noticeboard = pygame.image.load('noticeboard.png')
noticeboard = pygame.transform.scale(noticeboard, (1400,800))

closebutton = pygame.image.load('closebutton.png')
closebutton = pygame.transform.scale(closebutton, (1000,700))

nextbutton = pygame.image.load('nextbutton.png')
nextbutton = pygame.transform.scale(nextbutton, (1000,700))

#logo fade effect
logo = pygame.image.load('./picture/background with logo.png')
logo = pygame.transform.scale(logo, (screen_width,screen_height))
start_time = time.time()
fade_duration = 3

#money
font2 = pygame.font.Font('jugnle.ttf',50)
money_amount = 0
max_display_money = 1000000

def money_bar():
    money_text = font2.render(f"{money_amount}", True, black)
    text_rect = money_text.get_rect(center=(1250,67))
    screen.blit(money_text, text_rect)

#happy hour
order_completed = 0
hhactive = False
hhtime = 30
hh_start_time = None

def update_happy_hour_status():
    global hhactive,order_completed,hh_start_time
    if order_completed >= 5:
        hhactive = True
        hh_start_time = time.time()
        order_completed = order_completed % 5
    elif hhactive and (time.time() - hh_start_time) >= hhtime:
        hhactive = False

def happyhour_bar(happyhour):
    update_happy_hour_status()
    if hhactive:
        hhtext = font2.render("Happy Hour Active!", True, black)
    else:
        hhtext = font2.render("Happy Hour", True, black)

    remaining_order = (order_completed % 5 - 5) % 5
    hhtext2 = font2.render(f"{remaining_order} /5", True, black)
    text_rect = hhtext.get_rect(center=(670,60))
    text_rect2 = hhtext2.get_rect(center=(670,100))
    screen.blit(hhtext,text_rect)
    screen.blit(hhtext2,text_rect2)

def hhprofit(origin_profit):
    if hhactive:
        return origin_profit * 2
    return origin_profit

#intro
noticeboard_rect = noticeboard.get_rect(center=(700,400))
closebutton_rect = closebutton.get_rect(topright=(1225,43))
nextbutton_rect = nextbutton.get_rect(bottomright=(1255,795))
notice_font = pygame.font.Font('jugnle.ttf',20)
noticetext1 = "Welcome to World Restaurant!\nIntroduction of the game..."
noticetext2 = "Many tutorial...\nBla bla bla..."
intropage = 1
mouse_pressed_last_frame = False

def render_introtext(text,font,color,center):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        rendered_line = notice_font.render(line,True,black)
        line_rect = rendered_line.get_rect(center=(center[0],center[1] - 20 + i * 40))
        screen.blit(rendered_line,line_rect)

def intropage1():
    screen.blit(noticeboard, noticeboard_rect)
    render_introtext(noticetext1,notice_font,black,(noticeboard_rect.centerx-50,noticeboard_rect.centery-250))
    screen.blit(nextbutton,nextbutton_rect)

def intropage2():
    screen.blit(noticeboard,noticeboard_rect)
    render_introtext(noticetext2,notice_font,black,(noticeboard_rect.centerx-50,noticeboard_rect.centery-250))
    screen.blit(closebutton,closebutton_rect)


def intropage_click(page,mouse_pressed_last_frame):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]
    if page == 1 and nextbutton_rect.collidepoint(mouse_pos):
        if mouse_pressed_last_frame and not mouse_pressed:
            return 2,mouse_pressed
    elif page == 2 and closebutton_rect.collidepoint(mouse_pos):
        if mouse_pressed_last_frame and not mouse_pressed:
            return 0,mouse_pressed
    return page,mouse_pressed

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

font = pygame.font.SysFont("freesansbold.ttf", 26)


# Rectangle to display money
input_rect = pygame.Rect(740,125, 200, 33)



# Rectangle to display machine types (prepare file)
inputMA_rect = pygame.Rect(350,310, 200, 33)
inputMB_rect = pygame.Rect(640,310, 200, 33)
inputMC_rect = pygame.Rect(930,310, 200, 33)

# Load the background image
background = pygame.image.load("./picture/mainBG.jpg")
background = pygame.image.load("picture/background with ./picture/logo.png")
background = pygame.transform.scale(background, (1400, 750))

#load machine button images
machineA_img = pygame.image.load("./picture/machineA.png").convert_alpha()
lock_machineB_img = pygame.image.load("./picture/lockMachineB.png").convert_alpha()
lock_machineC_img = pygame.image.load("./picture/lockMachineC.png").convert_alpha()

#machine criteria
background = pygame.image.load("mainBG.jpg")
background = pygame.transform.scale(background, (1400, 750))

# Load the small image
coin1_img =  pygame.image.load("./picture/coin.png")
coin1_img = pygame.transform.scale(coin1_img, (25, 25))
coin2_img =  pygame.image.load("./picture/coin.png")
coin2_img = pygame.transform.scale(coin2_img, (25, 25))
oriMachineA = pygame.image.load("./picture/ori-machineA.png")
oriMachineA = pygame.transform.scale(oriMachineA, (248, 238))
oriMachineB = pygame.image.load("./picture/ori-machineB.png")
oriMachineB = pygame.transform.scale(oriMachineB, (200, 187))
oriMachineC = pygame.image.load("./picture/ori-machineC.png")
oriMachineC = pygame.transform.scale(oriMachineC, (200, 187))

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

# Main loop
show_popup = False
show_popup2 = False
show_popup3 = False
show_popup4 = False
selected_upgrade = None
selecting_machine = False
not_enough_money = False  # indicate not enough money
message_timer = 0  # Timer to show messages temporarily
money = 4000
unlocked_machine = set() # Set to track unlocked machines

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
                show_popup3 = False
                show_popup4 = False

            elif upgrade_btn.is_clicked(event.pos): 
                show_popup = True

            elif lock_machineB_button.is_clicked(event.pos) or lock_machineC_button.is_clicked(event.pos):
                show_popup2 = True
            
            if yes_button.is_clicked(event.pos):
                selecting_machine = True
                show_popup2 = True
                
            elif no_button.is_clicked(event.pos):
                show_popup2 = False   
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

            elif selecting_machine:
                if B_button.is_clicked(event.pos):
                    if "B" in unlocked_machine:
                        selected_upgrade = "B"
                        message_timer = 180
                    elif money >= upgrade_costs["B"]:
                        money -= upgrade_costs["B"]
                        unlocked_machine.add("B")
                        selected_upgrade = "B"
                        message_timer = 180
                    else:
                        not_enough_money = True
                        message_timer = 180

                elif C_button.is_clicked(event.pos):
                    if money < upgrade_costs["C"]:
                        not_enough_money = True
                        message_timer = 180
                    else:
                        if "C" not in unlocked_machine:
                            money -= upgrade_costs["C"]
                            unlocked_machine.add("C")
                            selected_upgrade = "C"
                            message_timer = 180
                
                elif menu_button.is_clicked(event.pos):
                    show_popup3 = True
    elapsed_time = time.time() - start_time
    
    if elapsed_time < fade_duration:
        fade_alpha = int(255 * (1 - (elapsed_time / fade_duration)))
        logo.set_alpha(fade_alpha)
        screen.fill(white)
        screen.blit(logo, (0,0))

    # Draw background
    else:
        if intropage == 1:
            intropage1()
        elif intropage == 2:
            intropage2()
        intropage,mouse_pressed_last_frame = intropage_click(intropage,mouse_pressed_last_frame)
        if intropage == 0:
            money_bar()
            happyhour_bar()
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
    menu_button.draw(screen)
    menuB_button.draw(screen)
    menuC_button.draw(screen)

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
    
    if show_popup3:
        pygame.draw.rect(screen, (255, 201, 254), popup3_rect)
        pygame.draw.rect(screen, (148, 5, 100), popup3_rect, 5)  # Popup border
        draw_text("Foods:", font, "black", screen, 465, 150)
        close_button.draw(screen)

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
