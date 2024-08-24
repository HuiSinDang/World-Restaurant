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

# Load the background image
background = pygame.image.load("mainBG.jpg")
background = pygame.transform.scale(background, (1400, 750))

# Load the small image
coin1_img =  pygame.image.load("coin.png")
coin1_img = pygame.transform.scale(coin1_img, (25, 25))
coin2_img =  pygame.image.load("coin.png")
coin2_img = pygame.transform.scale(coin2_img, (25, 25))

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
menu_button = Button (27, 90, "menu.png", 0.18)
![menu_button](World-Restaurant/picture/menu.png)

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

    # Draw background
    screen.blit(background, (0, 0))

    upgrade_btn.draw(screen)
    menu_button.draw(screen)

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
