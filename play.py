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
upgrade_font = pygame.font.Font('freesansbold.ttf', 20)
font2 = pygame.font.Font('./picture/jugnle.ttf', 50)

base_font = pygame.font.Font(None, 55)
main_font = pygame.font.SysFont("cambria", 45)

input_rect = pygame.Rect(550, 350, 250, 50)
color_active = pygame.Color('antiquewhite4')
color_passive = pygame.Color('gray5')
color_fill = pygame.Color('white')
color = color_passive

# select food to prepare
food_selection_font = pygame.font.SysFont("Comic Sans MS", 23, bold=True)
food_title_font = pygame.font.SysFont("Comic Sans MS", 18, bold=True)
color_pic = (222, 220, 250)

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
popup_rect = pygame.Rect(400, 120, 800, 600)
popup2_rect = pygame.Rect(423, 430, 750, 230)
food_selection1_rect = pygame.Rect(400, 120, 800, 600)

# Load the small image
coin1_img =  pygame.image.load("./picture/coin.png")
coin1_img = pygame.transform.scale(coin1_img, (25, 25))

coin2_img =  pygame.image.load("./picture/coin.png")
coin2_img = pygame.transform.scale(coin2_img, (25, 25))

background = pygame.image.load("./picture/lobby.jpg")
background = pygame.transform.scale(background, (1400, 750))

corndog_img = pygame.image.load("corndog.png")
corndog_img = pygame.transform.scale(corndog_img, (100, 127))

tokbokki_img = pygame.image.load("tokbokki.png")
tokbokki_img = pygame.transform.scale(tokbokki_img, (100, 127))

corndogcheese_img = pygame.image.load("corndogcheese.png")
corndogcheese_img = pygame.transform.scale(corndogcheese_img, (100, 127))

roticanai_img = pygame.image.load("roticanai.png")
roticanai_img = pygame.transform.scale(roticanai_img, (100, 127))

dumpling_img = pygame.image.load("dumpling.png")
dumpling_img = pygame.transform.scale(dumpling_img, (100, 127))

food_lists =[
    {
    "image": tokbokki_img,
    "name": "Tokbokki",
    "price": "RM10.00",
    },

    {
    "image": corndogcheese_img,
    "name": "Cheese Corndog",
    "price": "RM10.00",
    },

    {
    "image": corndog_img,
    "name": "Original Corndog",
    "price": "RM8.00",
    },

    {
    "image": roticanai_img,
    "name": "Roti Canai",
    "price": "RM1.50",
    },

    {
    "image": dumpling_img,
    "name": "Dumpling",
    "price": "RM6.00",
    }
]

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

upgrade_btn = pygame.image.load("./picture/upgrade-shop.png")
upgrade_btn = pygame.transform.scale(upgrade_btn, (110, 110))
upgrade_btn= Button(upgrade_btn, 76, 430, "")

default_machineA_button = pygame.image.load("./picture/machineA.png")
default_machineA_button = pygame.transform.scale(default_machineA_button, (160, 160))
default_machineA_button = Button(default_machineA_button, 710, 260, "")

machineB_button = pygame.image.load("./picture/machineB.png")
machineB_button = pygame.transform.scale(machineB_button, (160, 150))
machineB_button = Button(machineB_button, 890, 255, "")

machineC_button = pygame.image.load("./picture/machineC.png")
machineC_button = pygame.transform.scale(machineC_button, (160, 150))
machineC_button = Button(machineC_button, 1060, 255, "")

ori_machineA_button = pygame.image.load("./picture/ori-machineA.png")
ori_machineA_button = pygame.transform.scale(ori_machineA_button, (210, 240))
ori_machineA_button = Button(ori_machineA_button, 420, 260, "")

ori_machineB_button = pygame.image.load("./picture/ori-machineB.png")
ori_machineB_button = pygame.transform.scale(ori_machineB_button, (210, 180))
ori_machineB_button = Button(ori_machineB_button, 740, 255, "")

ori_machineC_button = pygame.image.load("./picture/ori-machineC.png")
ori_machineC_button = pygame.transform.scale(ori_machineC_button, (210, 180))
ori_machineC_button = Button(ori_machineC_button, 1050, 255, "")

yesC_button = pygame.image.load("./picture/yesButton.png")
yesC_button = pygame.transform.scale(yesC_button, (90, 43))
yesC_button = Button(yesC_button, 550,515, "")

noC_button = pygame.image.load("./picture/noButton.png")
noC_button = pygame.transform.scale(noC_button, (85, 41))
noC_button = Button(noC_button, 680,516, "")

yesB_button = pygame.image.load("./picture/yesButton.png")
yesB_button = pygame.transform.scale(yesB_button, (90, 43))
yesB_button = Button(yesB_button, 550,515, "")

noB_button = pygame.image.load("./picture/noButton.png")
noB_button = pygame.transform.scale(noB_button, (85, 41))
noB_button = Button(noB_button, 680,516, "")

close_button = pygame.image.load("./picture/close_windowBtn.png")
close_button = pygame.transform.scale(close_button, (60, 60))
close_button = Button(close_button, 1190, 130, "")

menu_button = pygame.image.load("./picture/menu.png")
menu_button = pygame.transform.scale(menu_button, (110,100))
menu_button = Button(menu_button, 76, 250, "")

setting_button = pygame.image.load("./picture/setting.png")
setting_button = pygame.transform.scale(setting_button, (120, 120))
setting_button = Button(setting_button, 73, 620, "")

next_btn = pygame.image.load("nextbutton.png")
next_btn = pygame.transform.scale(next_btn, (50, 60))
next_btn = Button(next_btn, 1138, 669, "")

back_btn = pygame.image.load("back_btn.png")
back_btn = pygame.transform.scale(back_btn, (60, 70))
back_btn = Button(back_btn, 460, 665, "")

selectDM_btn = pygame.image.load("select-default.png")
selectDM_btn = pygame.transform.scale(selectDM_btn, (600,100))
selectDM_btn = Button(selectDM_btn, 800, 340, "")

selectMB_btn = pygame.image.load("select-mb.png")
selectMB_btn = pygame.transform.scale(selectMB_btn, (600,90))
selectMB_btn = Button(selectMB_btn, 800, 450, "")

selectMC_btn = pygame.image.load("select-mc.png")
selectMC_btn = pygame.transform.scale(selectMC_btn, (600,90))
selectMC_btn = Button(selectMC_btn, 800, 560, "")

# Main loop
show_popup = False
show_popup2B = False
show_popup2C = False
selected_upgradeB = None
selected_upgradeC = None
current_upgrade = None
already_upgrade = False
not_enough_money = False 
message_timer = 0  
money = 2000
unlocked_machine = set() 
remind_unlock = False

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
                if event.key == pygame.K_ESCAPE:
                    profile()

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
                            f = open("./picture/name.txt","w")
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
        ori_machineA_button.update()
        ori_machineB_button.update()
        ori_machineC_button.update()
        screen.blit(surface,screen_rect)

        draw_text("Profile", font, "black", screen, 650, 200)

        f = open("./picture/name.txt","r")
        lines = f.readlines()
        name = lines[0].strip()
        count = list(name)

        fdate = open("./picture/date.txt","r")
        firstdate = fdate.readlines()
        date = firstdate[0].strip()

        path = './picture/totalearned.txt'
        check_file = os.path.isfile(path)

        if len(count) > int(14):
            draw_text(f"Name: {name} ", font, "black", screen, 650, 300)
            draw_text(f"Restaurant", font, "black", screen, 650, 350)
            draw_text(f"Opened in: {date}", font, "black",screen,650, 425)
            if check_file :
                y= open("./picture/totalearned.txt", 'r')
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
                y= open("./picture/totalearned.txt", 'r')
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    profile()
                if event.key == pygame.K_ESCAPE:
                    main()
                if event.key == pygame.K_r:
                    rename()
                

        button.update()
        resetbutton.update()
        profilebutton.update()
        upgrade_btn.update()
        menu_button.update()
        setting_button.update()
        money_bar()
        happyhour_bar(hhactive)

        pygame.display.flip()

def draw_popup():
    ori_machineA_button.update()
    ori_machineB_button.update()
    ori_machineC_button.update()
    profilebutton.update()
    upgrade_btn.update()
    menu_button.update()
    setting_button.update()
    pygame.draw.rect(screen, (255, 201, 254), popup_rect)
    pygame.draw.rect(screen, (148, 5, 100), popup_rect, 5)  # Popup border
    
    screen.blit(coin1_img,(850, 318))
    screen.blit(coin1_img,(1018, 318))
    default_machineA_button.update()
    machineB_button.update()
    machineC_button.update()
    inputmoney_rect = pygame.Rect(740,150, 200, 33)
    pygame.draw.rect(screen, (162, 164, 164), inputmoney_rect)

    draw_text("Money: ", upgrade_font, "black", screen, 700, 170)
    draw_text(money, upgrade_font, "navyblue", screen, 836, 170)
    draw_text("Machine Types: ", upgrade_font, "black", screen, 520, 250)
    draw_text("1800", upgrade_font, "black", screen, 900, 328)
    draw_text("4000", upgrade_font, "black", screen, 1068, 328)
    draw_text("Default", upgrade_font, "black", screen, 710, 343)
    draw_text("Machine B", upgrade_font, "black", screen, 890, 350)
    draw_text("Machine C", upgrade_font, "black", screen, 1060, 350)
    draw_text("Machine Features - B: Cooking process speed up to 40s", upgrade_font, "black", screen, 714, 380)
    draw_text("- C: Cooking process speed up to 30s", upgrade_font, "black", screen, 805, 408)

    close_button.update()

def draw_popup2B():
    # (width,height,x,y)
    popup2_rect = pygame.Rect(423, 430, 750, 230)
    pygame.draw.rect(screen, (243, 191, 215), popup2_rect)
    draw_text("INSTRUCTIONS: ", upgrade_font, "black", screen, 520, 449)
    draw_text("1. Do you want to upgrade your machine?", upgrade_font, "black", screen, 650, 478)

    yesB_button.update()
    noB_button.update()

def draw_popup2C():
    # (width,height,x,y)
    popup2_rect = pygame.Rect(423, 430, 750, 230)
    pygame.draw.rect(screen, (224, 248, 253), popup2_rect)
    draw_text("INSTRUCTIONS: ", upgrade_font, "black", screen, 520, 449)
    draw_text("1. Do you want to upgrade your machine?", upgrade_font, "black", screen, 650, 478)

    yesC_button.update()
    noC_button.update()

def select_upgrade_machineB():
    global selected_upgradeB, message_timer
    popup2_rect = pygame.Rect(423, 430, 750, 230)
    pygame.draw.rect(screen, (243, 191, 215), popup2_rect)
    draw_text(f"Machine upgraded to {selected_upgradeB}!", upgrade_font, "navyblue", screen, 800, 550)
    message_timer -= 1  
    if message_timer == 0:
        selected_upgradeB = False

def select_upgrade_machineC():
    global selected_upgradeC, message_timer
    popup2_rect = pygame.Rect(423, 430, 750, 230)
    pygame.draw.rect(screen, (224, 248, 253), popup2_rect)
    draw_text(f"Machine upgraded to {selected_upgradeC}!", upgrade_font, "navyblue", screen, 800, 550)
    message_timer -= 1  
    if message_timer == 0:
        selected_upgradeC = False

def draw_complete_upgrade():
    global current_upgrade, message_timer,already_upgrade
    popup2_rect = pygame.Rect(423, 430, 750, 230)
    pygame.draw.rect(screen, (255, 229, 215), popup2_rect)
    draw_text(f"Machine has already upgraded to {current_upgrade}!", upgrade_font, "navyblue", screen, 800, 550)
    message_timer -= 1  
    if message_timer == 0:
        already_upgrade = False
        not_enough_money = False

def less_money():
    global message_timer, not_enough_money, show_popup2B, show_popup2C
    popup3_rect = pygame.Rect(423, 430, 750, 230)
    pygame.draw.rect(screen, (255, 201, 254), popup3_rect)
    draw_text("You do not have enough money!", upgrade_font, "red", screen, 800, 630)
    message_timer -= 1  
    if message_timer == 0:
        not_enough_money = False
        show_popup2B = False
        show_popup2C = False

def handle_upgrades(): 
    global show_popup, show_popup2B, show_popup2C, not_enough_money, selected_upgradeB, selected_upgradeC, message_timer, current_upgrade, already_upgrade
    if show_popup:
        draw_popup()

    if show_popup2B:
        draw_popup2B()

    if show_popup2C:
        draw_popup2C()

    if selected_upgradeB:
        select_upgrade_machineB()

    if selected_upgradeC:
        select_upgrade_machineC()

    if already_upgrade:
        draw_complete_upgrade()
        
    if not_enough_money:
        less_money()

def upgrade_process():
    ori_machineA_button.update()
    ori_machineB_button.update()
    ori_machineC_button.update()
    profilebutton.update()
    upgrade_btn.update()
    menu_button.update()
    setting_button.update()
    pygame.draw.rect(screen, (148, 5, 100), popup_rect, 5)  # Popup border
    global show_popup, show_popup2B, show_popup2C, not_enough_money, selected_upgradeB,selected_upgradeC, message_timer, money, unlocked_machine,current_upgrade, already_upgrade
    
    show_popup= True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.checkForInput(pygame.mouse.get_pos()):
                    main()

                if upgrade_btn.checkForInput(pygame.mouse.get_pos()): 
                    draw_popup()

                if machineB_button.checkForInput(pygame.mouse.get_pos()):
                    if "B" in unlocked_machine:
                        current_upgrade = "MACHINE B"
                        already_upgrade = True
                        message_timer = 60
                    else:
                        if money < upgrade_costs["B"]:
                            not_enough_money = True
                            message_timer = 60
                        else:
                            show_popup2B = True
                        
                if yesB_button.checkForInput(pygame.mouse.get_pos()) and show_popup2B:
                    if "B" in unlocked_machine:
                        already_upgrade = True  # Ensure money is not deducted
                        message_timer = 60
                        show_popup2B = False
                    elif money >= upgrade_costs["B"]:
                        money -= upgrade_costs["B"]
                        unlocked_machine.add("B")
                        selected_upgradeB = "B"
                        current_upgrade = "MACHINE B"
                        message_timer = 60
                        show_popup2B = False
                    else:
                        not_enough_money = True
                        message_timer = 60
                
                if machineC_button.checkForInput(pygame.mouse.get_pos()):
                    if "C" in unlocked_machine:
                        current_upgrade = "MACHINE C"
                        already_upgrade = True
                        message_timer = 60
                    else:
                        if money < upgrade_costs["C"]:
                            not_enough_money = True
                            message_timer = 60
                        else:
                            show_popup2C = True
                    
                if yesC_button.checkForInput(pygame.mouse.get_pos()) and show_popup2C:
                    if "C" in unlocked_machine:
                        already_upgrade = True
                        message_timer = 60
                        show_popup2C = False
                    elif money >= upgrade_costs["C"]:
                        money -= upgrade_costs["C"]
                        unlocked_machine.add("C")
                        selected_upgradeC = "C"
                        current_upgrade = "MACHINE C"
                        message_timer = 60
                        show_popup2C = False
                    else:
                        not_enough_money = True
                        message_timer = 60

                if noB_button.checkForInput(pygame.mouse.get_pos()):
                    show_popup2B = False  
                   
                if noC_button.checkForInput(pygame.mouse.get_pos()):
                    show_popup2C = False 

        handle_upgrades()
        profilebutton.update()
        upgrade_btn.update()
        menu_button.update()
        setting_button.update()
        money_bar()
        pygame.display.update()
        clock.tick(60)

        happyhour_bar(hhactive)
        money_bar()

def remind_unlock_popout():
    global message_timer, remind_unlock,current_upgrade
    draw_text(f"You haven't unlocked {current_upgrade }!", food_selection_font, "red", screen, 800, 640)
    message_timer -= 1  
    if message_timer == 0:
        remind_unlock = False

def selectfood_page1():
    while True:
        global message_timer, remind_unlock, current_upgrade
        screen.blit(background, (0, 0))  # Add this to clear the screen properly before drawing
        
        # Draw UI elements
        ori_machineA_button.update()
        ori_machineB_button.update()
        ori_machineC_button.update()
        profilebutton.update()
        upgrade_btn.update()
        menu_button.update()
        setting_button.update()
        pygame.draw.rect(screen, (255, 201, 254), food_selection1_rect)
        pygame.draw.rect(screen, (148, 5, 100), food_selection1_rect, 5)
        draw_text("Please select the machine you want to prepare your food: ", food_selection_font, "black", screen, 800, 240)

        selectDM_btn.update()
        selectMB_btn.update()
        selectMC_btn.update()
        close_button.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.checkForInput(pygame.mouse.get_pos()):
                    main()
                if selectDM_btn.checkForInput(pygame.mouse.get_pos()):
                    return selectfood_page2()  # Call the next page and exit this loop
                if selectMB_btn.checkForInput(pygame.mouse.get_pos()):
                    if "B" in unlocked_machine:
                        selectfood_page2()
                    else:
                        current_upgrade = "MACHINE B "
                        remind_unlock = True
                        message_timer = 60
                if selectMC_btn.checkForInput(pygame.mouse.get_pos()):
                    if "C" in unlocked_machine:
                        selectfood_page2()
                    else:
                        current_upgrade = "MACHINE C "
                        remind_unlock = True
                        message_timer = 60

        money_bar()
        happyhour_bar(hhactive)

        if remind_unlock:
            remind_unlock_popout()

        pygame.display.update()
        clock.tick(60)

# Assume current_page starts from 1 and max_items_per_page is 3
current_page = 1
max_items_per_page = 3

# Calculate the total number of pages
total_pages = (len(food_lists) + max_items_per_page - 1) // max_items_per_page

def selectfood_page2():
    while True:
        global current_page
        screen.blit(background, (0, 0))  # Clear the screen before drawing
        ori_machineA_button.update()
        ori_machineB_button.update()
        ori_machineC_button.update() 

        # Render the food selection UI
        food_selection1_rect = pygame.Rect(400, 120, 800, 600)
        food_selection2_rect = pygame.Rect(425, 195, 752, 495)
        pygame.draw.rect(screen, (255, 201, 254), food_selection1_rect)
        pygame.draw.rect(screen, (148, 5, 100), food_selection1_rect, 5)
        pygame.draw.rect(screen, (196, 192, 255), food_selection2_rect)

        draw_text("Food selection: ", food_selection_font, "black", screen, 550, 155)

        # Determine items to display on the current page
        start_index = (current_page - 1) * max_items_per_page
        end_index = start_index + max_items_per_page
        items_on_page = food_lists[start_index:end_index]

        # Render the items
        for i in range(len(items_on_page)):
            food_item = items_on_page[i]
            y_position = 216 + i * 144
            pygame.draw.rect(screen, color_pic, pygame.Rect(440, y_position, 720, 130))
            screen.blit(food_item["image"], (460, y_position + 4))
            draw_text(food_item["name"], food_title_font, "black", screen, 700, y_position + 60)
            draw_text(food_item["price"], food_title_font, "black", screen, 900, y_position + 60)

        # Handle next/back buttons
        total_pages = (len(food_lists) + max_items_per_page - 1) // max_items_per_page
        if current_page < total_pages:
            next_btn.update()

        if current_page > 1:
            back_btn.update()

        # Event handling for buttons
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.checkForInput(pygame.mouse.get_pos()):
                    return main()
                if next_btn.checkForInput(pygame.mouse.get_pos()) and current_page < total_pages:
                    current_page += 1
                if back_btn.checkForInput(pygame.mouse.get_pos()) and current_page > 1:
                    current_page -= 1
        
        money_bar()
        profilebutton.update()
        menu_button.update()
        upgrade_btn.update()
        menu_button.update()
        setting_button.update()
        close_button.update()
        happyhour_bar(hhactive)
        pygame.display.update()
        clock.tick(60)


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
                if upgrade_btn.checkForInput(pygame.mouse.get_pos()): 
                    upgrade_process()
                if menu_button.checkForInput(pygame.mouse.get_pos()): 
                    selectfood_page1()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    profile()


        money_bar()
        profilebutton.update()
        upgrade_btn.update()
        ori_machineA_button.update()
        ori_machineB_button.update()
        ori_machineC_button.update()
        menu_button.update()
        setting_button.update()
        happyhour_bar(hhactive)

        pygame.display.flip()
        clock.tick(60)
#money
money_amount = 0
max_display_money = 1000000

def money_bar():
    money_text = font2.render(f"{money_amount}", True, black)
    text_rect = money_text.get_rect(center=(1250,55))
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
    remaining_order = (order_completed % 5 - 5) % 5
    if hhactive:
        hhtext = font2.render(f"Happy Hour Active! {remaining_order} /5", True, black)
    else:
        hhtext = font2.render(f"Happy Hour {remaining_order} /5", True, black)
    text_rect = hhtext.get_rect(center=(650,60))
    screen.blit(hhtext,text_rect)

def hhprofit(origin_profit):
    if hhactive:
        return origin_profit * 2
    return origin_profit

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
        show_intropage()
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
                            f = open("./picture/name.txt","x")
                            fdate = open("./picture/date.txt", "x")

                            f = open("./picture/name.txt", "a")
                            f.write(f'{user_text}')
                            f.close()

                            fdate = open("./picture/date.txt","a")
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

#intro
closebutton = pygame.image.load('./picture/closebutton.png')
closebutton = pygame.transform.scale(closebutton, (50,50))

nextbutton = pygame.image.load('./picture/nextbutton.png')
nextbutton = pygame.transform.scale(nextbutton, (50,50))

noticeboard = pygame.image.load('./picture/noticeboard.png')
noticeboard = pygame.transform.scale(noticeboard, (1400,800))

background = pygame.image.load('./picture/lobby.jpg')
background = pygame.transform.scale(background, (screen_width,screen_height))

noticeboard_rect = noticeboard.get_rect(center=(700,400))
closebutton_rect = closebutton.get_rect(topright=(900,100))
nextbutton_rect = nextbutton.get_rect(bottomright=(900,700))
notice_font = pygame.font.Font('./picture/jugnle.ttf',20)
noticetext1 = "Welcome to World Restaurant!\nIntroduction of the game..."
noticetext2 = "Many tutorial...\nBla bla bla..."



def render_introtext(text,font,color,center):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        rendered_line = notice_font.render(line,True,black)
        line_rect = rendered_line.get_rect(center=(center[0],center[1] - 20 + i * 40))
        screen.blit(rendered_line,line_rect)

def intropage1():
    screen.blit(background,(0,0))
    screen.blit(noticeboard, noticeboard_rect)
    render_introtext(noticetext1,notice_font,black,(noticeboard_rect.centerx-50,noticeboard_rect.centery-250))
    screen.blit(nextbutton,nextbutton_rect)

def intropage2():
    screen.blit(background,(0,0))
    screen.blit(noticeboard,noticeboard_rect)
    render_introtext(noticetext2,notice_font,black,(noticeboard_rect.centerx-50,noticeboard_rect.centery-250))
    screen.blit(closebutton,closebutton_rect)

def intropage_click(page,mouse_pressed_last_frame):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]
    if page == 1 and nextbutton_rect.collidepoint(mouse_pos):
        if not mouse_pressed_last_frame and mouse_pressed:
            return 2,mouse_pressed
    elif page == 2 and closebutton_rect.collidepoint(mouse_pos):
        if not mouse_pressed_last_frame and mouse_pressed:
            return 0,mouse_pressed
    return page,mouse_pressed

def show_intropage():
    global intropage, mouse_pressed_last_frame
    intropage = 1
    mouse_pressed_last_frame = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if intropage == 1:
            intropage1()
        elif intropage == 2:
            intropage2()
        intropage,mouse_pressed_last_frame = intropage_click(intropage,mouse_pressed_last_frame)
        if intropage == 0:
            main()


        pygame.display.flip()
        pygame.time.Clock().tick(30)


#logo_fade
start_time = time.time()
fade_duration = 3
logo = pygame.image.load('./picture/logo.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    elapsed_time = time.time() - start_time
    
    if elapsed_time < fade_duration:
        fade_alpha = int(255 * (1 - (elapsed_time / fade_duration)))
        logo.set_alpha(fade_alpha)
        screen.fill(white)
        screen.blit(logo, (0,0))
    else:
        path = './picture/name.txt'
        check_file = os.path.isfile(path)
        now = datetime.datetime.now()
        other_StyleTime = now.strftime("%Y-%m-%d")


        if check_file == True:
            f = open("./picture/name.txt", "r") 
            lines = f.readlines()
            show_name_from_file(lines[0].strip())
        else:
            get_restaurant_name()

    pygame.display.flip()
    pygame.time.Clock().tick(30)
    
pygame.quit()
sys.exit()