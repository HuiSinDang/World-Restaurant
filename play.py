#start
import pygame
import sys
import time
import os.path
import datetime
import random
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

screen_rect1 = screen.get_rect()
screen_rect1.x = 200
screen_rect1.y = 150
pygame.draw.rect(surface,(215, 228, 231 ,200),surface.get_rect(),0)

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
    "B": "Criteria - Cooking process lowered to 40s",
    "C": "Criteria - Cooking process lowered to 30s",
}

# Define the cost for each machine upgrade
upgrade_costs = {
    "STEAMER": 1800,  
    "OVEN": 4000   
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

corndog_img = pygame.image.load("./picture/corndog.png")
corndog_img = pygame.transform.scale(corndog_img, (130, 127))

tokbokki_img = pygame.image.load("./picture/tokbokki.png")
tokbokki_img = pygame.transform.scale(tokbokki_img, (100, 127))

corndogcheese_img = pygame.image.load("./picture/corndogcheese.png")
corndogcheese_img = pygame.transform.scale(corndogcheese_img, (100, 127))

roticanai_img = pygame.image.load("./picture/roticanai.png")
roticanai_img = pygame.transform.scale(roticanai_img, (100, 127))

dumpling_img = pygame.image.load("./picture/dumpling.png")
dumpling_img = pygame.transform.scale(dumpling_img, (100, 127))

dimsum_img = pygame.image.load("./picture/dimsum.png")
dimsum_img = pygame.transform.scale(dimsum_img, (100, 127))

mooncake_img = pygame.image.load("./picture/mooncake.png")
mooncake_img = pygame.transform.scale(mooncake_img, (100, 115))

nasilemak_img = pygame.image.load("./picture/nasilemak.png")
nasilemak_img = pygame.transform.scale(nasilemak_img, (100, 127))

satay_img = pygame.image.load("./picture/satay.png")
satay_img = pygame.transform.scale(satay_img, (100, 120))

friedrice_img = pygame.image.load("./picture/friedrice.png")
friedrice_img = pygame.transform.scale(friedrice_img, (121, 110))

oden_img = pygame.image.load("./picture/oden.png")
oden_img = pygame.transform.scale(oden_img, (125, 120))

bibimbap_img = pygame.image.load("./picture/bibimbap.png")
bibimbap_img = pygame.transform.scale(bibimbap_img, (140, 110))

dialogbox_img = pygame.image.load("./picture/dialog-box.png")
dialogbox_img = pygame.transform.scale(dialogbox_img, (100, 100))

armystew_img = pygame.image.load("./picture/armystew.png")
armystew_img = pygame.transform.scale(armystew_img, (150, 120))

steamfish_img = pygame.image.load("./picture/steamfish.png")
steamfish_img = pygame.transform.scale(steamfish_img, (140, 120))

kfry_img = pygame.image.load("./picture/kfry.png")
kfry_img = pygame.transform.scale(kfry_img, (130, 120))

calamari_img = pygame.image.load("./picture/calamari.png")
calamari_img = pygame.transform.scale(calamari_img, (110, 127))

rainbowcake_img = pygame.image.load("./picture/rainbowcake.png")
rainbowcake_img = pygame.transform.scale(rainbowcake_img, (120, 115))

redvelvet_img = pygame.image.load("./picture/redvelvet.png")
redvelvet_img = pygame.transform.scale(redvelvet_img, (120, 110))

blackforest_img = pygame.image.load("./picture/blackforest.png")
blackforest_img = pygame.transform.scale(blackforest_img, (150, 110))

pandanrollcake_img = pygame.image.load("./picture/pandanrollcake.png")
pandanrollcake_img = pygame.transform.scale(pandanrollcake_img, (126, 127))



food_lists =[
    {"image": tokbokki_img, "name": "Tokbokki", "price": "RM10.00"},

    {"image": friedrice_img, "name": "Fried rice", "price": "RM5.00"},

    {"image": oden_img, "name": "Oden", "price": "RM10.00"},

    {"image": bibimbap_img, "name": "Bibimbap", "price": "RM12.50"},

    {"image": armystew_img, "name": "Korean Army Stew", "price": "RM60.00" },

    {"image": mooncake_img, "name": "Mooncake", "price": "RM16.00"},

    {"image": satay_img, "name": "Satay(10 sticks)", "price": "RM10.00" },


]

foodlist_steamer = [
    {"image": steamfish_img, "name": "Thai Steamed Fish", "price": "RM50.00"},

    {"image": dimsum_img, "name": "Dimsum", "price": "RM12.00" },

    {"image": dumpling_img, "name": "Dumpling", "price": "RM6.00"},

    {"image": steamfish_img, "name": "Thai Steamed Fish", "price": "RM50.00"},

    {"image": dimsum_img, "name": "Dimsum", "price": "RM12.00" },

    
]

foodlist_oven = [
    {"image": corndog_img, "name": "Jumbo Corndog", "price": "RM25.00"},

    {"image": kfry_img, "name": "Korean Fried Chicken", "price": "RM22.00"},

    {"image": calamari_img, "name": "Calamari Rings", "price": "RM30.00"},

    {"image": rainbowcake_img, "name": "Rainbow cake (1 slice)", "price": "RM16.00"},

    {"image": redvelvet_img, "name": "Red Velvet (4-inch)", "price": "RM55.00"},

    {"image": blackforest_img, "name": "Black Forest (4-inch)", "price": "RM60.00"},

    {"image": pandanrollcake_img, "name": "Pandan Roll Cake", "price": "RM16.00"},

    {"image": corndog_img, "name": "Jumbo Corndog", "price": "RM25.00"},
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


class CookingBar: # draw cooking bar
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp
        self.start_time = None

    def draw(self, surface):
        # Calculate health ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

    def update(self, elapsed_time, duration):
        # Decrease hp based on elapsed time and duration
        self.hp = max(0, self.max_hp * (1 - elapsed_time / duration))
    


# SELECT button
selectbutton_surface = pygame.Surface((130, 40))
selectprepare_button_rect = pygame.Rect(1010, 90, 150, 40) 
SELECT_text = food_title_font.render(" SELECT ", True, "black")
text_rect = SELECT_text.get_rect(center=(selectbutton_surface.get_width()/2, selectbutton_surface.get_height()/2))

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
upgrade_btn= Button(upgrade_btn, 76, 500, "")

pan_unlock_button = pygame.image.load("./picture/pan-border.png")
pan_unlock_button = pygame.transform.scale(pan_unlock_button, (140, 130))
pan_unlock_button = Button(pan_unlock_button, 710, 260, "")

steamer_unlock_button = pygame.image.load("./picture/steamer-border.png")
steamer_unlock_button = pygame.transform.scale(steamer_unlock_button, (140, 130))
steamer_unlock_button = Button(steamer_unlock_button, 890, 258, "")

oven_unlock_button = pygame.image.load("./picture/oven-border.png")
oven_unlock_button = pygame.transform.scale(oven_unlock_button, (140, 130))
oven_unlock_button = Button(oven_unlock_button, 1068, 255, "")

pan_default_button = pygame.image.load("./picture/pan.png")
pan_default_button = pygame.transform.scale(pan_default_button, (260, 240))
pan_default_button = Button(pan_default_button, 440, 250, "")

steamer_button = pygame.image.load("./picture/steamer.png")
steamer_button = pygame.transform.scale(steamer_button, (220, 247))
steamer_button = Button(steamer_button, 740, 254, "")

oven_button = pygame.image.load("./picture/oven.png")
oven_button = pygame.transform.scale(oven_button, (240, 210))
oven_button = Button(oven_button, 1050, 255, "")

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
menu_button = Button(menu_button, 76, 225, "")

setting_button = pygame.image.load("./picture/setting.png")
setting_button = pygame.transform.scale(setting_button, (120, 120))
setting_button = Button(setting_button, 73, 650, "")

next_btn = pygame.image.load("./picture/nextbutton.png")
next_btn = pygame.transform.scale(next_btn, (50, 60))
next_btn = Button(next_btn, 1138, 669, "")

back_btn = pygame.image.load("./picture/back_btn.png")
back_btn = pygame.transform.scale(back_btn, (60, 70))
back_btn = Button(back_btn, 460, 665, "")




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

orderbtn_surface = pygame.image.load("./picture/order_btn.png")
orderbtn_surface = pygame.transform.scale(orderbtn_surface, (175, 175))
orderbtn = Button(orderbtn_surface, 75, 360,"")

order1button_surface = pygame.image.load("./picture/order.png")
order1button_surface = pygame.transform.scale(order1button_surface, (400, 400))
order1button = Button(order1button_surface, 350, 350,"")

order2button_surface = pygame.image.load("./picture/order.png")
order2button_surface = pygame.transform.scale(order2button_surface, (400, 400))
order2button = Button(order2button_surface, 650, 350,"")

order3button_surface = pygame.image.load("./picture/order.png")
order3button_surface = pygame.transform.scale(order3button_surface, (400, 400))
order3button = Button(order3button_surface, 950, 350,"")

completebutton_surface = pygame.image.load("./picture/reset_btn.png")
completebutton_surface = pygame.transform.scale(completebutton_surface, (250, 250))
completebutton = Button(completebutton_surface, 600, 575,"Complete")

man1_surface = pygame.image.load("./picture/man.png")
man1_surface = pygame.transform.scale(man1_surface, (50, 50))
man1 = Button(man1_surface, 260, 435,"")

man2_surface = pygame.image.load("./picture/man.png")
man2_surface = pygame.transform.scale(man2_surface, (50, 50))
man2 = Button(man2_surface, 570, 435,"")

man3_surface = pygame.image.load("./picture/man.png")
man3_surface = pygame.transform.scale(man3_surface, (50, 50))
man3 = Button(man3_surface, 875, 435,"")

chick1_surface = pygame.image.load("./picture/chick.png")
chick1_surface = pygame.transform.scale(chick1_surface, (50, 50))
chick1 = Button(chick1_surface, 260, 435,"")

chick2_surface = pygame.image.load("./picture/chick.png")
chick2_surface = pygame.transform.scale(chick2_surface, (50, 50))
chick2 = Button(chick2_surface, 570, 435,"")

chick3_surface = pygame.image.load("./picture/chick.png")
chick3_surface = pygame.transform.scale(chick3_surface, (50, 50))
chick3 = Button(chick3_surface, 875, 435,"")

robot1_surface = pygame.image.load("./picture/robot.png")
robot1_surface = pygame.transform.scale(robot1_surface, (50, 50))
robot1 = Button(robot1_surface, 260, 435,"")

robot2_surface = pygame.image.load("./picture/robot.png")
robot2_surface = pygame.transform.scale(robot2_surface, (50, 50))
robot2 = Button(robot2_surface, 570, 435,"")

robot3_surface = pygame.image.load("./picture/robot.png")
robot3_surface = pygame.transform.scale(robot3_surface, (50, 50))
robot3 = Button(robot3_surface, 875, 435,"")

unorder1button_surface = pygame.image.load("./picture/unorder.png")
unorder1button_surface = pygame.transform.scale(unorder1button_surface, (400, 400))
unorder1button = Button(unorder1button_surface, 350, 350,"")

unorder2button_surface = pygame.image.load("./picture/unorder.png")
unorder2button_surface = pygame.transform.scale(unorder2button_surface, (400, 400))
unorder2button = Button(unorder2button_surface, 650, 350,"")

unorder3button_surface = pygame.image.load("./picture/unorder.png")
unorder3button_surface = pygame.transform.scale(unorder3button_surface, (400, 400))
unorder3button = Button(unorder3button_surface, 950, 350,"")

frame1_surface = pygame.image.load("./picture/frame.png")
frame1_surface = pygame.transform.scale(frame1_surface, (295, 295))
frame1 = Button(frame1_surface, 345, 350,"")

frame2_surface = pygame.image.load("./picture/frame.png")
frame2_surface = pygame.transform.scale(frame2_surface, (295, 295))
frame2 = Button(frame2_surface, 645, 350,"")

frame3_surface = pygame.image.load("./picture/frame.png")
frame3_surface = pygame.transform.scale(frame3_surface, (295, 295))
frame3 = Button(frame3_surface, 945, 350,"")

# Main loop(irene)
show_popup = False
show_popup2B = False
show_popup2C = False
selected_upgradeB = None
selected_upgradeC = None
current_upgrade = None
already_upgrade = False
not_enough_money = False  # indicate not enough money
message_timer = 0  # Timer to show messages temporarily
money = 5000     #不确定要不要
unlocked_machine = set() # Set to track unlocked machines
remind_unlock = False
stovepot_call = False
steamer_call = False
oven_call = False

#money#
money_amount = 0
max_display_money = 1000000
money_file_path = os.path.join(os.getcwd(),"./picture/money.txt")

def show_money():
    if os.path.exists(money_file_path):
        try:
            with open("./picture/money.txt","r")as file:
                return int(file.read())
        except (ValueError,IOError):
            return 0
    else:
        return 0
    
def save_money():
    with open("./picture/money.txt","w") as file:
        file.write(str(money_amount))

def money_bar():
    money_text = font2.render(f"{money_amount}",True,black)
    text_rect = money_text.get_rect(center=(1250,55))
    screen.blit(money_text,text_rect)

def add_money(amount):
    global money_amount
    money_amount += amount
    money_amount = min(money_amount,max_display_money)
    save_money()

def subtract_money(amount):
    global money_amount
    if money_amount >= amount:
        money_amount -= amount
        money_amount = max(money_amount,0)
        save_money()
        return True
    else:
        return False
    
money_amount = show_money()

#happy hour
order_completed = 0
hhactive = False
hhtime = 30
hh_start_time = None
hh_file_path = os.path.join(os.getcwd(),"./picture/happyhour.txt")

def show_order_completed():
    if os.path.exists(money_file_path):
        try:
            with open("./picture/happyhour.txt","r")as file:
                return int(file.read())
        except (ValueError,IOError):
            return 0
    else:
        return 0
    
def save_order():
    with open("./picture/happyhour.txt","w") as file:
        file.write(str(order_completed))

def add_order(amount):
    global order_completed
    order_completed += amount
    save_order()

def update_happy_hour_status():
    global hhactive,order_completed,hh_start_time
    if order_completed >= 5:
        hhactive = True
        hh_start_time = time.time()
        order_completed = order_completed % 5
        save_order()
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
        pan_default_button.update()
        steamer_button.update()
        oven_button.update()
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
        orderbtn.update()
        money_bar()
        waiting_table()
        happyhour_bar(hhactive)

        pygame.display.flip()

order_profits = {
    'order1': 25,
    'order2': 43,
    'order3': 52
}

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(str(text), True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def update_button_image1(order_button1, all_available):
    # 更新按钮图片的函数
    if all_available:
        order_button1.update()  # 正常按钮图片
    else:
        unorder1button.update()  # 特殊按钮图片

def update_button_image2(order_button2, all_available):
    # 更新按钮图片的函数
    if all_available:
        order_button2.update()  # 正常按钮图片
    else:
        unorder2button.update()  # 特殊按钮图片

def update_button_image3(order_button3, all_available):
    # 更新按钮图片的函数
    if all_available:
        order_button3.update()  # 正常按钮图片
    else:
        unorder3button.update()  # 特殊按钮图片


# Main order function
def order():
    global show_complete_button1, show_complete_button2, show_complete_button3
    show_complete_button1 = False
    show_complete_button2 = False
    show_complete_button3 = False
    last_clicked_order = None
    
    while True:
        bg_img = pygame.image.load("./picture/lobby.jpg").convert()
        screen.blit(bg_img, (0, 0))  # Draw the background
        pan_default_button.update()
        steamer_button.update()
        oven_button.update()
        screen.blit(surface,screen_rect1)

        button.update()
        profilebutton.update()
        upgrade_btn.update()
        menu_button.update()
        setting_button.update()
        orderbtn.update()
        money_bar()
        happyhour_bar(hhactive)

        draw_text("Order", main_font, "black", screen, 650, 190)  # On top of button 1

        f = open("./picture/food.txt", "r")
        food = [line.strip() for line in f.readlines() if line.strip()]

        completebutton.update()

        #order1
        path1 = './picture/order1.txt'
        check_file1 = os.path.isfile(path1)
        fstaff1 = open("./picture/staff.txt", "r") 
        staff1 = [line.strip() for line in fstaff1.readlines() if line.strip()]

        if check_file1:
            ffood1 = open(path1, "r") 
            order1 = [line.strip() for line in ffood1.readlines() if line.strip()]
            fwaitingtable1 = open("./picture/waitingtable.txt", "r") 
            waitingtable1 = [line.strip() for line in fwaitingtable1.readlines() if line.strip()]
            y_offset = 275

            if order1 == []:
                ffood1 = open(path1, "a") 
                nofood = random.randint(1, 3)
                people1 = random.randint(1, 3)
                staff1.insert(0, people1)
                fstaff1 = open("./picture/staff.txt", "w")
                for i in staff1:
                    fstaff1.write(f'{i}\n')
                fstaff1.close()

                # 更新员工图像
                if int(people1) == 1:
                    man1.update()
                elif int(people1) == 2:
                    chick1.update()
                else:
                    robot1.update()

                for i in range(nofood):
                    y = random.randint(0, len(food) - 1)
                    f1 = food[y]
                    order1.append(f1)
                    ffood1.write(f'{f1}\n')
                    if f1 in waitingtable1 :
                        color = "green"
                    else :
                        color = "red"
                    draw_text(f1, main_font, color, screen, 350, y_offset)  # On top of button 1
                    y_offset += 50
                ffood1.close()

            else:

                waitingtable_copy1 = waitingtable1.copy()

                all_in_waitingtable1 = True
                for f1 in order1:
                    if f1 in waitingtable_copy1:
                        waitingtable_copy1.remove(f1)
                    else :
                        all_in_waitingtable1 = False
                        break
                update_button_image1(order1button, all_in_waitingtable1)

                # 更新员工图像
                if int(staff1[0]) == 1:
                    man1.update()
                elif int(staff1[0]) == 2:
                    chick1.update()
                else:
                    robot1.update()

                waitingtable_copy1 = waitingtable1.copy()
                y_offset = 275

                for f1 in order1:
                    if f1 in waitingtable_copy1:
                        color = "green"
                    else :
                        color = "red"
                    if f1 in waitingtable_copy1:
                        waitingtable_copy1.remove(f1)
                    draw_text(f1, main_font, color, screen, 350, y_offset)  # On top of button 1
                    y_offset += 50
                ffood1.close()
        else:
            ffood1 = open(path1, "x") 
            ffood1 = open(path1, "r") 
            order1 = [line.strip() for line in ffood1.readlines() if line.strip()]
            ffood1 = open(path1, "a")     
            y_offset = 275
            nofood = random.randint(1, 3)
            fwaitingtable1 = open("./picture/waitingtable.txt", "r") 
            waitingtable1 = [line.strip() for line in fwaitingtable1.readlines() if line.strip()]
            people1 = random.randint(1, 3)
            staff1.insert(0, people1)
            fstaff1 = open("./picture/staff.txt", "w")
            for i in staff1:
                fstaff1.write(f'{i}\n')
            fstaff1.close()

            # 更新员工图像
            if int(people1) == 1:
                man1.update()
            elif int(people1) == 2:
                chick1.update()
            else:
                robot1.update()

            for i in range(nofood):
                y = random.randint(0, len(food) - 1)
                f1 = food[y]
                order1.append(f1)
                ffood1.write(f'{f1}\n')
                color = "green" if f1 in waitingtable1 else "red"
                draw_text(f1, main_font, color, screen, 350, y_offset)  # On top of button 1
                y_offset += 50
            ffood1.close()

        #order 2
        path2 = './picture/order2.txt'
        check_file2 = os.path.isfile(path2)
        fstaff2 = open("./picture/staff.txt", "r") 
        staff2 = [line.strip() for line in fstaff2.readlines() if line.strip()]

        if check_file2:
            ffood2 = open(path2, "r") 
            order2 = [line.strip() for line in ffood2.readlines() if line.strip()]
            fwaitingtable2 = open("./picture/waitingtable.txt", "r") 
            waitingtable2 = [line.strip() for line in fwaitingtable2.readlines() if line.strip()]
            y_offset = 275

            if not order2:
                ffood2 = open(path2, "a") 
                nofood = random.randint(1, 3)
                people2 = random.randint(1, 3)
                staff2.insert(1, people2)
                fstaff2 = open("./picture/staff.txt", "w")
                for i in staff2:
                    fstaff2.write(f'{i}\n')
                fstaff2.close()

                # 更新员工图像
                if int(people2) == 1:
                    man2.update()
                elif int(people2) == 2:
                    chick2.update()
                else:
                    robot2.update()

                for i in range(nofood):
                    y = random.randint(0, len(food) - 1)
                    f2 = food[y]
                    order2.append(f2)
                    ffood2.write(f'{f2}\n')
                    if f2 in waitingtable2:
                        color = "green"
                    else :
                        color = "red"
                    draw_text(f2, main_font, color, screen, 650, y_offset)  # On top of button 2
                    y_offset += 50
                ffood2.close()

            else:
                # 创建一个waitingtable的拷贝，用来逐一匹配食物项
                waitingtable_copy2 = waitingtable2.copy()

                all_in_waitingtable2 = True
                for f2 in order2:
                    if f2 in waitingtable_copy2:
                        waitingtable_copy2.remove(f2)  # 成功匹配后从副本中移除该项
                    else:
                        all_in_waitingtable2 = False  # 一旦有一个食物无法匹配，就标记为False
                        break

                update_button_image2(order2button, all_in_waitingtable2)

                # 更新员工图像
                if int(staff2[1]) == 1:
                    man2.update()
                elif int(staff2[1]) == 2:
                    chick2.update()
                else:
                    robot2.update()

                waitingtable_copy2 = waitingtable2.copy()
                y_offset = 275

                for f2 in order2:
                    if f2 in waitingtable_copy2:
                        color = "green"
                    else:
                        color = "red"
                    if f2 in waitingtable_copy2:
                        waitingtable_copy2.remove(f2)  # 成功匹配后移除该项
                    draw_text(f2, main_font, color, screen, 650, y_offset)  # On top of button 2
                    y_offset += 50
                ffood2.close()
        else:
            ffood2 = open(path2, "x") 
            ffood2 = open(path2, "r") 
            order2 = [line.strip() for line in ffood2.readlines() if line.strip()]
            ffood2 = open(path2, "a")     
            y_offset = 275
            nofood = random.randint(1, 3)
            fwaitingtable2 = open("./picture/waitingtable.txt", "r") 
            waitingtable2 = [line.strip() for line in fwaitingtable2.readlines() if line.strip()]
            people2 = random.randint(1, 3)
            staff2.insert(1, people2)
            fstaff2 = open("./picture/staff.txt", "w")
            for i in staff2:
                fstaff2.write(f'{i}\n')
            fstaff2.close()

            # 更新员工图像
            if int(people2) == 1:
                man2.update()
            elif int(people2) == 2:
                chick2.update()
            else:
                robot2.update()

            for i in range(nofood):
                y = random.randint(0, len(food) - 1)
                f2 = food[y]
                order2.append(f2)
                ffood2.write(f'{f2}\n')
                if f2 in waitingtable2:
                    color = "green"
                else:
                    color = "red"
                draw_text(f2, main_font, color, screen, 650, y_offset)  # On top of button 2
                y_offset += 50
            ffood2.close()

        #order 3
        path3 = './picture/order3.txt'
        check_file3 = os.path.isfile(path3)
        fstaff3 = open("./picture/staff.txt", "r") 
        staff3 = [line.strip() for line in fstaff3.readlines() if line.strip()]

        if check_file3:
            ffood3 = open(path3, "r") 
            order3 = [line.strip() for line in ffood3.readlines() if line.strip()]
            fwaitingtable3 = open("./picture/waitingtable.txt", "r") 
            waitingtable3 = [line.strip() for line in fwaitingtable3.readlines() if line.strip()]
            y_offset = 275

            if not order3:
                ffood3 = open(path3, "a") 
                nofood = random.randint(1, 3)
                people3 = random.randint(1, 3)
                staff3.insert(2, people3)
                fstaff3 = open("./picture/staff.txt", "w")
                for i in staff3:
                    fstaff3.write(f'{i}\n')
                fstaff3.close()

                # 更新员工图像
                if int(people3) == 1:
                    man3.update()
                elif int(people3) == 2:
                    chick3.update()
                else:
                    robot3.update()

                for i in range(nofood):
                    y = random.randint(0, len(food) - 1)
                    f3 = food[y]
                    order3.append(f3)
                    ffood3.write(f'{f3}\n')
                    if f3 in waitingtable3:
                        color = "green"
                    else:
                        color = "red"
                    draw_text(f3, main_font, color, screen, 950, y_offset)  # On top of button 3
                    y_offset += 50
                ffood3.close()

            else:
                # 创建一个waitingtable的拷贝，用来逐一匹配食物项
                waitingtable_copy3 = waitingtable3.copy()

                all_in_waitingtable3 = True
                for f3 in order3:
                    if f3 in waitingtable_copy3:
                        waitingtable_copy3.remove(f3)  # 成功匹配后从副本中移除该项
                    else:
                        all_in_waitingtable3 = False  # 一旦有一个食物无法匹配，就标记为False
                        break

                update_button_image3(order3button, all_in_waitingtable3)

                # 更新员工图像
                if int(staff3[2]) == 1:
                    man3.update()
                elif int(staff3[2]) == 2:
                    chick3.update()
                else:
                    robot3.update()

                waitingtable_copy3 = waitingtable3.copy()
                y_offset = 275

                for f3 in order3:
                    if f3 in waitingtable_copy3:
                        color = "green"
                    else:
                        color = "red"
                    if f3 in waitingtable_copy3:
                        waitingtable_copy3.remove(f3)  # 成功匹配后移除该项
                    draw_text(f3, main_font, color, screen, 950, y_offset)  # On top of button 3
                    y_offset += 50
                ffood3.close()
        else:
            ffood3 = open(path3, "x") 
            ffood3 = open(path3, "r") 
            order3 = [line.strip() for line in ffood3.readlines() if line.strip()]
            ffood3 = open(path3, "a")     
            y_offset = 275
            nofood = random.randint(1, 3)
            fwaitingtable3 = open("./picture/waitingtable.txt", "r") 
            waitingtable3 = [line.strip() for line in fwaitingtable3.readlines() if line.strip()]
            people3 = random.randint(1, 3)
            staff3.insert(2, people3)
            fstaff3 = open("./picture/staff.txt", "w")
            for i in staff3:
                fstaff3.write(f'{i}\n')
            fstaff3.close()

            # 更新员工图像
            if int(people3) == 1:
                man3.update()
            elif int(people3) == 2:
                chick3.update()
            else:
                robot3.update()

            for i in range(nofood):
                y = random.randint(0, len(food) - 1)
                f3 = food[y]
                order3.append(f3)
                ffood3.write(f'{f3}\n')
                if f3 in waitingtable3:
                    color = "green"
                else:
                    color = "red"
                draw_text(f3, main_font, color, screen, 950, y_offset)  # On top of button 3
                y_offset += 50
            ffood3.close()
        
        if last_clicked_order == "order1":
            frame1.update()
        elif last_clicked_order == "order2" :
            frame2.update()
        elif last_clicked_order == "order3" :
            frame3.update()


        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.checkForInput(pygame.mouse.get_pos()):
                    main()
                if profilebutton.checkForInput(pygame.mouse.get_pos()):
                    profile()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    profile()
                if event.key == pygame.K_ESCAPE:
                    main()


            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if order1button.checkForInput(mouse_pos):
                    if all_in_waitingtable1 == True:
                        last_clicked_order = "order1"
                    else:
                        draw_text("The order is not completed", main_font, "red", screen, 650, 510)  # On top of button 1
                        pygame.display.flip()
                        pygame.time.wait(1000)

                if order2button.checkForInput(mouse_pos):
                    if all_in_waitingtable2 == True:
                        last_clicked_order = "order2"
                    else:
                        draw_text("The order is not completed", main_font, "red", screen, 650, 510)  # On top of button 2
                        pygame.display.flip()
                        pygame.time.wait(1000)

                if order3button.checkForInput(mouse_pos):
                    if all_in_waitingtable3 == True:
                        last_clicked_order = "order3"
                    else:
                        draw_text("The order is not completed", main_font, "red", screen, 650, 510)  # On top of button 3
                        pygame.display.flip()
                        pygame.time.wait(1000)

                if completebutton.checkForInput(pygame.mouse.get_pos()):
                    if last_clicked_order == "order1":
                        def load_list_from_file(filename):
                            file =  open(filename, 'r') 
                            return [line.strip() for line in file.readlines()]
                        
                        def save_list_to_file(filename, data_list):
                            file = open(filename, 'w') 
                            for item in data_list:
                                file.write(f"{item}\n")

                        def check_and_update_lists(list1_filename, list2_filename):
                            pygame.display.flip()
                            list1 = load_list_from_file(list1_filename)
                            list2 = load_list_from_file(list2_filename)

                            for item in list1:
                                list2.remove(item)

                            list1.clear()  

                            fstaff1 = open("./picture/staff.txt", "r") 
                            staff1 = [line.strip() for line in fstaff1.readlines() if line.strip()]
                            del staff1[0]
                            fstaff1 = open("./picture/staff.txt", "w")
                            for i in staff1 :
                                fstaff1.write(f'{i}\n')
                            fstaff1.close()

                            save_list_to_file(list1_filename, list1)
                            save_list_to_file(list2_filename, list2)

                            draw_text("Order Completed!!!", main_font, "green", screen, 650, 510)  # On top of button 1
                            pygame.display.flip()
                            pygame.time.wait(1000)

                        list1_filename = './picture/order1.txt'
                        list2_filename = './picture/waitingtable.txt'

                        check_and_update_lists(list1_filename, list2_filename)
                        last_clicked_order = None
                        profit_per_order = order_profits['order1']
                        add_money(profit_per_order)
                        order_completed +=1

                    elif last_clicked_order == "order2":
                        def load_list_from_file(filename):
                            file =  open(filename, 'r') 
                            return [line.strip() for line in file.readlines()]

                        def save_list_to_file(filename, data_list):
                            file = open(filename, 'w') 
                            for item in data_list:
                                file.write(f"{item}\n")

                        def check_and_update_lists(list1_filename, list2_filename):
                            list1 = load_list_from_file(list1_filename)
                            list2 = load_list_from_file(list2_filename)

                            for item in list1:
                                list2.remove(item)

                            list1.clear()  
                            fstaff2 = open("./picture/staff.txt", "r") 
                            staff2 = [line.strip() for line in fstaff2.readlines() if line.strip()]
                            del staff2[1]
                            fstaff2 = open("./picture/staff.txt", "w")
                            for i in staff2 :
                                fstaff2.write(f'{i}\n')
                            fstaff2.close()

                            save_list_to_file(list1_filename, list1)
                            save_list_to_file(list2_filename, list2)

                            draw_text("Order Completed!!!", main_font, "green", screen, 650, 510)  # On top of button 1
                            pygame.display.flip()
                            pygame.time.wait(1000)

                        list1_filename = './picture/order2.txt'
                        list2_filename = './picture/waitingtable.txt'

                        check_and_update_lists(list1_filename, list2_filename)
                        last_clicked_order = None
                        profit_per_order = order_profits['order2']
                        add_money(profit_per_order)
                        order_completed +=1

                    elif last_clicked_order == "order3":
                        def load_list_from_file(filename):
                            file =  open(filename, 'r') 
                            return [line.strip() for line in file.readlines()]

                        def save_list_to_file(filename, data_list):
                            file = open(filename, 'w') 
                            for item in data_list:
                                file.write(f"{item}\n")

                        def check_and_update_lists(list1_filename, list2_filename):
                            list1 = load_list_from_file(list1_filename)
                            list2 = load_list_from_file(list2_filename)

                            for item in list1:
                                list2.remove(item)

                            list1.clear()  
                            fstaff3 = open("./picture/staff.txt", "r") 
                            staff3 = [line.strip() for line in fstaff3.readlines() if line.strip()]
                            del staff3[2]
                            fstaff3 = open("./picture/staff.txt", "w")
                            for i in staff3 :
                                fstaff3.write(f'{i}\n')
                            fstaff3.close()

                            save_list_to_file(list1_filename, list1)
                            save_list_to_file(list2_filename, list2)

                            draw_text("Order Completed!!!", main_font, "green", screen, 650, 510)  # On top of button 1
                            pygame.display.flip()
                            pygame.time.wait(1000)

                        list1_filename = './picture/order3.txt'
                        list2_filename = './picture/waitingtable.txt'

                        check_and_update_lists(list1_filename, list2_filename)
                        last_clicked_order = None
                        profit_per_order = order_profits['order3']
                        add_money(profit_per_order)
                        order_completed +=1
                    
                    else :
                        draw_text("Please select a order", main_font, "red", screen, 650, 510)  # On top of button 1
                        pygame.display.flip()
                        pygame.time.wait(1000)

        waiting_table()
        pygame.display.flip()
        clock.tick(30)

def draw_popup():
    pan_default_button.update()
    steamer_button.update()
    oven_button.update()
    profilebutton.update()
    upgrade_btn.update()
    menu_button.update()
    setting_button.update()
    pygame.draw.rect(screen, (255, 201, 254), popup_rect)
    pygame.draw.rect(screen, (148, 5, 100), popup_rect, 5)  # Popup border
    
    screen.blit(coin1_img,(852, 322))
    screen.blit(coin1_img,(1023, 322))
    pan_unlock_button.update()
    steamer_unlock_button.update()
    oven_unlock_button.update()
    inputmoney_rect = pygame.Rect(740,150, 200, 33)
    pygame.draw.rect(screen, (162, 164, 164), inputmoney_rect)

    draw_text("Money: ", upgrade_font, "black", screen, 700, 170)
    draw_text(money, upgrade_font, "navyblue", screen, 836, 170)
    draw_text("Machine Types: ", upgrade_font, "black", screen, 520, 250)
    draw_text("1800", upgrade_font, "black", screen, 908, 336)
    draw_text("4000", upgrade_font, "black", screen, 1078, 336)
    draw_text("Default", upgrade_font, "black", screen, 710, 343)
    draw_text("Steamer", upgrade_font, "black", screen, 892, 358)
    draw_text("Oven", upgrade_font, "black", screen, 1073, 358)
    draw_text("Machine Features - B: Cooking process lowered to 40s", upgrade_font, "black", screen, 714, 380)
    draw_text("- C: Cooking process lowered to 30s", upgrade_font, "black", screen, 805, 408)

    close_button.update()


def draw_popup2B():
    # (width,height,x,y)
    popup2_rect = pygame.Rect(423, 430, 750, 230)
    pygame.draw.rect(screen, (243, 191, 215), popup2_rect)
    draw_text("INSTRUCTIONS: ", upgrade_font, "black", screen, 520, 449)
    draw_text("1. Do you want to unlock the steamer?", upgrade_font, "black", screen, 650, 478)

    yesB_button.update()
    noB_button.update()


def draw_popup2C():
    # (width,height,x,y)
    popup2_rect = pygame.Rect(423, 430, 750, 230)
    pygame.draw.rect(screen, (224, 248, 253), popup2_rect)
    draw_text("INSTRUCTIONS: ", upgrade_font, "black", screen, 520, 449)
    draw_text("1. Do you want to unlock the oven?", upgrade_font, "black", screen, 650, 478)

    yesC_button.update()
    noC_button.update()


def select_upgrade_steamer_unlock():
    global selected_upgradeB, message_timer
    popup2_rect = pygame.Rect(423, 430, 750, 230)
    pygame.draw.rect(screen, (243, 191, 215), popup2_rect)
    draw_text(f"Unlocked {selected_upgradeB}!", upgrade_font, "navyblue", screen, 800, 550)
    message_timer -= 1  
    if message_timer == 0:
        selected_upgradeB = False


def select_upgrade_oven_unlock():
    global selected_upgradeC, message_timer
    popup2_rect = pygame.Rect(423, 430, 750, 230)
    pygame.draw.rect(screen, (224, 248, 253), popup2_rect)
    draw_text(f"Unlocked {selected_upgradeC}!", upgrade_font, "navyblue", screen, 800, 550)
    message_timer -= 1  
    if message_timer == 0:
        selected_upgradeC = False


def draw_complete_upgrade():
    global current_upgrade, message_timer,already_upgrade, not_enough_money
    popup2_rect = pygame.Rect(423, 430, 750, 230)
    pygame.draw.rect(screen, (255, 229, 215), popup2_rect)
    draw_text(f"Congratulations, you have unlocked a {current_upgrade}!", upgrade_font, "navyblue", screen, 800, 550)
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
        select_upgrade_steamer_unlock()

    if selected_upgradeC:
        select_upgrade_oven_unlock()

    if already_upgrade:
        draw_complete_upgrade()
        
    if not_enough_money:
        less_money()


def upgrade_process():
    pan_default_button.update()
    steamer_button.update()
    oven_button.update()
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

                if steamer_unlock_button.checkForInput(pygame.mouse.get_pos()):
                    if "STEAMER" in unlocked_machine:
                        current_upgrade = "STEAMER"
                        already_upgrade = True
                        message_timer = 60
                    else:
                        if money < upgrade_costs["STEAMER"]:
                            not_enough_money = True
                            message_timer = 60
                        else:
                            show_popup2B = True
                        
                if yesB_button.checkForInput(pygame.mouse.get_pos()) and show_popup2B:
                    if "STEAMER" in unlocked_machine:
                        already_upgrade = True  # Ensure money is not deducted
                        message_timer = 60
                        show_popup2B = False
                    elif money >= upgrade_costs["STEAMER"]:
                        money -= upgrade_costs["STEAMER"]
                        unlocked_machine.add("STEAMER")
                        selected_upgradeB = "STEAMER"
                        current_upgrade = "STEAMER"
                        message_timer = 60
                        show_popup2B = False
                    else:
                        not_enough_money = True
                        message_timer = 60
                
                if oven_unlock_button.checkForInput(pygame.mouse.get_pos()):
                    if "OVEN" in unlocked_machine:
                        current_upgrade = "OVEN"
                        already_upgrade = True
                        message_timer = 60
                    else:
                        if money < upgrade_costs["OVEN"]:
                            not_enough_money = True
                            message_timer = 60
                        else:
                            show_popup2C = True
                    
                if yesC_button.checkForInput(pygame.mouse.get_pos()) and show_popup2C:
                    if "OVEN" in unlocked_machine:
                        already_upgrade = True
                        message_timer = 60
                        show_popup2C = False
                    elif money >= upgrade_costs["OVEN"]:
                        money -= upgrade_costs["OVEN"]
                        unlocked_machine.add("OVEN")
                        selected_upgradeC = "OVEN"
                        current_upgrade = "OVEN"
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
        waiting_table()
        pygame.display.update()
        clock.tick(60)

        happyhour_bar(hhactive)


def remind_unlock_popout():
    global message_timer, remind_unlock,current_upgrade
    draw_text(f"You haven't unlocked the {current_upgrade}!", food_selection_font, "red", screen, 800, 640)
    message_timer -= 1  
    if message_timer == 0:
        remind_unlock = False

machinetype_surface = pygame.Surface ((160, 60))
machinetype_button_rect1 = pygame.Rect(480, 200, 160, 50) #surface和button的vertical不一样所以会有shadow酱
machinetype_button_rect2 = pygame.Rect(480, 400, 160, 50)
machinetype_button_rect3 = pygame.Rect(480, 600, 160, 50)

font_button_machine = pygame.font.SysFont("Comic Sans MS", 21, bold=True)

ChooseMachine_text1 = font_button_machine.render(" STOVE POT", True, "white")
ChooseMachine_text_rect1 = ChooseMachine_text1.get_rect(center=(machinetype_surface.get_width()/2, machinetype_surface.get_height()/2))

ChooseMachine_text2 = font_button_machine.render(" STEAMER", True, "white")
ChooseMachine_text_rect2 = ChooseMachine_text2.get_rect(center=(machinetype_surface.get_width()/2, machinetype_surface.get_height()/2))

ChooseMachine_text3 = font_button_machine.render(" OVEN", True, "white")
ChooseMachine_text_rect3 = ChooseMachine_text3.get_rect(center=(machinetype_surface.get_width()/2, machinetype_surface.get_height()/2))



# Assume current_page starts from 1 and max_items_per_page is 3
current_page = 1
max_items_per_page = 3

total_pages = (len(food_lists) + max_items_per_page - 1) // max_items_per_page

machinetype_surface1 = pygame.Surface ((180, 50))
machinetype_button_rect1 = pygame.Rect(315, 310, 180, 40)
ChooseMachine_text1 = font_button_machine.render(" STOVE POT", True, "white")
ChooseMachine_text_rect1 = ChooseMachine_text1.get_rect(center=(machinetype_surface1.get_width()/2, machinetype_surface1.get_height()/2))

machinetype_surface2 = pygame.Surface ((180, 50))
machinetype_button_rect2 = pygame.Rect(638, 310, 180, 40)
ChooseMachine_text2 = font_button_machine.render(" STEAMER", True, "white")
ChooseMachine_text_rect2 = ChooseMachine_text2.get_rect(center=(machinetype_surface2.get_width()/2, machinetype_surface2.get_height()/2))

machinetype_surface3 = pygame.Surface ((180, 50))
machinetype_button_rect3 = pygame.Rect(960, 310, 180, 40)
ChooseMachine_text3 = font_button_machine.render(" OVEN ", True, "white")
ChooseMachine_text_rect3 = ChooseMachine_text3.get_rect(center=(machinetype_surface3.get_width()/2, machinetype_surface3.get_height()/2))


def selectfood_page2(): # after player click STOVE POT button rect
    global stovepot_food_index, current_page
     
    print(f"Initial stovepot_food_index: {stovepot_food_index}")
    while True:
        screen.blit(background, (0, 0))

        waiting_table()

        pan_default_button.update()
        steamer_button.update()
        oven_button.update()
        profilebutton.update()
        upgrade_btn.update()
        menu_button.update()
        setting_button.update() 
      

        food_selection1_rect = pygame.Rect(400, 120, 800, 600)
        food_selection2_rect = pygame.Rect(425, 195, 752, 495)
        stovepot_button_select()
        steamer_button_select()
        oven_button_select()
        pygame.draw.rect(screen, (255, 201, 254), food_selection1_rect)
        pygame.draw.rect(screen, (148, 5, 100), food_selection1_rect, 5)
        pygame.draw.rect(screen, (196, 192, 255), food_selection2_rect)

        draw_text("Food selection: ", food_selection_font, "black", screen, 550, 155)

        start_index = (current_page - 1) * max_items_per_page
        end_index = start_index + max_items_per_page
        items_on_page = food_lists[start_index:end_index]

       

        for i in range(len(items_on_page)):
            food_item = items_on_page[i]
            y_position = 216 + i * 144
            pygame.draw.rect(screen, color_pic, pygame.Rect(440, y_position, 720, 130))
            screen.blit(food_item["image"], (460, y_position + 4))
            draw_text(food_item["name"], food_title_font, "black", screen, 700, y_position + 60)
            draw_text(food_item["price"], food_title_font, "black", screen, 900, y_position + 60)

            # Define the rect for the select button
            selectprepare_button_rect = pygame.Rect(1010, y_position + 43, 130, 40)
            selectbutton_surface = pygame.Surface((130, 40))

            select_button_color = (186, 255, 184)
            if selectprepare_button_rect.collidepoint(pygame.mouse.get_pos()):
                select_button_color = (18, 255, 50)
            
            selectbutton_surface.fill(select_button_color)
        
            # Render the "SELECT" button text
            selectbutton_surface.blit(SELECT_text, text_rect)
            screen.blit(selectbutton_surface, selectprepare_button_rect.topleft)

        total_pages = (len(food_lists) + max_items_per_page - 1) // max_items_per_page
        if current_page < total_pages:
            next_btn.update()

        if current_page > 1:
            back_btn.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.checkForInput(pygame.mouse.get_pos()):
                    print("Close button clicked")
                    stovepot_food_index = -1
                    return 
                    
                if next_btn.checkForInput(pygame.mouse.get_pos()) and current_page < total_pages:
                    current_page += 1

                if back_btn.checkForInput(pygame.mouse.get_pos()) and current_page > 1:
                    current_page -= 1

                # Check if the select button is clicked
                for i in range(len(items_on_page)):
                    y_position = 216 + i * 144
                    selectprepare_button_rect = pygame.Rect(1010, y_position + 43, 130, 40)
                    if selectprepare_button_rect.collidepoint(event.pos):
                        click_sfx.play()
                        selected_food_index = start_index + i
                        print(f"Food selected index: {selected_food_index}")
                        stovepot_food_index = selected_food_index  # Update the global index
                        return stovepot_process(selected_food_index)


        money_bar()
        profilebutton.update()
        menu_button.update()
        upgrade_btn.update()
        setting_button.update()
        close_button.update()
        orderbtn.update()
        happyhour_bar(hhactive)
        pygame.display.update()
        clock.tick(60)


def selectfood_page3(): # after player click steamer
    global steamer_food_index, current_page

    print(f"Initial steamer_food_index: {steamer_food_index}")
    while True:
        screen.blit(background, (0, 0))  

        waiting_table()

        pan_default_button.update()
        steamer_button.update()
        oven_button.update()
        profilebutton.update()
        upgrade_btn.update()
        menu_button.update()
        setting_button.update()  

        
        
        food_selection1_rect = pygame.Rect(400, 120, 800, 600)
        food_selection2_rect = pygame.Rect(425, 195, 752, 495)
        stovepot_button_select()
        steamer_button_select()
        oven_button_select()
        pygame.draw.rect(screen, (255, 201, 254), food_selection1_rect)
        pygame.draw.rect(screen, (148, 5, 100), food_selection1_rect, 5)
        pygame.draw.rect(screen, (196, 192, 255), food_selection2_rect)

        draw_text("Food selection: ", food_selection_font, "black", screen, 550, 155)

        start_index = (current_page - 1) * max_items_per_page
        end_index = start_index + max_items_per_page
        items_on_page = foodlist_steamer[start_index:end_index]

        for i in range(len(items_on_page)):
            food_item = items_on_page[i]
            y_position = 216 + i * 144
            pygame.draw.rect(screen, color_pic, pygame.Rect(440, y_position, 720, 130))
            screen.blit(food_item["image"], (460, y_position + 4))
            draw_text(food_item["name"], food_title_font, "black", screen, 700, y_position + 60)
            draw_text(food_item["price"], food_title_font, "black", screen, 900, y_position + 60)

            # Define the rect for the select button
            selectprepare_button_rect = pygame.Rect(1010, y_position + 43, 130, 40)
            selectbutton_surface = pygame.Surface((130, 40))

            select_button_color =(255, 204, 159)
            if selectprepare_button_rect.collidepoint(pygame.mouse.get_pos()):
                select_button_color = (255, 129, 31)
            
            selectbutton_surface.fill(select_button_color)

            # Render the "SELECT" button text
            selectbutton_surface.blit(SELECT_text, text_rect)
            screen.blit(selectbutton_surface, selectprepare_button_rect.topleft)

        total_pages = (len(foodlist_steamer) + max_items_per_page - 1) // max_items_per_page
        if current_page < total_pages:
            next_btn.update()

        if current_page > 1:
            back_btn.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.checkForInput(pygame.mouse.get_pos()):
                   print("Close button clicked")
                   steamer_food_index = -1
                   return

                if next_btn.checkForInput(pygame.mouse.get_pos()) and current_page < total_pages:
                    current_page += 1

                if back_btn.checkForInput(pygame.mouse.get_pos()) and current_page > 1:
                    current_page -= 1

                # Check if the select button is clicked
                for i in range(len(items_on_page)):
                    y_position = 216 + i * 144
                    selectprepare_button_rect = pygame.Rect(1010, y_position + 43, 130, 40)
                    if selectprepare_button_rect.collidepoint(event.pos):
                        click_sfx.play()
                        selected_food_index = start_index + i
                        print(f"Food selected index: {selected_food_index}")
                        steamer_food_index = selected_food_index  # Update the global index
                        return steamer_process(selected_food_index)
                
 
        money_bar()
        profilebutton.update()
        menu_button.update()
        upgrade_btn.update()
        setting_button.update()
        close_button.update()
        orderbtn.update()
        happyhour_bar(hhactive)
        pygame.display.update()
        clock.tick(60)


def selectfood_page4(): # after player click oven
    global current_page, oven_food_index

    print(f"Initial oven_food_index: {oven_food_index}")
    while True:
        screen.blit(background, (0, 0)) 

        waiting_table()

        pan_default_button.update()
        steamer_button.update()
        oven_button.update()
        profilebutton.update()
        upgrade_btn.update()
        menu_button.update()
        setting_button.update()

      
       
        food_selection1_rect = pygame.Rect(400, 120, 800, 600)
        food_selection2_rect = pygame.Rect(425, 195, 752, 495)
        stovepot_button_select()
        steamer_button_select()
        oven_button_select()
        pygame.draw.rect(screen, (255, 201, 254), food_selection1_rect)
        pygame.draw.rect(screen, (148, 5, 100), food_selection1_rect, 5)
        pygame.draw.rect(screen, (196, 192, 255), food_selection2_rect)

        draw_text("Food selection: ", food_selection_font, "black", screen, 550, 155)

        start_index = (current_page - 1) * max_items_per_page
        end_index = start_index + max_items_per_page
        items_on_page = foodlist_oven[start_index:end_index]

        for i in range(len(items_on_page)):
            food_item = items_on_page[i]
            y_position = 216 + i * 144
            pygame.draw.rect(screen, color_pic, pygame.Rect(440, y_position, 720, 130))
            screen.blit(food_item["image"], (460, y_position + 4))
            draw_text(food_item["name"], food_title_font, "black", screen, 700, y_position + 60)
            draw_text(food_item["price"], food_title_font, "black", screen, 900, y_position + 60)

            # Define the rect for the select button
            selectprepare_button_rect = pygame.Rect(1010, y_position + 43, 130, 40)
            selectbutton_surface = pygame.Surface((130, 40))

            select_button_color = (255, 255, 199)
            if selectprepare_button_rect.collidepoint(pygame.mouse.get_pos()):
                select_button_color = (255, 255, 41)
            
            selectbutton_surface.fill(select_button_color)
        
            # Render the "SELECT" button text
            selectbutton_surface.blit(SELECT_text, text_rect)
            screen.blit(selectbutton_surface, selectprepare_button_rect.topleft)

        total_pages = (len(foodlist_oven) + max_items_per_page - 1) // max_items_per_page
        if current_page < total_pages:
            next_btn.update()

        if current_page > 1:
            back_btn.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.checkForInput(pygame.mouse.get_pos()):
                    print("Close button clicked")
                    oven_food_index = -1
                    return

                if next_btn.checkForInput(pygame.mouse.get_pos()) and current_page < total_pages:
                    current_page += 1

                if back_btn.checkForInput(pygame.mouse.get_pos()) and current_page > 1:
                    current_page -= 1

                # Check if the select button is clicked
                for i in range(len(items_on_page)):
                    y_position = 216 + i * 144
                    selectprepare_button_rect = pygame.Rect(1010, y_position + 43, 130, 40)
                    if selectprepare_button_rect.collidepoint(event.pos):
                        click_sfx.play()
                        selected_food_index = start_index + i
                        print(f"Food selected index: {selected_food_index}")
                        oven_food_index = selected_food_index  # Update the global index
                        return oven_process(selected_food_index)

        money_bar()
        profilebutton.update()
        menu_button.update()
        upgrade_btn.update()
        setting_button.update()
        close_button.update()
        orderbtn.update()
        happyhour_bar(hhactive)
        pygame.display.update()
        clock.tick(60)


def stovepot_button_select(): # STOVE POT button on main screen   
    machinetype_surface1 = pygame.Surface ((180, 50), pygame.SRCALPHA)
    machinetype_button_rect1 = pygame.Rect(315, 310, 180, 50)

    stovepot_button_color =  (151, 155, 213)
    if machinetype_button_rect1.collidepoint(pygame.mouse.get_pos()):
        stovepot_button_color = (21, 28, 125) 

    machinetype_surface1.fill(stovepot_button_color)

    ChooseMachine_text1 = font_button_machine.render(" STOVE POT", True, "white")
    ChooseMachine_text_rect1 = ChooseMachine_text1.get_rect(center=(machinetype_surface1.get_width()/2, machinetype_surface1.get_height()/2))
    machinetype_surface1.blit(ChooseMachine_text1, ChooseMachine_text_rect1)
    
    screen.blit( machinetype_surface1, machinetype_button_rect1.topleft)
    return machinetype_button_rect1  # Return the rect for click detection


def steamer_button_select(): # STEAMER button on main screen
    machinetype_surface2 = pygame.Surface ((180, 50),pygame.SRCALPHA)
    machinetype_button_rect2 = pygame.Rect(638, 310, 180, 50)

    steamer_button_color = (151, 155, 213)
    if machinetype_button_rect2.collidepoint(pygame.mouse.get_pos()):
        steamer_button_color = (21, 28, 125) 

    machinetype_surface2.fill(steamer_button_color)

    ChooseMachine_text2 = font_button_machine.render(" STEAMER", True, "white")
    ChooseMachine_text_rect2 = ChooseMachine_text2.get_rect(center=(machinetype_surface2.get_width()/2, machinetype_surface2.get_height()/2))
    machinetype_surface2.blit(ChooseMachine_text2, ChooseMachine_text_rect2)
    
    screen.blit( machinetype_surface2, machinetype_button_rect2.topleft)
    return machinetype_button_rect2


def oven_button_select(): # OVEN button on main screen
    machinetype_surface3 = pygame.Surface ((180, 50), pygame.SRCALPHA)
    machinetype_button_rect3 = pygame.Rect(960, 310, 180, 50)

    oven_button_color = (151, 155, 213)
    if machinetype_button_rect3.collidepoint(pygame.mouse.get_pos()):
        oven_button_color = (21, 28, 125) 

    machinetype_surface3.fill(oven_button_color)

    
    ChooseMachine_text3 = font_button_machine.render(" OVEN ", True, "white")
    ChooseMachine_text_rect3 = ChooseMachine_text3.get_rect(center=(machinetype_surface3.get_width()/2, machinetype_surface3.get_height()/2))
    machinetype_surface3.blit(ChooseMachine_text3, ChooseMachine_text_rect3)

    screen.blit( machinetype_surface3, machinetype_button_rect3.topleft)
    return machinetype_button_rect3


# Initialize process states and start times
stovepot_running = False
steamer_running = False
oven_running = False

stovepot_start_time = 0
steamer_start_time = 0
oven_start_time = 0

# Duration in seconds for each cooking process
stovepot_duration = 10
steamer_duration = 15
oven_duration = 20

# x, y, w, h, max_hp
cooking_bar_stovepot = CookingBar(330, 119, 160, 20, 100)  # x, y, w, h, max_hp
cooking_bar_steamer = CookingBar(651, 120, 160, 20, 100)
cooking_bar_oven = CookingBar(965, 119, 160, 20, 100)


def stovepot_process(selected_food_index):
    global stovepot_start_time, stovepot_running, stovepot_duration, stovepot_food_index

    # Validate the selected food index
    if selected_food_index < 0 or selected_food_index >= len(food_lists):
        print(f"Invalid food index: {selected_food_index}")
        return       # Exit if the index is invalid

    stovepot_running = True
    stovepot_start_time = time.time()
    stovepot_duration = 10 
    stovepot_food_index = selected_food_index

    # Debug statement 
    print(f"Stovepot started with food index: {stovepot_food_index}, start time: {stovepot_start_time}")

    # make sure not block the game loop
    return
      

def steamer_process(selected_food_index):
    global steamer_start_time, steamer_running, steamer_duration, steamer_food_index

    # Validate the selected food index
    if selected_food_index < 0 or selected_food_index >= len(foodlist_steamer):
        print(f"Invalid food index: {selected_food_index}")
        return         # Exit if the index is invalid

    steamer_running = True
    steamer_start_time = time.time()
    steamer_duration = 15  
    steamer_food_index = selected_food_index

    # Debug statement 
    print(f"Steamer started with food index: {steamer_food_index}, start time: {steamer_start_time}")

    return


def oven_process(selected_food_index):
    global oven_start_time, oven_running, oven_duration, oven_food_index

    # Validate the selected food index
    if selected_food_index < 0 or selected_food_index >= len(foodlist_oven):
        print(f"Invalid food index: {selected_food_index}")
        return            # Exit if the index is invalid

    oven_running = True
    oven_start_time = time.time()
    oven_duration = 20 
    oven_food_index = selected_food_index

    # Debug statement to confirm the process
    print(f"Oven started with food index: {oven_food_index}, start time: {oven_start_time}")

    return
       

def pastefood_stovepot(selected_food_index):
    global food_lists

    food_image = food_lists[selected_food_index]["image"]

    stovepot_button_color =  (255, 0, 102) 
    machinetype_surface1.fill(stovepot_button_color)

    # Resize the food image to the desired size (e.g., 100x100 pixels)
    new_food_image = pygame.transform.scale(food_image, (80, 80))
        
    # Coordinates of the dialog box
    dialog_x, dialog_y = 230, 147

    screen.blit(dialogbox_img, ( dialog_x, dialog_y))
    food_x = dialog_x + (dialogbox_img.get_width() - (new_food_image.get_width()))//2
    food_y = dialog_y + (dialogbox_img.get_height() - (new_food_image.get_height()))/2
    screen.blit(new_food_image, (food_x, food_y)) 

 
def pastefood_steamer(selected_food_index):
    global foodlist_steamer
    food_image = foodlist_steamer[selected_food_index]["image"]

    # Resize the food image to the desired size (e.g., 100x100 pixels)
    new_food_image = pygame.transform.scale(food_image, (80, 80))

    steamer_button_color =  (255, 0, 102) 
    machinetype_surface2.fill(steamer_button_color)
        
    # Coordinates of the dialog box
    dialog_x, dialog_y = 555, 147

    screen.blit(dialogbox_img, ( dialog_x, dialog_y))
    food_x = dialog_x + (dialogbox_img.get_width() - (new_food_image.get_width()))//2
    food_y = dialog_y + (dialogbox_img.get_height() - (new_food_image.get_height()))/2
    screen.blit(new_food_image, (food_x, food_y)) 

    
def pastefood_oven(selected_food_index):
    global foodlist_oven
    food_image = foodlist_oven[selected_food_index]["image"]

    # Resize the food image to the desired size (e.g., 100x100 pixels)
    new_food_image = pygame.transform.scale(food_image, (80, 80))

    oven_button_color =  (255, 0, 102) 
    machinetype_surface3.fill(oven_button_color)
        
    # Coordinates of the dialog box
    dialog_x, dialog_y = 840, 147

    screen.blit(dialogbox_img, ( dialog_x, dialog_y))
    food_x = dialog_x + (dialogbox_img.get_width() - (new_food_image.get_width()))//2
    food_y = dialog_y + (dialogbox_img.get_height() - (new_food_image.get_height()))/2
    screen.blit(new_food_image, (food_x, food_y))


def waiting_table():
    table_rect = pygame.Rect(195, 620, 1070, 140)
    table_color = (188,143,143)
    pygame.draw.rect(screen, table_color, table_rect, pygame.SRCALPHA)  


    # 6个格子在1 row (代表table width被分割六份）
    slot_width = table_rect.width // 6         # Divide the table into 6 equal slots
    slot_height = table_rect.height            # The height of each slot is the full height of the table


    # Iterate through the 6 slots to draw them
    for col in range(6):  # 6 columns for 6 slots
        slot_rect = pygame.Rect(
            table_rect.x + col * slot_width,
            table_rect.y,
            slot_width, slot_height
        )
        pygame.draw.rect(screen, (200, 200, 200), slot_rect, 3)  # Draw slot rectangles with gray borders


        if slots[col] is not None:
            food_item = slots[col]
            food_image = food_item["image"]
            new_food_image = pygame.transform.scale(food_image, (slot_width, slot_height))
            screen.blit(new_food_image, slot_rect.topleft)


slots = [None]*6

def determine_available_slots():
    index = 0
    while index < len(slots):
        if slots[index] is None:
            return index
        index +=1
    return None 


def update_slots(slot_index, food_item):    
    if slot_index is not None and 0 <= slot_index < len(slots):
        slots[slot_index] = food_item
        print(f"Slot {slot_index} updated with {food_item}")


def cooking_process():
    global stovepot_running, steamer_running, oven_running
    global stovepot_start_time, steamer_start_time, oven_start_time
    global stovepot_food_index, steamer_food_index, oven_food_index
    global machine_type, food_item, message_timer, full_slot_remind

    # Handle stovepot cooking process
    if stovepot_running:
        elapsed_time = time.time() - stovepot_start_time
        if elapsed_time >= stovepot_duration:
            stovepot_running = False
            put_food_to_slots(stovepot_food_index, "stovepot")
            stovepot_food_index = -1

        cooking_bar_stovepot.update(elapsed_time, stovepot_duration)
        cooking_bar_stovepot.draw(screen)
        pastefood_stovepot(stovepot_food_index)

    
        machinetype_surface1 = pygame.Surface((180, 50), pygame.SRCALPHA)
        stovepot_button_color = (255, 0, 128)
        machinetype_surface1.fill(stovepot_button_color)
        machinetype_surface1.blit(ChooseMachine_text1, ChooseMachine_text_rect1)
        screen.blit(machinetype_surface1, machinetype_button_rect1.topleft)

    # Handle steamer cooking process
    if steamer_running:
        elapsed_time = time.time() - steamer_start_time
        if elapsed_time >= steamer_duration:
            steamer_running = False
            put_food_to_slots(steamer_food_index, "steamer")
            steamer_food_index = -1

        cooking_bar_steamer.update(elapsed_time, steamer_duration)
        cooking_bar_steamer.draw(screen)
        pastefood_steamer(steamer_food_index)

        machinetype_surface2 = pygame.Surface((180, 50), pygame.SRCALPHA)
        steamer_button_color = (255, 0, 128)
        machinetype_surface2.fill(steamer_button_color)
        machinetype_surface2.blit(ChooseMachine_text2, ChooseMachine_text_rect2)
        screen.blit(machinetype_surface2, machinetype_button_rect2.topleft)

    # Handle oven cooking process
    if oven_running:
        elapsed_time = time.time() - oven_start_time
        if elapsed_time >= oven_duration:
            oven_running = False
            put_food_to_slots(oven_food_index, "oven")
            oven_food_index = -1

        cooking_bar_oven.update(elapsed_time, oven_duration)
        cooking_bar_oven.draw(screen)
        pastefood_oven(oven_food_index)

        machinetype_surface3 = pygame.Surface((180, 50), pygame.SRCALPHA)
        oven_button_color = (255, 0, 128)
        machinetype_surface3.fill(oven_button_color)
        machinetype_surface3.blit(ChooseMachine_text3, ChooseMachine_text_rect3)
        screen.blit(machinetype_surface3, machinetype_button_rect3.topleft)

    if full_slot_remind:
        font_slot = pygame.font.SysFont("cambria", 30, bold=True)
        draw_text("Full    slots    now !", font_slot, "red", screen, 710, 600)
        print(f"Message Timer: {message_timer}")
        message_timer -= 1
        if message_timer <= 0:
            full_slot_remind = False

def remind_no_empty_slots():
    global message_timer, full_slot_remind
    full_slot_remind = True
    message_timer = 180
    print("Reminder triggered: Full slots")


def put_food_to_slots(selected_food_index, machine_type):
    print(f"Putting food with index {selected_food_index} into slots")
    slot_index = determine_available_slots()
    if slot_index is not None:
        print(f"Available slot found at index {slot_index}")
        if machine_type == "oven":
            food_name = foodlist_oven[selected_food_index]["name"]
            food_price = foodlist_oven[selected_food_index]["price"]
            update_slots(slot_index, foodlist_oven[selected_food_index])
        elif machine_type == "stovepot":
            food_name = food_lists[selected_food_index]["name"]
            food_price = food_lists[selected_food_index]["price"]
            update_slots(slot_index, food_lists[selected_food_index])
        elif machine_type == "steamer":
            food_name = foodlist_steamer[selected_food_index]["name"]
            food_price = foodlist_steamer[selected_food_index]["price"]
            update_slots(slot_index, foodlist_steamer[selected_food_index])
        else:
            print(f"Unknown machine type: {machine_type}")
            return
        
        f = open("./picture/food-complete-name.txt", "a")
        f.write (f"{food_name}\n")
        f.close()

        f = open("./picture/food-complete-price.txt", "a")
        f.write(f"{food_price}\n")
        f.close()

    else:
        print("No available slots now")
        remind_no_empty_slots()


def main():
    global stovepot_running, steamer_running, oven_running
    global stovepot_start_time, steamer_start_time, oven_start_time
    global stovepot_food_index, steamer_food_index, oven_food_index
    global machine_type, food_item, message_timer, full_slot_remind

    print("Main loop running")

    # Initialize global variables
    stovepot_running = False
    steamer_running = False
    oven_running = False
    full_slot_remind = False
    message_timer = 0

    stovepot_start_time = 0
    steamer_start_time = 0
    oven_start_time = 0

    stovepot_food_index = -1
    steamer_food_index = -1
    oven_food_index = -1


    slot_index = None
    machine_type = None
    food_item = None

    while True:
        bg_img = pygame.image.load("./picture/lobby.jpg").convert()
        screen.blit(bg_img, (0, 0))

        money_bar()
        profilebutton.update()
        upgrade_btn.update()
        orderbtn.update()
        pan_default_button.update()
        steamer_button.update()
        oven_button.update()

        # Draw buttons for each machine
        stovepot_button_rect = stovepot_button_select()
        steamer_button_rect = steamer_button_select()
        oven_button_rect = oven_button_select()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if profilebutton.checkForInput(pygame.mouse.get_pos()):
                    profile()
                    
                if upgrade_btn.checkForInput(pygame.mouse.get_pos()): 
                    upgrade_process()

                if orderbtn.checkForInput(pygame.mouse.get_pos()): 
                    order()


                if close_button.checkForInput(pygame.mouse.get_pos()):
                    # Reset all running states and food indexes
                    print("Close button clicked")
                    print(f"Before reset: stovepot_food_index={stovepot_food_index}, steamer_food_index={steamer_food_index}, oven_food_index = {oven_food_index}")
                    stovepot_running = False
                    steamer_running = False
                    oven_running = False
                    
                    stovepot_food_index = -1
                    steamer_food_index = -1
                    oven_food_index = -1
                    print("After reset: stovepot_food_index={stovepot_food_index}, steamer_food_index={steamer_food_index}, oven_food_index={oven_food_index}")
                    
                    # Return to the main screen without any active processes
                    return

                if stovepot_button_rect.collidepoint(event.pos) and not stovepot_running:
                    click_sfx.play()
                    selectfood_page2()  # Select food from the page
                    # After selecting, ensure `stovepot_food_index` is updated before processing
                    if stovepot_food_index >= 0:
                        stovepot_process(stovepot_food_index)

                if steamer_button_rect.collidepoint(event.pos) and not steamer_running:
                    click_sfx.play()
                    selectfood_page3()  # Select food from the page
                    # After selecting, ensure `steamer_food_index` is updated before processing
                    if steamer_food_index >= 0:
                        steamer_process(steamer_food_index)

                if oven_button_rect.collidepoint(event.pos) and not oven_running:
                    click_sfx.play()
                    selectfood_page4()  # Select food from the page
                    # After selecting, ensure `oven_food_index` is updated before processing
                    if oven_food_index >= 0:
                        oven_process(oven_food_index)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    profile()

        # Call the cooking process function
        cooking_process()

        # Update other game elements
        menu_button.update()
        setting_button.update()
        orderbtn.update()
        upgrade_btn.update()
        profilebutton.update()
        happyhour_bar(hhactive)
        waiting_table()
        update_slots(slot_index, food_item)

        pygame.display.flip()
        clock.tick(60)




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
noticetext1 = "Welcome to the restaurant!\nLet us introduce the game for you ...\n\nProfile\nIt show your profile...of course.\nand also you can change your name there.\n\nMenu\nYou can prepare your food there!\n\nOrder\nYou have to check your order there.\nAfter done preparing the food,\nremember to click the complete button!"
noticetext2 = "Shop\nYou can unlock your machine there.\nBy unlocking your machine,\ndifferent food will be unlock also.\n\nSound\nYou can adjust your music sound there.\n\nHappy hour\nBy completed every 5 order,\nyou can earn double profit for 30second!\n\nWish your business is\nbooming,thriving and thriving!"



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

save_money()    
pygame.quit()
sys.exit()