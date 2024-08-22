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

##### irene_upgrade ######
money = int(input("Enter your money: "))

machine_criteria = { 
    "B": "Criteria - Cooking process speed up to 40s",
    "C": "Criteria - Cooking process speed up to 30s ",
    "D": "Criteria - Cooking process speed up to 20s", 
    "E": "Criteria - Cooking process speed up to 15s"}

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

        if lock_machineB_button.draw(screen):
            print("machineB lock")
        elif lock_machineC_button.draw(screen):
            print("machineC lock")
        elif default_machineA_button.draw(screen):
            print("Default machine")

    if show_popup2:
        pygame.draw.rect(screen,(222, 201, 235), popup2_rect)

        draw_text("INSTRUCTIONS: ", font, "black", screen, 504, 400)
        draw_text("--> Your money now can only upgrade to Machine B. ", font, "black", screen, 639, 423)
        draw_text("--> So, do you want to upgrade your current machine to machine B? ", font, "black", screen, 705, 448)
    
        yes_button.draw(screen)
        no_button.draw(screen)

    if show_popup3:
        pygame.draw.rect(screen,(201, 148, 220), popup3_rect)

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
