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
pink = (255,182,193)
dark_pink = (170,51,106)

#login
font = pygame.font.Font('freesansbold.ttf', 50)
upgrade_font = pygame.font.Font('freesansbold.ttf', 20)
font2 = pygame.font.Font('./picture/jugnle.ttf', 50)

base_font = pygame.font.Font(None, 55)
main_font = pygame.font.SysFont("cambria", 45)
main_font1 = pygame.font.SysFont("cambria", 20)

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
redvelvet_img = pygame.transform.scale(redvelvet_img, (80, 80))

blackforest_img = pygame.image.load("./picture/blackforest.png")
blackforest_img = pygame.transform.scale(blackforest_img, (125, 100))

pandanrollcake_img = pygame.image.load("./picture/pandanrollcake.png")
pandanrollcake_img = pygame.transform.scale(pandanrollcake_img, (126, 127))

friednoodle_img = pygame.image.load("./picture/friednoodle.png")
friednoodle_img = pygame.transform.scale(friednoodle_img, (125, 115))

bihun_img = pygame.image.load("./picture/bihun.png") 
bihun_img = pygame.transform.scale(bihun_img, (120, 120))

hokkienmee_img = pygame.image.load("./picture/hokkienmee.png") 
hokkienmee_img = pygame.transform.scale(hokkienmee_img, (120, 120))

ramen_img = pygame.image.load("./picture/ramen.png") 
ramen_img = pygame.transform.scale(ramen_img, (120, 115))

udon_img = pygame.image.load("./picture/udon.png") 
udon_img = pygame.transform.scale(udon_img, (120, 120))

currymee_img = pygame.image.load("./picture/currymee.png") 
currymee_img = pygame.transform.scale(currymee_img, (120, 120))

kueyteow_img = pygame.image.load("./picture/kueyteow.png") 
kueyteow_img = pygame.transform.scale(kueyteow_img, (120, 115))

horfun_img = pygame.image.load("./picture/horfun.png") 
horfun_img = pygame.transform.scale(horfun_img, (120, 115))

mala_img = pygame.image.load("./picture/mala.png") 
mala_img = pygame.transform.scale(mala_img, (110, 115))

youtiao_img = pygame.image.load("./picture/youtiao.png")  
youtiao_img = pygame.transform.scale(youtiao_img, (100, 112))

hanjiben_img = pygame.image.load("./picture/hanjiben.png") 
hanjiben_img = pygame.transform.scale(hanjiben_img, (100, 127))

steamegg_img = pygame.image.load("./picture/steamegg.png") ##
steamegg_img = pygame.transform.scale(steamegg_img, (100, 127))

hanjiben_img = pygame.image.load("./picture/hanjiben.png") 
hanjiben_img = pygame.transform.scale(hanjiben_img, (100, 127))

lomaigai_img = pygame.image.load("./picture/lomaigai.png") 
lomaigai_img = pygame.transform.scale(lomaigai_img, (100, 127))

herbalchicken_img = pygame.image.load("./picture/herbalchicken.png") 
herbalchicken_img = pygame.transform.scale(herbalchicken_img, (100, 127))

shrimpdumpling_img = pygame.image.load("./picture/shrimpdumpling.png") 
shrimpdumpling_img = pygame.transform.scale(shrimpdumpling_img, (100, 127))

custardbun_img = pygame.image.load("./picture/custardbun.png") 
custardbun_img = pygame.transform.scale(custardbun_img, (100, 127))

dustbin_img = pygame.image.load("./picture/dustbin.png")
dustbin_img = pygame.transform.scale(dustbin_img, (200, 140))

fire_img = pygame.image.load("./picture/fire.png")
fire_img = pygame.transform.scale(fire_img, (30, 30))

soundon_btn = pygame.image.load("./picture/soundon.png")
soundon_btn = pygame.transform.scale(soundon_btn, (112, 112))
soundon_btn_rect = soundon_btn.get_rect(topleft=(18, 595))

soundoff_btn = pygame.image.load("./picture/soundoff.png")
soundoff_btn = pygame.transform.scale(soundoff_btn, (112, 112))
soundoff_btn_rect = soundoff_btn.get_rect(topleft=(18, 595))

food_lists =[
    {"image": tokbokki_img, "name": "Tokbokki", "price": "RM10.00"},

    {"image": friedrice_img, "name": "Fried Rice", "price": "RM5.00"},

    {"image": oden_img, "name": "Oden", "price": "RM18.00"},

    {"image": bibimbap_img, "name": "Bibimbap", "price": "RM8.00"},

    {"image": armystew_img, "name": "Korean Army Stew", "price": "RM68.00" },

    {"image": friednoodle_img, "name": "Fried Noodles", "price": "RM5.00"},

    {"image": bihun_img, "name": "Fried Bihuns", "price": "RM18.00"},

    {"image": hokkienmee_img, "name": "Hokkien Mee", "price": "RM6.00"},

    {"image": ramen_img, "name": "Ramen", "price": "RM8.00"},
    
    {"image": udon_img, "name": "Fried Udons", "price": "RM8.00"},

    {"image": currymee_img, "name": "Curry Mee", "price": "RM5.00"},

    {"image": kueyteow_img, "name": "Cantonese Kuey Teow", "price": "RM6.00"},

    {"image": horfun_img, "name": "Kai See Hor Fun", "price": "RM7.00"},

    {"image": mala_img, "name": "Mala Xiang Guo", "price": "RM10.00"},

    {"image": youtiao_img, "name": "Youtiao", "price": "RM4.00"},

    {"image": hanjiben_img, "name": "Hanjiben", "price": "RM2.00"},

]

foodlist_steamer = [
    {"image": steamfish_img, "name": "Thai Steamed Fish", "price": "RM50.00"},

    {"image": dimsum_img, "name": "Xiu Mai", "price": "RM8.00" },

    {"image": steamegg_img, "name": "Steamed Egg", "price": "RM6.00"},

    {"image": lomaigai_img, "name": "Lo Mai Gai", "price": "RM9.00"},

    {"image": herbalchicken_img, "name": "Herbal Chicken", "price": "RM20.00"},

    {"image": dumpling_img, "name": "Soup Dumplings", "price": "RM10.00"},

    {"image": shrimpdumpling_img, "name": "Shrimp Dumplings", "price": "RM12.00"},

    {"image": custardbun_img, "name": "Egg Custard Bun", "price": "RM8.00"},

]

foodlist_oven = [
    {"image": corndog_img, "name": "Corndogs", "price": "RM12.00"},

    {"image": kfry_img, "name": "Korean Fried Chicken", "price": "RM20.00"},

    {"image": calamari_img, "name": "Calamari Rings", "price": "RM14.00"},

    {"image": rainbowcake_img, "name": "Rainbow Cake", "price": "RM16.00"},

    {"image": redvelvet_img, "name": "Red Velvet", "price": "RM16.00"},

    {"image": blackforest_img, "name": "Black Forest", "price": "RM18.00"},

    {"image": pandanrollcake_img, "name": "Pandan Roll Cake", "price": "RM27.00"},

    {"image": mooncake_img, "name": "Mooncake", "price": "RM20.00"},

    {"image": satay_img, "name": "Satay", "price": "RM10.00" }

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
    
class ImageButton:
    def __init__(self,image,x,y,action):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
        self.action = action

    def draw(self,screen):
        if self.image:
            screen.blit(self.image,self.rect)

    def is_clicked(self,pos):
        return self.rect.collidepoint(pos)
    
    def press(self):
        self.action()


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
    
class Deliveryman(pygame.sprite.Sprite):
    def __init__(self, target_x, deliveryman_type, speed=5, image_size=(250, 250)):
        super().__init__()
        self.deliveryman_type = deliveryman_type  # 保存 deliveryman_type 为实例属性

        # 加载不同的外卖员图片
        if deliveryman_type == 1:
            self.image = pygame.image.load("./picture/dm1.png")
        elif deliveryman_type == 2:
            self.image = pygame.image.load("./picture/dm2.png")
        elif deliveryman_type == 3:
            self.image = pygame.image.load("./picture/dm3.png")
        
        self.image = pygame.transform.scale(self.image, image_size)
        self.original_image = self.image  # 保存原始图像，用于翻转回来
        self.rect = self.image.get_rect()
        self.rect.x = screen_width  # 从右边进入屏幕
        self.rect.y = 400
        self.speed = speed
        self.target_x = target_x
        self.direction = -1  # 初始向左移动
        self.wait_time = 0  # 停留时间计时器
        self.finished = False  # 是否走完的标志
        self.reflected = False  # 是否已经反转过图像

    def update(self):
        # 外卖员向左移动到目标位置
        if self.direction == -1 and self.rect.x > self.target_x:
            self.rect.x -= self.speed
        # 到达目标位置后停留3秒，并翻转图片
        elif self.rect.x <= self.target_x and self.wait_time == 0:
            self.wait_time = pygame.time.get_ticks()  # 开始计时
            if not self.reflected:
                self.image = pygame.transform.flip(self.image, True, False)  # 水平翻转
                self.reflected = True  # 标记为已经反转
        # 停留3秒后，开始回走
        elif pygame.time.get_ticks() - self.wait_time > 1000 and self.direction == -1:
            self.direction = 1  # 转身，开始向右回走
            # 在开始回走的时候删除文件中的数据
            update_file_after_removal("./picture/foodrak.txt", self.deliveryman_type)
        # 回走到屏幕右侧时再次反转图片
        elif self.direction == 1 and self.rect.x < screen_width:
            self.rect.x += self.speed
        # 当外卖员完全走出屏幕时，设置为已完成并恢复图片
        elif self.rect.x >= screen_width:
            if self.reflected:  # 走出屏幕后恢复图像方向
                self.image = pygame.transform.flip(self.image, True, False)
                self.reflected = False
            self.finished = True
    
def read_file_and_get_list(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()

    if not content:
        return []

    content_list = [line for line in content.split('\n') if line.strip()]
    content = ','.join(content_list)
    result = list(map(int, content.split(',')))
    return result

    
# 更新文件，删除已完成的外卖员类型
def update_file_after_removal(filename, completed_type):
    positions = read_file_and_get_list(filename)
    if completed_type in positions:
        positions.remove(completed_type)  # 从列表中移除已完成的外卖员类型
    with open(filename, 'w') as f:
        f.write(','.join(map(str, positions)))

# 动态检查文件更新并生成新的外卖员
def update_deliverymen(existing_positions, deliverymen_group, filename):
    new_positions = read_file_and_get_list(filename)

    # 只处理新增的外卖员类型
    if len(new_positions) > len(existing_positions):
        new_elements = new_positions[len(existing_positions):]

        # 创建新的外卖员实例
        for i, deliveryman_type in enumerate(new_elements):
            target_x = 250 + (len(existing_positions) + i) * 300  # 每个外卖员的目标点依次增加
            deliveryman = Deliveryman(target_x=target_x, deliveryman_type=deliveryman_type)
            deliverymen_group.add(deliveryman)

        existing_positions.extend(new_elements)

    return existing_positions


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
resetbutton_surface = pygame.transform.scale(resetbutton_surface, (250, 60))
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
order1button_surface = pygame.transform.scale(order1button_surface, (270, 270))
order1button = Button(order1button_surface, 350, 350,"")

order2button_surface = pygame.image.load("./picture/order.png")
order2button_surface = pygame.transform.scale(order2button_surface, (270, 270))
order2button = Button(order2button_surface, 650, 350,"")

order3button_surface = pygame.image.load("./picture/order.png")
order3button_surface = pygame.transform.scale(order3button_surface, (270, 270))
order3button = Button(order3button_surface, 950, 350,"")

completebutton_surface = pygame.image.load("./picture/reset_btn.png")
completebutton_surface = pygame.transform.scale(completebutton_surface, (250, 60))
completebutton = Button(completebutton_surface, 600, 575,"Complete")

man1_surface = pygame.image.load("./picture/man.png")
man1_surface = pygame.transform.scale(man1_surface, (50, 50))
man1 = Button(man1_surface, 275, 435,"")

man2_surface = pygame.image.load("./picture/man.png")
man2_surface = pygame.transform.scale(man2_surface, (50, 50))
man2 = Button(man2_surface, 570, 435,"")

man3_surface = pygame.image.load("./picture/man.png")
man3_surface = pygame.transform.scale(man3_surface, (50, 50))
man3 = Button(man3_surface, 875, 435,"")

chick1_surface = pygame.image.load("./picture/chick.png")
chick1_surface = pygame.transform.scale(chick1_surface, (50, 50))
chick1 = Button(chick1_surface, 275, 435,"")

chick2_surface = pygame.image.load("./picture/chick.png")
chick2_surface = pygame.transform.scale(chick2_surface, (50, 50))
chick2 = Button(chick2_surface, 575, 435,"")

chick3_surface = pygame.image.load("./picture/chick.png")
chick3_surface = pygame.transform.scale(chick3_surface, (50, 50))
chick3 = Button(chick3_surface, 875, 435,"")

robot1_surface = pygame.image.load("./picture/robot.png")
robot1_surface = pygame.transform.scale(robot1_surface, (50, 50))
robot1 = Button(robot1_surface, 275, 435,"")

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
frame1 = Button(frame1_surface, 355, 350,"")

frame2_surface = pygame.image.load("./picture/frame.png")
frame2_surface = pygame.transform.scale(frame2_surface, (295, 295))
frame2 = Button(frame2_surface, 655, 350,"")

frame3_surface = pygame.image.load("./picture/frame.png")
frame3_surface = pygame.transform.scale(frame3_surface, (295, 295))
frame3 = Button(frame3_surface, 955, 350,"")

food_prices = {
    "Tokbokki": 10,
    "Fried Rice": 5,
    "Oden": 18,
    "Bibimbap": 8,
    "Korean Army Stew" :68,
    "Fried Noodles" : 5,
    "Fried Bihuns": 6,
    "Hokkien Mee": 6,
    "Ramen": 8,
    "Fried Udons": 8,
    "Curry Mee": 5,
    "Cantonese Kuey Teow": 6,
    "Kai See Hor Fun": 7,
    "Mala Xiang Guo": 10,
    "Youtiao" : 4,
    "Hanjiben": 2,
    "Thai Steamed Fish": 50,
    "Xiu Mai" : 8,
    "Steamed Egg": 6,
    "Lo Mai Gai": 9,
    "Herbal Chicken": 20,
    "Soup Dumplings": 10,
    "Shrimp Dumplings" :12,
    "Egg Custard Bun": 12,
    "Corndogs" :12,
    "Korean Fried Chicken" : 20,
    "Calamari Rings" :14,
    "Rainbow Cake": 16,
    "Red Velvet" : 16,
    "Black Forest": 18,
    "Pandan Roll Cake": 27,
    "Mooncake": 20,
    "Satay": 10
}

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
unlocked_machine = set() # Set to track unlocked machines
remind_unlock = False
stovepot_call = False
steamer_call = False
oven_call = False

#money#
money_amount = 100
max_display_money = 1000000
money_file_path = os.path.join(os.getcwd(),"./picture/money.txt")
moneybox = pygame.image.load('./picture/moneybox.png')
moneybox = pygame.transform.scale(moneybox,(295,85))

def show_money():
    if os.path.exists(money_file_path):
        try:
            with open("./picture/money.txt","r")as file:
                return int(file.read())
        except (ValueError,IOError):
            return 100
    else:
        return 100
    
def save_money():
    with open("./picture/money.txt","w") as file:
        file.write(str(money_amount))

def show_message(message,position=(900,200)):
    message_font = pygame.font.Font('./picture/jugnle.ttf', 35)
    message_text = message_font.render(message,True,(255,0,0))
    text_rect = message_text.get_rect(center=(750,375))
    screen.blit(message_text,text_rect)
    pygame.display.update()
    pygame.time.delay(1500)

def money_bar():
    money_bar_rect = pygame.Rect(1100, 10, 200, 100)
    screen.blit(moneybox,money_bar_rect.topleft)
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
        save_money()
        return True
    else:
        show_message("Not enough money!")
        return False
    
money_amount = show_money()

#happy hour
order_completed = 0
hhactive = False
hhtime = 30
hh_start_time = None
hh_file_path = os.path.join(os.getcwd(),"./picture/happyhour.txt")

def show_order_completed():
    if os.path.exists(hh_file_path):
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

def add_order():
    global order_completed
    order_completed += 1
    save_order()
    update_happy_hour_status()

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

#menu-unlock food
def load_image(path,size):
    try:
        image = pygame.image.load(path)
        return pygame.transform.scale(image,size)
    except pygame.error as e:
        return None
    
menupage = load_image('./picture/menupage.png',(900,800))
nextbutton = load_image('./picture/nextbutton.png',(35,35))
previousbutton = load_image('./picture/previousbutton.png',(35,35))
closebutton = load_image('./picture/closebutton.png',(40,40))

def load_font(path,size):
    try:
        return pygame.font.Font(path,size)
    except FileNotFoundError as e:
        return pygame.font.Font(None,size)
    
font3 = load_font('./picture/jugnle.ttf', 20)

def save_unlocked_food():
    with open('./picture/unlocked_food.txt','w')as f:
        for button in buttons_page1 + buttons_page2 + buttons_page3 + buttons_page4 + buttons_page5 + buttons_page6:
            f.write(f"{button.foodname}:{button.pressed}\n")

def load_unlocked_food():
    unlocked_food = {"Tokbokki","Oden","Fried Rice"}
    try:
        with open('./picture/unlocked_food.txt','r')as f:
            lines = f.readlines()
            for line in lines:
                foodname,pressed = line.strip().split(':')
                if pressed == 'True':
                    unlocked_food.add(foodname)
    except FileNotFoundError:
        pass
    for button in buttons_page1 + buttons_page2 + buttons_page3 + buttons_page4 + buttons_page5 + buttons_page6:
        if button.foodname in unlocked_food:
            button.pressed = True
        else:
            button.pressed = False

class Button:
    def __init__(self,foodname,button_text,x,y,width,height,action,label_text,image_path=None,image_size=(50,50),cost=20):
        self.rect = pygame.Rect(x,y,width,height)
        self.foodname = foodname
        self.button_text = button_text
        self.action = action
        self.pressed = False
        self.label_text = label_text
        self.label_lines = []
        self.image = None
        self.image_rect = None
        self.cost = cost
        self.update_text(self.button_text)
        if self.label_text:
            self.update_label()
        if image_path:
            self.load_image(image_path,image_size)

    def update_text(self,new_text):
        self.text_surface = font3.render(new_text,True,black)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def update_label(self):
        if self.label_text:
            lines = self.label_text.split('\n')
            self.label_lines = [font3.render(line,True,black)for line in lines]

    def load_image(self,image_path,size):
        try:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image,size)
            self.image_rect = self.image.get_rect(center=(self.rect.centerx,self.rect.top -70))
        except pygame.error as e:
            pass

    def draw(self,screen):
        if self.image:
            self.image_rect.centerx = self.rect.centerx
            self.image_rect.bottom = self.rect.top - 60
            screen.blit(self.image,self.image_rect)
        if self.label_lines:
            label_y_position = self.image_rect.bottom + 10 if self.image else self.rect.top - 70
            line_height = font3.get_height()
            for i, line_surface in enumerate(self.label_lines):
                line_rect = line_surface.get_rect(center=(self.rect.centerx,label_y_position + i * line_height))
                screen.blit(line_surface,line_rect)

        color =  dark_pink if self.pressed else pink
        pygame.draw.rect(screen,color,self.rect)
        display_text = "Unlocked" if self.pressed else self.button_text
        self.update_text(display_text)
        screen.blit(self.text_surface,self.text_rect)

    def is_clicked(self,pos):
        return self.rect.collidepoint(pos)

    def press(self):
        if not self.pressed:
            if subtract_money(self.cost):
                self.pressed = True
                self.action()
                save_money()
                save_unlocked_food()
                return True
            else:
                return False

buttons_page1 = [
    Button("Tokbokki","Unlock",575,225,125,40,lambda:unlock_item(1),label_text="Tokbokki\nRM 20",image_path='./picture/tokbokki.png',cost=20),
    Button("Fried Rice","Unlock",780,225,125,40,lambda:unlock_item(2),label_text="Fried Rice\nRM 20",image_path='./picture/friedrice.png',cost=20),
    Button("Oden","Unlock",575,425,125,40,lambda:unlock_item(3),label_text="Oden\nRM 20",image_path='./picture/oden.png',cost=20),
    Button("Bibimbap","Unlock",780,425,125,40,lambda:unlock_item(4),label_text="Bibimbap\nRM 20",image_path='./picture/bibimbap.png',cost=20),
    Button("Korean Army Stew","Unlock",575,625,125,40,lambda:unlock_item(5),label_text="Korean Army Stew\nRM 20",image_path='./picture/armystew.png',cost=20),
    Button("Fried Noodles","Unlock",780,625,125,40,lambda:unlock_item(6),label_text="Fried Noodles\nRM 20",image_path='./picture/friednoodle.png',cost=20),
]

buttons_page2 =[
    Button("Fried Bihuns","Unlock",575,225,125,40,lambda:unlock_item(7),label_text="Fried Bihuns\nRM 20",image_path='./picture/oden.png',cost=20),
    Button("Hokkien Mee","Unlock",780,225,125,40,lambda:unlock_item(8),label_text="Hokkien Mee\nRM 20",image_path='./picture/hokkienmee.png',cost=20),
    Button("Ramen","Unlock",575,425,125,40,lambda:unlock_item(9),label_text="Ramen\nRM 20",image_path='./picture/ramen.png',cost=20),
    Button("Fried Udons","Unlock",780,425,125,40,lambda:unlock_item(10),label_text="Fried Udons\nRM 20",image_path='./picture/udon.png',cost=20),
    Button("Curry Mee","Unlock",575,625,125,40,lambda:unlock_item(11),label_text="Curry Mee\nRM 20",image_path='./picture/currymee.png',cost=20),
    Button("Cantonese Kuey Teow","Unlock",780,625,125,40,lambda:unlock_item(12),label_text="Cantonese Kuey Teow\nRM 20",image_path='./picture/kueyteow.png',cost=20),
]

buttons_page3 =[
    Button("Kai See Hor Fun","Unlock",575,225,125,40,lambda:unlock_item(13),label_text="Kai See Hor Fun\nRM 20",image_path='./picture/horfun.png',cost=20),
    Button("Mala Xiang Guo","Unlock",780,225,125,40,lambda:unlock_item(14),label_text="Mala Xiang Guo\nRM 20",image_path='./picture/mala.png',cost=20),
    Button("Youtiao","Unlock",575,425,125,40,lambda:unlock_item(15),label_text="Youtiao\nRM 20",image_path='./picture/youtiao.png',cost=20),
    Button("Hanjiben","Unlock",780,425,125,40,lambda:unlock_item(16),label_text="Hanjiben\nRM 20",image_path='./picture/hanjiben.png',cost=20),
    Button("Thai Steamed Fish","Unlock",575,625,125,40,lambda:unlock_item(17),label_text="Thai Steamed Fish\nRM 20",image_path='./picture/steamfish.png',cost=20),
    Button("Xiu Mai","Unlock",780,625,125,40,lambda:unlock_item(18),label_text="Xiu Mai\nRM 20",image_path='./picture/oden.png',cost=20),
]

buttons_page4 =[
    Button("Steamed Egg","Unlock",575,225,125,40,lambda:unlock_item(19),label_text="Steamed Egg\nRM 20",image_path='./picture/steamegg.png',cost=20),
    Button("Lo Mai Gai","Unlock",780,225,125,40,lambda:unlock_item(20),label_text="Lo Mai Gai\nRM 20",image_path='./picture/lomaigai.png',cost=20),
    Button("Herbal Chicken","Unlock",575,425,125,40,lambda:unlock_item(21),label_text="Herbal Chicken\nRM 20",image_path='./picture/herbalchicken.png',cost=20),
    Button("Soup Dumplings","Unlock",780,425,125,40,lambda:unlock_item(22),label_text="Soup Dumplings\nRM 20",image_path='./picture/dumpling.png',cost=20),
    Button("Shrimp Dumplings","Unlock",575,625,125,40,lambda:unlock_item(23),label_text="Shrimp Dumplings\nRM 20",image_path='./picture/shrimpdumpling.png',cost=20),
    Button("Egg Custard Bun","Unlock",780,625,125,40,lambda:unlock_item(24),label_text="Egg Custard Bun\nRM 20",image_path='./picture/custardbun.png',cost=20),
]

buttons_page5 =[
    Button("Corndogs","Unlock",575,225,125,40,lambda:unlock_item(25),label_text="Corndogs\nRM 20",image_path='./picture/corndog.png',cost=20),
    Button("Korean Fried Chicken","Unlock",780,225,125,40,lambda:unlock_item(26),label_text="Korean Fried Chicken\nRM 20",image_path='./picture/kfry.png',cost=20),
    Button("Calamari Rings","Unlock",575,425,125,40,lambda:unlock_item(27),label_text="Calamari Rings\nRM 20",image_path='./picture/calamari.png',cost=20),
    Button("Rainbow Cake","Unlock",780,425,125,40,lambda:unlock_item(28),label_text="Rainbow Cake\nRM 20",image_path='./picture/rainbowcake.png',cost=20),
    Button("Red Velvet","Unlock",575,625,125,40,lambda:unlock_item(29),label_text="Red Velvet\nRM 20",image_path='./picture/redvelvet.png',cost=20),
    Button("Black Forest","Unlock",780,625,125,40,lambda:unlock_item(30),label_text="Black Forest\nRM 20",image_path='./picture/blackforest.png',cost=20),
]

buttons_page6 =[
    Button("Pandan Roll Cake","Unlock",575,225,125,40,lambda:unlock_item(31),label_text="Pandan Roll Cake\nRM 20",image_path='./picture/pandanrollcake.png',cost=20),
    Button("Cookies","Unlock",780,225,125,40,lambda:unlock_item(32),label_text="Cookies\nRM 20",image_path='./picture/oden.png',cost=20),
    Button("Mooncake","Unlock",575,425,125,40,lambda:unlock_item(33),label_text="Mooncake\nRM 20",image_path='./picture/mooncake.png',cost=20),
    Button("Satay","Unlock",780,425,125,40,lambda:unlock_item(34),label_text="Satay\nRM 20",image_path='./picture/satay.png',cost=20),
]


button_mapping_page1 = {
    1: buttons_page1[0],
    2: buttons_page1[1],
    3: buttons_page1[2],
    4: buttons_page1[3],
    5: buttons_page1[4],
    6: buttons_page1[5],
}

button_mapping_page2 = {
    7: buttons_page2[0],
    8: buttons_page2[1],
    9: buttons_page2[2],
    10: buttons_page2[3],
    11: buttons_page2[4],
    12: buttons_page2[5],
}

button_mapping_page3 = {
    13: buttons_page3[0],
    14: buttons_page3[1],
    15: buttons_page3[2],
    16: buttons_page3[3],
    17: buttons_page3[4],
    18: buttons_page3[5],
}

button_mapping_page4 = {
    19: buttons_page4[0],
    20: buttons_page4[1],
    21: buttons_page4[2],
    22: buttons_page4[3],
    23: buttons_page4[4],
    24: buttons_page4[5],
}

button_mapping_page5 = {
    25: buttons_page5[0],
    26: buttons_page5[1],
    27: buttons_page5[2],
    28: buttons_page5[3],
    29: buttons_page5[4],
    30: buttons_page5[5],
}

button_mapping_page6 = {
    31: buttons_page6[0],
    32: buttons_page6[1],
    33: buttons_page6[2],
    34: buttons_page6[3],
}

def unlock_item(item_id):
    button = None
    if 1 <= item_id <= 6:
        button = button_mapping_page1.get(item_id)
    elif 7 <= item_id <= 12:
        button = button_mapping_page2.get(item_id)
    elif 13 <= item_id <= 18:
        button = button_mapping_page3.get(item_id)
    elif 19 <= item_id <= 24:
        button = button_mapping_page4.get(item_id)
    elif 25 <= item_id <= 30:
        button = button_mapping_page5.get(item_id)
    elif 31 <= item_id <= 34:
        button = button_mapping_page6.get(item_id)
    if button and not button.pressed:
        button.press()

current_page = 1
buttons = buttons_page1

def display_message(screen,message,position,color=(255,0,0)):
    text_surface=font3.render(message,True,color)
    screen.blit(text_surface,position)



def change_page(forward=True):
    global current_page,buttons
    if forward:
        if current_page == 1:
            current_page = 2
            buttons = buttons_page2
        elif current_page == 2:
            current_page = 3
            buttons = buttons_page3
        elif current_page == 3:
            current_page = 4
            buttons = buttons_page4
        elif current_page == 4:
            current_page = 5
            buttons = buttons_page5
        elif current_page == 5:
            current_page = 6
            buttons = buttons_page6
        else:
            current_page = 1
            buttons = buttons_page1
    else:
        if current_page == 6:
            current_page = 5
            buttons = buttons_page5
        elif current_page == 5:
            current_page = 4
            buttons = buttons_page4
        elif current_page == 4:
            current_page = 3
            buttons = buttons_page3
        elif current_page == 3:
            current_page = 2
            buttons = buttons_page2
        elif current_page == 2:
            current_page = 1
            buttons = buttons_page1
        else:
            current_page = 6
            buttons = buttons_page6

def close_menu():  #yv
    global running
    running = False

nextpbutton = ImageButton(nextbutton,925,625,change_page)
previouspbutton = ImageButton(previousbutton,500,625,lambda:change_page(forward=False))
closepbutton = ImageButton(closebutton,925,100,close_menu)

def show_menupage():
    global current_page,buttons,running
    running = True
    load_unlocked_food()
    
    while running:
        if current_page == 1:
            screen.blit(menupage,(275,20))
            buttons = buttons_page1
        elif current_page == 2:
            screen.blit(menupage,(275,20))
            buttons = buttons_page2
        elif current_page == 3:
            screen.blit(menupage,(275,20))
            buttons = buttons_page3
        elif current_page == 4:
            screen.blit(menupage,(275,20))
            buttons = buttons_page4
        elif current_page == 5:
            screen.blit(menupage,(275,20))
            buttons = buttons_page5
        elif current_page == 6:
            screen.blit(menupage,(275,20))
            buttons = buttons_page6

        for button in buttons:
            button.draw(screen)
        if current_page > 1:
            previouspbutton.draw(screen)
        if current_page < 6:
            nextpbutton.draw(screen)
        closepbutton.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nextpbutton.is_clicked(event.pos):
                    click_sfx.play()
                    nextpbutton.press()
                elif previouspbutton.is_clicked(event.pos):
                    click_sfx.play() 
                    previouspbutton.press()
                elif closepbutton.is_clicked(event.pos):
                    click_sfx.play()
                    closepbutton.press()
                for button in buttons:
                    if button.is_clicked(event.pos):
                        click_sfx.play()
                        button.press()
        
        if sound_muted:
            screen.blit(soundoff_btn, soundoff_btn_rect.topleft)
        else:
            screen.blit(soundon_btn, soundon_btn_rect.topleft)

        pygame.display.flip()
        pygame.time.Clock().tick(30)


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

def pinky_closebutton(): #hs
    global running
    running = False

button = load_image('./picture/close_windowBtn.png',(60,60))
button = ImageButton(button, 1065, 130, pinky_closebutton)

def profile():
    global running
    running = True

    while running:
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
                totalmoney = [int(i) for i in y.read().split("\n") if i.strip()]
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
                totalmoney = [int(i) for i in y.read().split("\n") if i.strip()]
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
                if button.is_clicked(event.pos):
                    click_sfx.play()
                    button.press()
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

        if sound_muted:
            screen.blit(soundoff_btn, soundoff_btn_rect.topleft)  
        else:
            screen.blit(soundon_btn, soundon_btn_rect.topleft) 

        button.draw(screen)
        resetbutton.update()
        pygame.display.flip()
        clock.tick(30)

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
    global person_x, person_y, person_speed, moving, returning, flipped
    global running
    running = True
    last_clicked_order = None
    
    while running:
        screen.blit(surface,screen_rect1)
        button.draw(screen)
        
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
            fwaitingtable1 = open("./picture/food-complete-name.txt", "r") 
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
                    draw_text(f1, main_font, color, screen, 360, y_offset)  # On top of button 1
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

                    if len(f1) > int(10):
                        font_to_use1 = main_font1
                    else :
                        font_to_use1 = main_font

                    draw_text(f1, font_to_use1, color, screen, 360, y_offset)  # On top of button 1
                    y_offset += 50
                ffood1.close()

                fmoney1 = open("./picture/order1.txt","r")
                ordered_items1 = [line.strip() for line in fmoney1.readlines() if line.strip()]

                total_price1 = 0 
                for item in ordered_items1:
                    if item in food_prices:
                        total_price1 += food_prices[item]

                draw_text(total_price1, main_font, "black", screen, 360, 440)  # On top of button 1
                fmoney1.close()
        else:
            ffood1 = open(path1, "x") 
            ffood1 = open(path1, "r") 
            order1 = [line.strip() for line in ffood1.readlines() if line.strip()]
            ffood1 = open(path1, "a")     
            y_offset = 275
            nofood = random.randint(1, 3)
            fwaitingtable1 = open("./picture/food-complete-name.txt", "r") 
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
                draw_text(f1, main_font, color, screen, 360, y_offset)  # On top of button 1
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
            fwaitingtable2 = open("./picture/food-complete-name.txt", "r") 
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
                    draw_text(f2, main_font, color, screen, 660, y_offset)  # On top of button 2
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

                    if len(f2) > int(10):
                        font_to_use2 = main_font1
                    else :
                        font_to_use2 = main_font

                    draw_text(f2, font_to_use2, color, screen, 660, y_offset)  # On top of button 2
                    y_offset += 50
                ffood2.close()

                fmoney2 = open("./picture/order2.txt","r")
                ordered_items2 = [line.strip() for line in fmoney2.readlines() if line.strip()]

                total_price2 = 0 
                for item in ordered_items2:
                    if item in food_prices:
                        total_price2 += food_prices[item]

                draw_text(total_price2, main_font, "black", screen, 660, 440)  # On top of button 1
                fmoney2.close()

        else:
            ffood2 = open(path2, "x") 
            ffood2 = open(path2, "r") 
            order2 = [line.strip() for line in ffood2.readlines() if line.strip()]
            ffood2 = open(path2, "a")     
            y_offset = 275
            nofood = random.randint(1, 3)
            fwaitingtable2 = open("./picture/food-complete-name.txt", "r") 
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
                draw_text(f2, main_font, color, screen, 660, y_offset)  # On top of button 2
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
            fwaitingtable3 = open("./picture/food-complete-name.txt", "r") 
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
                    draw_text(f3, main_font, color, screen, 960, y_offset)  # On top of button 3
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

                    if len(f3) > int(10):
                        font_to_use3 = main_font1
                    else :
                        font_to_use3 = main_font
                    draw_text(f3, font_to_use3, color, screen, 960, y_offset)  # On top of button 3
                    y_offset += 50
                ffood3.close()

                fmoney3 = open("./picture/order3.txt","r")
                ordered_items3 = [line.strip() for line in fmoney3.readlines() if line.strip()]

                total_price3 = 0 
                for item in ordered_items3:
                    if item in food_prices:
                        total_price3 += food_prices[item]

                draw_text(total_price3, main_font, "black", screen, 960, 440)  # On top of button 1
                fmoney3.close()

        else:
            ffood3 = open(path3, "x") 
            ffood3 = open(path3, "r") 
            order3 = [line.strip() for line in ffood3.readlines() if line.strip()]
            ffood3 = open(path3, "a")     
            y_offset = 275
            nofood = random.randint(1, 3)
            fwaitingtable3 = open("./picture/food-complete-name.txt", "r") 
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
                draw_text(f3, main_font, color, screen, 960, y_offset)  # On top of button 3
                y_offset += 50
            ffood3.close()
        
        if last_clicked_order == "order1":
            frame1.update()
        elif last_clicked_order == "order2" :
            frame2.update()
        elif last_clicked_order == "order3" :
            frame3.update()

        pathtotal1 = './picture/totalearned.txt'
        check_file11 = os.path.isfile(pathtotal1)
        if check_file11 == True:
            ftotal = open("./picture/totalearned.txt", "a")
        else:
            ftotal = open("./picture/totalearned.txt","x")
            check_file11 == True

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event.pos):
                    click_sfx.play()
                    button.press()
                if profilebutton.checkForInput(pygame.mouse.get_pos()):
                    profile()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    profile()
                if event.key == pygame.K_ESCAPE:
                    main()


            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if soundon_btn_rect.collidepoint(event.pos) or soundoff_btn_rect.collidepoint(event.pos):
                    mute_sound()

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
                    
                    ffoodrak = open("./picture/foodrak.txt", "r")
                    foodrak = [line.strip() for line in ffoodrak.readlines()]
                    ffoodrak.close()

                    if len(foodrak) < 3:
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
                                ffoodrak = open("./picture/foodrak.txt", "a")
                                ffoodrak.write(f'{staff1[0]}\n')
                                del staff1[0]
                                fstaff1 = open("./picture/staff.txt", "w")
                                for i in staff1 :
                                    fstaff1.write(f'{i}\n')
                                fstaff1.close()

                                save_list_to_file(list1_filename, list1)
                                save_list_to_file(list2_filename, list2)
                                
                                profit = int(total_price1)
                                if hhactive:
                                    add_money(total_price1 * 2)
                                else:
                                    add_money(total_price1)
                                ftotal.write(f'{profit}\n')
                                ftotal.close
                                add_order()

                                draw_text("Order Completed!!!", main_font, "green", screen, 650, 510)  # On top of button 1
                                pygame.display.flip()
                                pygame.time.wait(1000)

                            list1_filename = './picture/order1.txt'
                            list2_filename = './picture/food-complete-name.txt'

                            check_and_update_lists(list1_filename, list2_filename)
                            last_clicked_order = None

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
                                ffoodrak = open("./picture/foodrak.txt", "a")
                                ffoodrak.write(f'{staff2[1]}\n')
                                del staff2[1]
                                fstaff2 = open("./picture/staff.txt", "w")
                                for i in staff2 :
                                    fstaff2.write(f'{i}\n')
                                fstaff2.close()

                                save_list_to_file(list1_filename, list1)
                                save_list_to_file(list2_filename, list2)
                                
                                profit = int(total_price2)
                                if hhactive:
                                    add_money(total_price2 * 2)
                                else:
                                    add_money(total_price2)
                                ftotal.write(f'{profit}\n')
                                ftotal.close
                                add_order()

                                draw_text("Order Completed!!!", main_font, "green", screen, 650, 510)  # On top of button 1
                                pygame.display.flip()
                                pygame.time.wait(1000)

                            list1_filename = './picture/order2.txt'
                            list2_filename = './picture/food-complete-name.txt'

                            check_and_update_lists(list1_filename, list2_filename)
                            last_clicked_order = None

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
                                ffoodrak = open("./picture/foodrak.txt", "a")
                                ffoodrak.write(f'{staff3[2]}\n')
                                del staff3[2]
                                fstaff3 = open("./picture/staff.txt", "w")
                                for i in staff3 :
                                    fstaff3.write(f'{i}\n')
                                fstaff3.close()

                                save_list_to_file(list1_filename, list1)
                                save_list_to_file(list2_filename, list2)
                                
                                profit = int(total_price3)
                                if hhactive:
                                    add_money(total_price3 * 2)
                                else:
                                    add_money(total_price3)
                                ftotal.write(f'{profit}\n')
                                ftotal.close
                                add_order()

                                draw_text("Order Completed!!!", main_font, "green", screen, 650, 510)  # On top of button 1
                                pygame.display.flip()
                                pygame.time.wait(1000)

                            list1_filename = './picture/order3.txt'
                            list2_filename = './picture/food-complete-name.txt'

                            check_and_update_lists(list1_filename, list2_filename)
                            last_clicked_order = None
                    
                        
                        else :
                            draw_text("Please select an order", main_font, "red", screen, 650, 510)  # On top of button 1
                            pygame.display.flip()
                            pygame.time.wait(1000)
                    
                    elif len(foodrak) == 3:

                        for i in range(min(3, len(foodrak))):
                            if foodrak[i] == "":

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

                                        # 读取文件内容，保留空行
                                        ffoodrak =  open("./picture/foodrak.txt", "r")
                                        foodrak = [line.rstrip('\n') for line in ffoodrak.readlines()]  # 只去掉换行符，保留空行
                                            
                                        # 检查前三个元素是否有空位，并填入数据
                                        for i in range(min(3, len(foodrak))):
                                            if foodrak[i] == "":  # 找到空行
                                                foodrak[i] = staff1[0]  # 用 staff1[0] 填充空位
                                                
                                                # 写入更新后的内容到文件
                                                ffoodrak =  open("./picture/foodrak.txt", "w")
                                                for item in foodrak:
                                                        ffoodrak.write(f"{item}\n")  # 确保数据按行写入

                                        del staff1[0]
                                        fstaff1 = open("./picture/staff.txt", "w")
                                        for i in staff1 :
                                            fstaff1.write(f'{i}\n')
                                        fstaff1.close()

                                        save_list_to_file(list1_filename, list1)
                                        save_list_to_file(list2_filename, list2)
                                        
                                        profit = int(total_price1)
                                        add_money(total_price1)
                                        add_order
                                        ftotal.write(f'{profit}\n')
                                        ftotal.close

                                        draw_text("Order Completed!!!", main_font, "green", screen, 650, 510)  # On top of button 1
                                        pygame.display.flip()
                                        pygame.time.wait(1000)

                                    list1_filename = './picture/order1.txt'
                                    list2_filename = './picture/food-complete-name.txt'

                                    check_and_update_lists(list1_filename, list2_filename)
                                    last_clicked_order = None

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

                                        # 读取文件内容，保留空行
                                        ffoodrak =  open("./picture/foodrak.txt", "r")
                                        foodrak = [line.rstrip('\n') for line in ffoodrak.readlines()]  # 只去掉换行符，保留空行
                                           
                                        # 检查前三个元素是否有空位，并填入数据
                                        for i in range(min(3, len(foodrak))):
                                            if foodrak[i] == "":  # 找到空行
                                                foodrak[i] = staff2[1]  # 用 staff1[0] 填充空位
                                                

                                                # 写入更新后的内容到文件
                                                ffoodrak =  open("./picture/foodrak.txt", "w")
                                                for item in foodrak:
                                                        ffoodrak.write(f"{item}\n")  # 确保数据按行写入

                                        del staff2[1]
                                        fstaff2 = open("./picture/staff.txt", "w")
                                        for i in staff2 :
                                            fstaff2.write(f'{i}\n')
                                        fstaff2.close()

                                        save_list_to_file(list1_filename, list1)
                                        save_list_to_file(list2_filename, list2)
                                        
                                        profit = int(total_price2)
                                        add_money(total_price2)
                                        ftotal.write(f'{profit}\n')
                                        ftotal.close

                                        draw_text("Order Completed!!!", main_font, "green", screen, 650, 510)  # On top of button 1
                                        pygame.display.flip()
                                        pygame.time.wait(1000)

                                    list1_filename = './picture/order2.txt'
                                    list2_filename = './picture/food-complete-name.txt'

                                    check_and_update_lists(list1_filename, list2_filename)
                                    last_clicked_order = None

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

                                        # 读取文件内容，保留空行
                                        ffoodrak =  open("./picture/foodrak.txt", "r")
                                        foodrak = [line.rstrip('\n') for line in ffoodrak.readlines()]  # 只去掉换行符，保留空行
                                           
                                        # 检查前三个元素是否有空位，并填入数据
                                        for i in range(min(3, len(foodrak))):
                                            if foodrak[i] == "":  # 找到空行
                                                foodrak[i] = staff3[2]  # 用 staff1[0] 填充空位

                                                # 写入更新后的内容到文件
                                                ffoodrak =  open("./picture/foodrak.txt", "w")
                                                for item in foodrak:
                                                        ffoodrak.write(f"{item}\n")  # 确保数据按行写入

                                        del staff3[2]
                                        fstaff3 = open("./picture/staff.txt", "w")
                                        for i in staff3 :
                                            fstaff3.write(f'{i}\n')
                                        fstaff3.close()

                                        save_list_to_file(list1_filename, list1)
                                        save_list_to_file(list2_filename, list2)
                                        
                                        profit = int(total_price3)
                                        add_money(total_price3)
                                        ftotal.write(f'{profit}\n')
                                        ftotal.close

                                        draw_text("Order Completed!!!", main_font, "green", screen, 650, 510)  # On top of button 1
                                        pygame.display.flip()
                                        pygame.time.wait(1000)

                                    list1_filename = './picture/order3.txt'
                                    list2_filename = './picture/food-complete-name.txt'

                                    check_and_update_lists(list1_filename, list2_filename)
                                    last_clicked_order = None                        
                                
                                else :
                                    draw_text("Please select an order", main_font, "red", screen, 650, 510)  # On top of button 1
                                    pygame.display.flip()
                                    pygame.time.wait(1000)

                                break
                            
                            else:
                        
                                draw_text("Waiting table is fulled", main_font, "red", screen, 650, 510)  # On top of button 1
                                pygame.display.flip()
                                pygame.time.wait(1000)

        if sound_muted:
            screen.blit(soundoff_btn, soundoff_btn_rect.topleft)  
        else:
            screen.blit(soundon_btn, soundon_btn_rect.topleft)  
        
        
        
        pygame.display.flip()
        pygame.time.Clock().tick(30)

def draw_popup():
    pygame.draw.rect(screen, (255, 201, 254), popup_rect)
    pygame.draw.rect(screen, (148, 5, 100), popup_rect, 5)  # Popup border
    
    screen.blit(coin1_img,(852, 322))
    screen.blit(coin1_img,(1023, 322))
    pan_unlock_button.update()  # 带框的机器图片，不能删
    steamer_unlock_button.update()
    oven_unlock_button.update()
    inputmoney_rect = pygame.Rect(740,150, 200, 33)
    pygame.draw.rect(screen, (162, 164, 164), inputmoney_rect)

    draw_text("Money: ", upgrade_font, "black", screen, 700, 170)
    draw_text(money_amount, upgrade_font, "navyblue", screen, 836, 170)
    draw_text("Machine Types: ", upgrade_font, "black", screen, 520, 250)
    draw_text("1800", upgrade_font, "black", screen, 908, 336)
    draw_text("4000", upgrade_font, "black", screen, 1078, 336)
    draw_text("Default", upgrade_font, "black", screen, 710, 343)
    draw_text("Steamer", upgrade_font, "black", screen, 892, 358)
    draw_text("Oven", upgrade_font, "black", screen, 1073, 358)
    draw_text("Machine Features - B: Cooking process lowered to 40s", upgrade_font, "black", screen, 714, 380)
    draw_text("- C: Cooking process lowered to 30s", upgrade_font, "black", screen, 805, 408)

    close_button.draw(screen)


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

def pink_closebutton(): #irene
    global running
    running = False

close_button = load_image('./picture/close_windowBtn.png',(60,60))
close_button = ImageButton(close_button, 1165, 103, pink_closebutton)

def save_unlocked_machines(): #把已经unlock的machine写进file里
    f = open("./picture/unlocked_machines.txt", "w")  # Open the file in write mode
    for machine in unlocked_machine:
        f.write(machine + "\n")  # Write each unlocked machine to the file
    f.close()

def load_unlocked_machines(): #读file
    global unlocked_machine
    unlocked_machine = set() 
    try:
        f = open("./picture/unlocked_machines.txt", "r")  #读的file
        lines = f.readlines()
        for line in lines:
            unlocked_machine.add(line.strip())  #将machine的名字加进去
        f.close()  # 读完file后就会关掉
    except FileNotFoundError:
        pass

def upgrade_process():
    global running
    global show_popup, show_popup2B, show_popup2C, not_enough_money
    global selected_upgradeB,selected_upgradeC, message_timer
    global money_amount, unlocked_machine,current_upgrade, already_upgrade


    pygame.draw.rect(screen, (148, 5, 100), popup_rect, 5)  # Popup border
    
    show_popup = True
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.is_clicked(event.pos):
                    click_sfx.play()
                    close_button.press()

                if upgrade_btn.checkForInput(pygame.mouse.get_pos()): 
                    draw_popup()

                if steamer_unlock_button.checkForInput(pygame.mouse.get_pos()):
                    if "STEAMER" in unlocked_machine:
                        current_upgrade = "STEAMER"
                        already_upgrade = True
                        message_timer = 60
                    else:
                        if money_amount < upgrade_costs["STEAMER"]:
                            not_enough_money = True
                            message_timer = 60
                        else:
                            show_popup2B = True
                        
                if yesB_button.checkForInput(pygame.mouse.get_pos()) and show_popup2B:
                    if "STEAMER" in unlocked_machine:
                        already_upgrade = True  # Ensure money is not deducted
                        message_timer = 60
                        show_popup2B = False
                    elif money_amount >= upgrade_costs["STEAMER"]:
                        money_amount -= upgrade_costs["STEAMER"]
                        unlocked_machine.add("STEAMER")
                        selected_upgradeB = "STEAMER"
                        current_upgrade = "STEAMER"
                        message_timer = 60
                        show_popup2B = False
                        save_unlocked_machines() # Save the unlocked machines to file
                    else:
                        not_enough_money = True
                        message_timer = 60
                
                if oven_unlock_button.checkForInput(pygame.mouse.get_pos()):
                    if "OVEN" in unlocked_machine:
                        current_upgrade = "OVEN"
                        already_upgrade = True
                        message_timer = 60
                    else:
                        if money_amount < upgrade_costs["OVEN"]:
                            not_enough_money = True
                            message_timer = 60
                        else:
                            show_popup2C = True
                    
                if yesC_button.checkForInput(pygame.mouse.get_pos()) and show_popup2C:
                    if "OVEN" in unlocked_machine:
                        already_upgrade = True
                        message_timer = 60
                        show_popup2C = False
                    elif money_amount >= upgrade_costs["OVEN"]:
                        money_amount -= upgrade_costs["OVEN"]
                        unlocked_machine.add("OVEN")
                        selected_upgradeC = "OVEN"
                        current_upgrade = "OVEN"
                        message_timer = 60
                        show_popup2C = False
                        save_unlocked_machines() # Save the unlocked machines to file
                    else:
                        not_enough_money = True
                        message_timer = 60

                if noB_button.checkForInput(pygame.mouse.get_pos()):
                    show_popup2B = False  
                   
                if noC_button.checkForInput(pygame.mouse.get_pos()):
                    show_popup2C = False 

                if soundon_btn_rect.collidepoint(event.pos) or soundoff_btn_rect.collidepoint(event.pos):
                    mute_sound()
        
        if sound_muted:
            screen.blit(soundoff_btn, soundoff_btn_rect.topleft)  
        else:
            screen.blit(soundon_btn, soundon_btn_rect.topleft)  
        
        handle_upgrades()
        pygame.display.update()
        clock.tick(60)

load_unlocked_machines()


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

def detect_unlock_food():
    f = open("./picture/unlocked_food.txt", "r")
    content = f.read()

    unlocked_items = {}

    lines = content.splitlines()
    for line in lines:
        if ":True" in line:
            food_name = line.split(":True")[0].strip().lower()
            unlocked_items[food_name] = True
        elif ":False" in line:
            food_name = line.split(":False")[0].strip().lower()
            unlocked_items[food_name] = False
    
    return unlocked_items


def selectfood_page2(): # after player click STOVE POT button rect
    global stovepot_food_index, current_page, running

    waiting_duration = 10
    food_selected = False  # 用来track food select

    unlocked_items = detect_unlock_food()
    color_locked = (128, 128, 128) #灰色
    color_unlocked = (186, 255, 184) #浅青色
    hover_color = (18, 255, 50) #深青色
    running = True

    while running:
        
        if steamer_running:
            steamer_elapsed = time.time() - steamer_start_time
            cooking_bar_steamer.update(steamer_elapsed, steamer_duration)
            cooking_bar_steamer.draw(screen)
            pastefood_steamer(steamer_food_index)
            draw_machine_type_button("steamer")

        if oven_running:
            oven_elapsed = time.time() - oven_start_time
            cooking_bar_oven.update(oven_elapsed, oven_duration)
            cooking_bar_oven.draw(screen)
            pastefood_oven(oven_food_index)
            draw_machine_type_button("oven")

        if steamer_exceed_time:
            waiting_elapsed = time.time() - steamer_waiting_start_time
            waiting_bar_steamer.update(waiting_elapsed, waiting_duration)
            waiting_bar_steamer.draw(screen)
            pastefood_steamer(steamer_food_index)
            screen.blit(fire_img, (610, 113))
            draw_machine_waiting_button("steamer")

        if oven_exceed_time:
            waiting_elapsed = time.time() - oven_waiting_start_time
            waiting_bar_oven.update(waiting_elapsed, waiting_duration)
            waiting_bar_oven.draw(screen)
            pastefood_oven(oven_food_index)
            screen.blit(fire_img, (930, 113))
            draw_machine_waiting_button("oven")

        if sound_muted:
            screen.blit(soundoff_btn, soundoff_btn_rect.topleft)
        else:
            screen.blit(soundon_btn, soundon_btn_rect.topleft)


        food_selection1_rect = pygame.Rect(400, 120, 800, 600)
        food_selection2_rect = pygame.Rect(425, 195, 752, 495)
        pygame.draw.rect(screen, (255, 201, 254), food_selection1_rect)
        pygame.draw.rect(screen, (148, 5, 100), food_selection1_rect, 5)
        pygame.draw.rect(screen, (196, 192, 255), food_selection2_rect)
        close_button.draw(screen)

        draw_text("Food selection: ", food_selection_font, "black", screen, 550, 155)

        start_index = (current_page - 1) * max_items_per_page
        end_index = start_index + max_items_per_page
        items_on_page = food_lists[start_index:end_index]

       
        for i in range(len(items_on_page)):
            food_item = items_on_page[i]
            food_name_normalized = food_item["name"].strip().lower()    # Normalizing the item name
            y_position = 216 + i * 144

            # 确定格子的颜色，如果locked的话就灰色， unlocked的话就冷白色
            if not unlocked_items.get(food_name_normalized, True):
                rect_color = color_locked
            else:
                rect_color = color_pic

            pygame.draw.rect(screen, rect_color, pygame.Rect(440, y_position, 720, 130))
            screen.blit(food_item["image"], (460, y_position + 4))
            draw_text(food_item["name"], food_title_font, "black", screen, 700, y_position + 60)
            draw_text(food_item["price"], food_title_font, "black", screen, 900, y_position + 60)

            # Only show select button for unlocked food items
            if rect_color == color_pic:
                selectprepare_button_rect = pygame.Rect(1010, y_position + 43, 130, 40)
                select_button_color = color_unlocked
                if selectprepare_button_rect.collidepoint(pygame.mouse.get_pos()):
                    select_button_color = hover_color

                # Draw select button
                selectbutton_surface.fill(select_button_color)
                selectbutton_surface.blit(SELECT_text, text_rect)
                screen.blit(selectbutton_surface, selectprepare_button_rect.topleft)

        total_pages = (len(food_lists) + max_items_per_page - 1) // max_items_per_page
        if current_page < total_pages:
            next_btn.update()

        if current_page > 1:
            back_btn.update()

        if stovepot_running:
            cooking_bar_stovepot.update(time.time() - stovepot_start_time, stovepot_duration)
            cooking_bar_stovepot.draw(screen)
            pastefood_stovepot(stovepot_food_index)
            draw_machine_type_button("stovepot")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.is_clicked(event.pos):
                    click_sfx.play()
                    if not food_selected:
                        stovepot_food_index = -1  #
                    close_button.press()  

                    if not (stovepot_running or steamer_running or oven_running):
                        close_button.press()  

                    else:
                        return_cooking_view()  # Keep cooking view active if cooking is still ongoing
                        close_button.press()
                    
                if next_btn.checkForInput(pygame.mouse.get_pos()) and current_page < total_pages:
                    current_page += 1

                if back_btn.checkForInput(pygame.mouse.get_pos()) and current_page > 1:
                    current_page -= 1

                # Check if the select button is clicked
                for i, food_item in enumerate(items_on_page):
                    food_name_normalized = food_item["name"].strip().lower()
                    y_position = 216 + i * 144
                    selectprepare_button_rect = pygame.Rect(1010, y_position + 43, 130, 40)
                    if selectprepare_button_rect.collidepoint(event.pos):
                        click_sfx.play()
                        selected_food_index = start_index + i
                        stovepot_food_index = selected_food_index  # Update the global index
                        food_selected = True
                        return stovepot_process(selected_food_index)

                if soundon_btn_rect.collidepoint(event.pos) or soundoff_btn_rect.collidepoint(event.pos):
                    mute_sound()
        # close_button.draw(screen)
        pygame.display.update()
        clock.tick(60)


def selectfood_page3(): # after player click steamer
    global steamer_food_index, current_page, running

    waiting_duration = 10
    food_selected = False

    unlocked_items = detect_unlock_food()
    color_locked = (128, 128, 128)
    color_unlocked = (186, 255, 184) 
    hover_color = (18, 255, 50)
    running = True

    while running:
        
        if stovepot_running:
            cooking_bar_stovepot.update(time.time() - stovepot_start_time, stovepot_duration)
            cooking_bar_stovepot.draw(screen)
            pastefood_stovepot(stovepot_food_index)
            draw_machine_type_button("stovepot")
        
        if oven_running:
            cooking_bar_oven.update(time.time() - oven_start_time, oven_duration)
            cooking_bar_oven.draw(screen)
            pastefood_oven(oven_food_index)
            draw_machine_type_button("oven")

        if stovepot_exceed_time:
            waiting_elapsed = time.time() - stovepot_waiting_start_time
            waiting_bar_stovepot.update(waiting_elapsed, waiting_duration)
            waiting_bar_stovepot.draw(screen)
            pastefood_stovepot(stovepot_food_index)
            screen.blit(fire_img, (290, 113))
            draw_machine_waiting_button("stovepot")

        if oven_exceed_time:
            waiting_elapsed = time.time() - oven_waiting_start_time
            waiting_bar_oven.update(waiting_elapsed, waiting_duration)
            waiting_bar_oven.draw(screen)
            pastefood_oven(oven_food_index)
            screen.blit(fire_img, (930, 113))
            draw_machine_waiting_button("oven")
        
        if sound_muted:
            screen.blit(soundoff_btn, soundoff_btn_rect.topleft)  
        else:
            screen.blit(soundon_btn, soundon_btn_rect.topleft)  

        
        food_selection1_rect = pygame.Rect(400, 120, 800, 600)
        food_selection2_rect = pygame.Rect(425, 195, 752, 495)
        pygame.draw.rect(screen, (255, 201, 254), food_selection1_rect)
        pygame.draw.rect(screen, (148, 5, 100), food_selection1_rect, 5)
        pygame.draw.rect(screen, (196, 192, 255), food_selection2_rect)
        close_button.draw(screen)

        draw_text("Food selection: ", food_selection_font, "black", screen, 550, 155)

        start_index = (current_page - 1) * max_items_per_page
        end_index = start_index + max_items_per_page
        items_on_page = foodlist_steamer[start_index:end_index]

        for i in range(len(items_on_page)):
            food_item = items_on_page[i]
            food_name_normalized = food_item["name"].strip().lower() 
            y_position = 216 + i * 144

            # 确定格子的颜色，如果locked的话就灰色， unlocked的话就冷白色
            if not unlocked_items.get(food_name_normalized, True):
                rect_color = color_locked
            else:
                rect_color = color_pic

            pygame.draw.rect(screen, rect_color, pygame.Rect(440, y_position, 720, 130))
            screen.blit(food_item["image"], (460, y_position + 4))
            draw_text(food_item["name"], food_title_font, "black", screen, 700, y_position + 60)
            draw_text(food_item["price"], food_title_font, "black", screen, 900, y_position + 60)

           # Only show select button for unlocked food items
            if rect_color == color_pic:
                selectprepare_button_rect = pygame.Rect(1010, y_position + 43, 130, 40)
                select_button_color = color_unlocked
                if selectprepare_button_rect.collidepoint(pygame.mouse.get_pos()):
                    select_button_color = hover_color

                # Draw select button
                selectbutton_surface.fill(select_button_color)
                selectbutton_surface.blit(SELECT_text, text_rect)
                screen.blit(selectbutton_surface, selectprepare_button_rect.topleft)

        total_pages = (len(foodlist_steamer) + max_items_per_page - 1) // max_items_per_page
        if current_page < total_pages:
            next_btn.update()

        if current_page > 1:
            back_btn.update()
        
        if steamer_running:
            cooking_bar_steamer.update(time-time() - steamer_start_time, steamer_duration)
            cooking_bar_steamer.draw(screen)
            pastefood_steamer(steamer_food_index)
            draw_machine_type_button('steamer')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.is_clicked(event.pos):
                    click_sfx.play()
                    if not food_selected:
                        steamer_food_index = -1  # Reset the food index
                        close_button.press()  # Go back to the main screen
                    if not (stovepot_running or steamer_running or oven_running):
                        close_button.press()   #return main screen
                    else:
                        return_cooking_view() # 确保他还在煮
                        close_button.press()
                    

                if next_btn.checkForInput(pygame.mouse.get_pos()) and current_page < total_pages:
                    current_page += 1

                if back_btn.checkForInput(pygame.mouse.get_pos()) and current_page > 1:
                    current_page -= 1

                # Check if the select button is clicked
                for i, food_item in enumerate(items_on_page):
                    food_name_normalized = food_item["name"].strip().lower()
                    y_position = 216 + i * 144
                    selectprepare_button_rect = pygame.Rect(1010, y_position + 43, 130, 40)
                    if selectprepare_button_rect.collidepoint(event.pos) and unlocked_items.get(food_name_normalized, False):
                        click_sfx.play()
                        selected_food_index = start_index + i
                        steamer_food_index = selected_food_index
                        food_selected = True
                        return steamer_process(selected_food_index)
                
                if soundon_btn_rect.collidepoint(event.pos) or soundoff_btn_rect.collidepoint(event.pos):
                    mute_sound()
                
        pygame.display.update()
        clock.tick(60)


def selectfood_page4(): # after player click oven
    global current_page, oven_food_index, running

    waiting_duration = 10
    food_selected = False

    unlocked_items = detect_unlock_food()
    color_locked = (128, 128, 128)
    color_unlocked = (186, 255, 184) 
    hover_color = (18, 255, 50)
    running = True

    while running:

        if stovepot_running:
            cooking_bar_stovepot.update(time.time() - stovepot_start_time, stovepot_duration)
            cooking_bar_stovepot.draw(screen)
            pastefood_stovepot(stovepot_food_index)
            draw_machine_type_button("stovepot")
        
        if steamer_running:
            cooking_bar_steamer.update(time.time() - steamer_start_time, steamer_duration)
            cooking_bar_steamer.draw(screen)
            pastefood_steamer(steamer_food_index)
            draw_machine_type_button("steamer")

        if stovepot_exceed_time:
            waiting_elapsed = time.time() - stovepot_waiting_start_time
            waiting_bar_stovepot.update(waiting_elapsed, waiting_duration)
            waiting_bar_stovepot.draw(screen)
            pastefood_stovepot(stovepot_food_index)
            screen.blit(fire_img, (290, 113))
            draw_machine_waiting_button("stovepot")

        if steamer_exceed_time:
            waiting_elapsed = time.time() - steamer_waiting_start_time
            waiting_bar_steamer.update(waiting_elapsed, waiting_duration)
            waiting_bar_steamer.draw(screen)
            pastefood_steamer(steamer_food_index)
            screen.blit(fire_img, (610, 113))
            draw_machine_waiting_button("steamer")
        
        if sound_muted:
            screen.blit(soundoff_btn, soundoff_btn_rect.topleft)  
        else:
            screen.blit(soundon_btn, soundon_btn_rect.topleft)  

       
        food_selection1_rect = pygame.Rect(400, 120, 800, 600)
        food_selection2_rect = pygame.Rect(425, 195, 752, 495)
        pygame.draw.rect(screen, (255, 201, 254), food_selection1_rect)
        pygame.draw.rect(screen, (148, 5, 100), food_selection1_rect, 5)
        pygame.draw.rect(screen, (196, 192, 255), food_selection2_rect)
        close_button.draw(screen)

        draw_text("Food selection: ", food_selection_font, "black", screen, 550, 155)

        start_index = (current_page - 1) * max_items_per_page
        end_index = start_index + max_items_per_page
        items_on_page = foodlist_oven[start_index:end_index]

        for i in range(len(items_on_page)):
            food_item = items_on_page[i]
            food_name_normalized = food_item["name"].strip().lower()
            y_position = 216 + i * 144

            # 确定格子的颜色，如果locked的话就灰色， unlocked的话就冷白色
            if not unlocked_items.get(food_name_normalized, True):
                rect_color = color_locked
            else:
                rect_color = color_pic


            pygame.draw.rect(screen, rect_color, pygame.Rect(440, y_position, 720, 130))
            screen.blit(food_item["image"], (460, y_position + 4))
            draw_text(food_item["name"], food_title_font, "black", screen, 700, y_position + 60)
            draw_text(food_item["price"], food_title_font, "black", screen, 900, y_position + 60)

            # Only show select button for unlocked food items
            if rect_color == color_pic:
                selectprepare_button_rect = pygame.Rect(1010, y_position + 43, 130, 40)
                select_button_color = color_unlocked
                if selectprepare_button_rect.collidepoint(pygame.mouse.get_pos()):
                    select_button_color = hover_color

                # Draw select button
                selectbutton_surface.fill(select_button_color)
                selectbutton_surface.blit(SELECT_text, text_rect)
                screen.blit(selectbutton_surface, selectprepare_button_rect.topleft)

        total_pages = (len(foodlist_oven) + max_items_per_page - 1) // max_items_per_page
        if current_page < total_pages:
            next_btn.update()

        if current_page > 1:
            back_btn.update()

        if oven_running:
            cooking_bar_oven.update(time-time() - oven_start_time, oven_duration)
            cooking_bar_oven.draw(screen)
            pastefood_oven(oven_food_index)
            draw_machine_type_button("oven")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.is_clicked(event.pos):
                    click_sfx.play()
                    if not food_selected:
                        oven_food_index = -1  # Reset the food index
                        close_button.press() # Go back to the main screen
                    if not (stovepot_running or steamer_running or oven_running):
                        close_button.press()  
                    else:
                        return_cooking_view() # 确保他还在煮
                        close_button.press() 

                if next_btn.checkForInput(pygame.mouse.get_pos()) and current_page < total_pages:
                    current_page += 1

                if back_btn.checkForInput(pygame.mouse.get_pos()) and current_page > 1:
                    current_page -= 1

                # Check if the select button is clicked
                for i, food_item in enumerate(items_on_page):
                    food_name_normalized = food_item["name"].strip().lower()
                    y_position = 216 + i * 144
                    selectprepare_button_rect = pygame.Rect(1010, y_position + 43, 130, 40)
                    if selectprepare_button_rect.collidepoint(event.pos):
                        click_sfx.play()
                        selected_food_index = start_index + i
                        oven_food_index = selected_food_index  # Update the global index
                        food_selected = True
                        return oven_process(selected_food_index)

                    
                if soundon_btn_rect.collidepoint(event.pos) or soundoff_btn_rect.collidepoint(event.pos):
                    mute_sound()

        
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

    if selected_food_index < 0 or selected_food_index >= len(food_lists):
        return       # Exit if the index is invalid

    stovepot_running = True
    stovepot_start_time = time.time()
    stovepot_duration = 10 
    stovepot_food_index = selected_food_index

    return
      

def steamer_process(selected_food_index):
    global steamer_start_time, steamer_running, steamer_duration, steamer_food_index

    if selected_food_index < 0 or selected_food_index >= len(foodlist_steamer):
        return         # Exit if the index is invalid

    steamer_running = True
    steamer_start_time = time.time()
    steamer_duration = 15  
    steamer_food_index = selected_food_index

    return


def oven_process(selected_food_index):
    global oven_start_time, oven_running, oven_duration, oven_food_index

    if selected_food_index < 0 or selected_food_index >= len(foodlist_oven):
        return            

    oven_running = True
    oven_start_time = time.time()
    oven_duration = 20 
    oven_food_index = selected_food_index

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
    slot_width = table_rect.width // 6         
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


def remind_no_empty_slots():
    global message_timer, full_slot_remind
    full_slot_remind = True
    message_timer = 120


        
def put_food_to_slots(selected_food_index, machine_type):
    if selected_food_index is None or selected_food_index<0:
        return False
    
    slot_index = determine_available_slots()

    if slot_index is not None:

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

        f = open("./picture/food-complete-name.txt", "a")
        f.write (f"{food_name}\n")
        f.close()

        f = open("./picture/food-complete-price.txt", "a")
        f.write(f"{food_price}\n")
        f.close()

    else:
        remind_no_empty_slots()

    return True
        
waiting_bar_stovepot = CookingBar(330, 119, 160, 20, 100)  # x, y, w, h, max_hp
waiting_bar_steamer = CookingBar(651, 120, 160, 20, 100)
waiting_bar_oven = CookingBar(965, 119, 160, 20, 100)    


def throw_food_into_dustbin():
    global stovepot_food_index, steamer_food_index, oven_food_index
    global waste_food_index, stovepot_button_rect, steamer_button_rect, oven_button_rect
    global soundoff_btn_rect, soundon_btn_rect

    waste_food_img = None
    waste_food_position = None

    if sound_muted:
        sound_button_img = soundoff_btn
        sound_button_rect = soundoff_btn_rect
    else:
        sound_button_img = soundon_btn
        sound_button_rect = soundon_btn_rect


    if stovepot_food_index == waste_food_index:
        if waste_food_index in range(len(food_lists)):
            waste_food_img = food_lists[waste_food_index]["image"]
        waste_food_position = (240, 157)  # stovepot食物的位置
    elif steamer_food_index == waste_food_index:
        if waste_food_index in range(len(foodlist_steamer)):
            waste_food_img = foodlist_steamer[waste_food_index]["image"]
        waste_food_position = (565, 157)  
    elif oven_food_index == waste_food_index:
        if waste_food_index in range(len(foodlist_oven)):
            waste_food_img = foodlist_oven[waste_food_index]["image"]
        waste_food_position = (850, 157) 


    # 如果没有食物的图片的话就退出
    if waste_food_img is None or waste_food_position is None:
        return

    dustbin_pos = (1250, 160)  
    speed = 15
    throwing = True
    angle = 0  # 初始角度

    while throwing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                throwing = False

        # 计算食物和垃圾桶的direction vector
        direction_x = dustbin_pos[0] - waste_food_position[0]
        direction_y = dustbin_pos[1] - waste_food_position[1]

        # 计算食物与垃圾桶的距离
        distance = (direction_x**2 + direction_y**2)**0.5

        if distance > 10:  # 继续往垃圾桶方向移动
            dir_x = direction_x / distance
            dir_y = (direction_y / distance)
            waste_food_position = (waste_food_position[0] + dir_x * speed, waste_food_position[1] + dir_y * speed)

            # 旋转食物
            angle += 10  
            rotated_food_img = pygame.transform.rotate(waste_food_img, angle)

            rotated_rect = rotated_food_img.get_rect(center=waste_food_position)

            screen.blit(background, (0, 0))  
            pan_default_button.update()
            steamer_button.update()
            oven_button.update()  
            profilebutton.update()
            upgrade_btn.update()
            menu_button.update()
            orderbtn.update()
            happyhour_bar(hhactive)
            money_bar()
            waiting_table()

            stovepot_button_rect = stovepot_button_select()
            steamer_button_rect = steamer_button_select()
            oven_button_rect = oven_button_select()

            screen.blit(rotated_food_img, rotated_rect.topleft)  
            screen.blit(sound_button_img, sound_button_rect.topleft)  # Draw the sound button
            screen.blit(dustbin_img, dustbin_pos)
            pygame.display.update()

        else:
            throwing = False
            waste_food_index = None  # Reset waste food index

        pygame.time.delay(20)



def exceed_time_collect():
    global stovepot_exceed_time, steamer_exceed_time, oven_exceed_time
    global waste_food_index, stovepot_waiting_start_time, steamer_waiting_start_time, oven_waiting_start_time
    global stovepot_food_index, steamer_food_index, oven_food_index

    waiting_duration = 10
    current_time = time.time()

    if sound_muted:
        screen.blit(soundoff_btn, soundoff_btn_rect.topleft)  
    else:
        screen.blit(soundon_btn, soundon_btn_rect.topleft)  


    # Handle Stovepot waiting bar
    if stovepot_exceed_time:
        waiting_elapsed = current_time - stovepot_waiting_start_time
        waiting_bar_stovepot.update(waiting_elapsed, waiting_duration)
        waiting_bar_stovepot.draw(screen)
        pastefood_stovepot(stovepot_food_index)
        screen.blit(fire_img, (290, 113))
        draw_machine_waiting_button("stovepot")
        if waiting_elapsed >= waiting_duration:
            waste_food_index = stovepot_food_index
            throw_food_into_dustbin()
            stovepot_food_index = None
            stovepot_exceed_time = False
         

    # Handle Steamer waiting bar
    if steamer_exceed_time:
        waiting_elapsed = current_time - steamer_waiting_start_time
        waiting_bar_steamer.update(waiting_elapsed, waiting_duration)
        waiting_bar_steamer.draw(screen)
        pastefood_steamer(steamer_food_index)
        screen.blit(fire_img, (610, 113))
        draw_machine_waiting_button("steamer")
        if waiting_elapsed >= waiting_duration:
            waste_food_index = steamer_food_index
            throw_food_into_dustbin()
            steamer_food_index = None
            steamer_exceed_time = False
          

    # Handle Oven waiting bar
    if oven_exceed_time:
        waiting_elapsed = current_time - oven_waiting_start_time
        waiting_bar_oven.update(waiting_elapsed, waiting_duration)
        waiting_bar_oven.draw(screen)
        pastefood_oven(oven_food_index)
        screen.blit(fire_img, (930, 113))
        draw_machine_waiting_button("oven")
        if waiting_elapsed >= waiting_duration:
            waste_food_index = oven_food_index
            throw_food_into_dustbin()
            oven_food_index = None
            oven_exceed_time = False
            

def cooking_process():
    global stovepot_running, steamer_running, oven_running, message_timer
    global stovepot_start_time, steamer_start_time, oven_start_time
    global stovepot_food_index, steamer_food_index, oven_food_index
    global stovepot_exceed_time, steamer_exceed_time, oven_exceed_time
    global stovepot_waiting_start_time, steamer_waiting_start_time, oven_waiting_start_time

    current_time = time.time()

    full_slot_remind = False
    message_timer = 0

    # Handle Stovepot cooking process
    if stovepot_running:
        elapsed_time = current_time - stovepot_start_time
        if elapsed_time >= stovepot_duration:
            stovepot_running = False
            slot_index = determine_available_slots()
            if slot_index is not None:
                put_food_to_slots(stovepot_food_index, "stovepot")
                stovepot_exceed_time = False
            else:
                stovepot_exceed_time = True
                stovepot_waiting_start_time = current_time  # Start waiting bar timer

        cooking_bar_stovepot.update(elapsed_time, stovepot_duration)
        cooking_bar_stovepot.draw(screen)
        pastefood_stovepot(stovepot_food_index)
        draw_machine_type_button("stovepot")

    # Handle Steamer cooking process
    if steamer_running:
        elapsed_time = current_time - steamer_start_time
        if elapsed_time >= steamer_duration:
            steamer_running = False
            slot_index = determine_available_slots()
            if slot_index is not None:
                put_food_to_slots(steamer_food_index, "steamer")
                steamer_exceed_time = False
            else:
                steamer_exceed_time = True
                steamer_waiting_start_time = current_time  # Start waiting bar timer

        cooking_bar_steamer.update(elapsed_time, steamer_duration)
        cooking_bar_steamer.draw(screen)
        pastefood_steamer(steamer_food_index)
        draw_machine_type_button("steamer")

    # Handle Oven cooking process
    if oven_running:
        elapsed_time = current_time - oven_start_time
        if elapsed_time >= oven_duration:
            oven_running = False
            slot_index = determine_available_slots()
            if slot_index is not None:
                put_food_to_slots(oven_food_index, "oven")
                oven_exceed_time = False
            else:
                oven_exceed_time = True
                oven_waiting_start_time = current_time  # Start waiting bar timer

        cooking_bar_oven.update(elapsed_time, oven_duration)
        cooking_bar_oven.draw(screen)
        pastefood_oven(oven_food_index)
        draw_machine_type_button("oven")

    if full_slot_remind:
        font_slot = pygame.font.SysFont("cambria", 30, bold=True)
        draw_text("Full   slots   now! ", font_slot, "red", screen, 680, 600)
        message_timer -= 1
        if message_timer <= 0:
            full_slot_remind = False

    # Handle waiting bar if exceed time
    exceed_time_collect()

def draw_machine_type_button(machine_type):
    colors_cooking = {
        "stovepot": (255, 0, 128),
        "steamer": (255, 0, 128),
        "oven": (255, 0, 128)
    }
    texts = {
        "stovepot": ChooseMachine_text1,
        "steamer": ChooseMachine_text2,
        "oven": ChooseMachine_text3
    }

    text_rects = {
        "stovepot": ChooseMachine_text_rect1,
        "steamer": ChooseMachine_text_rect2,
        "oven": ChooseMachine_text_rect3
    }

    button_rects = {
        "stovepot": machinetype_button_rect1,
        "steamer": machinetype_button_rect2,
        "oven": machinetype_button_rect3
    }
    surface = pygame.Surface((180, 50), pygame.SRCALPHA)
    surface.fill(colors_cooking[machine_type])
    surface.blit(texts[machine_type], text_rects[machine_type])
    screen.blit(surface, button_rects[machine_type].topleft)


def draw_machine_waiting_button(machine_type):
    colors_waiting = {
        "stovepot": (204, 0, 0),
        "steamer": (204, 0, 0),
        "oven": (204, 0, 0)
    }
    texts = {
        "stovepot": ChooseMachine_text1,
        "steamer": ChooseMachine_text2,
        "oven": ChooseMachine_text3
    }

    text_rects = {
        "stovepot": ChooseMachine_text_rect1,
        "steamer": ChooseMachine_text_rect2,
        "oven": ChooseMachine_text_rect3
    }

    button_rects = {
        "stovepot": machinetype_button_rect1,
        "steamer": machinetype_button_rect2,
        "oven": machinetype_button_rect3
    }
    surface = pygame.Surface((180, 50), pygame.SRCALPHA)
    surface.fill(colors_waiting[machine_type])
    surface.blit(texts[machine_type], text_rects[machine_type])
    screen.blit(surface, button_rects[machine_type].topleft)


sound_muted = False
def mute_sound():
    global sound_muted

    if sound_muted:
        mixer.music.set_volume(1) 
        screen.blit(soundon_btn, soundon_btn_rect.topleft)
        
    else:
        mixer.music.set_volume(0)  
        screen.blit(soundoff_btn, soundoff_btn_rect.topleft)
       
    sound_muted = not sound_muted
    click_sfx.play()  
    pygame.display.update()


def machine_already_unlocked(machine_name):
    global message_timer, machine_complete_unlocked

    unlock_font = pygame.font.Font(None, 36)
    draw_text(f"You haven't unlocked the {machine_name} yet !", unlock_font, "red", screen, 710, 610 )
    message_timer -= 1
    if message_timer == 0:
        machine_complete_unlocked = False

def handle_unlocking_machine():
    global message_timer, machine_complete_unlocked, machine_name

    screen.blit(dustbin_img, (1250, 160))
    machine_complete_unlocked = True

    if machine_complete_unlocked:
        machine_already_unlocked(machine_name)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if soundon_btn_rect.collidepoint(event.pos) or soundoff_btn_rect.collidepoint(event.pos):
                mute_sound()

    if sound_muted:
        screen.blit(soundoff_btn, soundoff_btn_rect.topleft)
    else:
        screen.blit(soundon_btn, soundon_btn_rect.topleft)
    
    pygame.display.flip()
    clock.tick(30)

def read_food_list(filename):
    with open(filename, "r") as file:
        # 读取文件并按换行符分割食物名称
        lines = file.read().splitlines()  
        # 去掉每一行中的空格并确保每个名称是一个独立的元素
        result = [item.strip() for item in lines if item.strip()]
        return result

def display_food_images(foodcom):

    # 1. 先绘制等待桌格子
    table_rect = pygame.Rect(195, 620, 1070, 140)
    table_color = (188, 143, 143)
    pygame.draw.rect(screen, table_color, table_rect, pygame.SRCALPHA)

    slot_width = table_rect.width // 6  # 每个格子的宽度
    slot_height = table_rect.height     # 每个格子的高度是table的高度

    # 绘制6个格子
    for col in range(6):  # 6个列代表6个格子
        slot_rect = pygame.Rect(
            table_rect.x + col * slot_width,
            table_rect.y,
            slot_width, slot_height
        )
        pygame.draw.rect(screen, (200, 200, 200), slot_rect, 3)  # 灰色边框的格子
        # 图片映射
        
    food_image_mapping = {
        'Tokbokki': "./picture/tokbokki.png",
        "Fried Rice": "./picture/friedrice.png",
        "Oden": "./picture/oden.png",
        "Bibimbap": "./picture/bibimbap.png",
        "Korean Army Stew": "./picture/armystew.png",
        "Fried Noodles": "./picture/friednoodle.png",
        "Fried Bihuns": "./picture/bihun.png",
        "Hokkien Mee": "./picture/hokkienmee.png",
        "Ramen": "./picture/ramen.png",
        "Fried Udons": "./picture/udon.png",
        "Curry Mee": "./picture/currymee.png",
        "Cantonese Kuey Teow": "./picture/kueyteow.png",
        "Kai See Hor Fun": "./picture/horfun.png",
        "Mala Xiang Guo": "./picture/mala.png",
        "Youtiao": "./picture/youtiao.png",
        "Hanjiben": "./picture/hanjiben.png",
        "Thai Steamed Fish": "./picture/steamfish.png",
        "Xiu Mai": "./picture/dimsum.png",
        "Steamed Egg": "./picture/steamegg.png",
        "Lo Mai Gai": "./picture/lomaigai.png",
        "Herbal Chicken": "./picture/herbalchicken.png",
        "Soup Dumplings": "./picture/dumpling.png",
        "Shrimp Dumplings": "./picture/shrimpdumpling.png",
        "Egg Custard Bun": "./picture/custardbun.png",
        "Corndogs": "./picture/corndog.png",
        "Korean Fried Chicken": "./picture/kfry.png",
        "Calamari Rings": "./picture/calamari.png",
        "Rainbow Cake": "./picture/rainbowcake.png",
        "Red Velvet": "./picture/redvelvet.png",
        "Black Forest": "./picture/blackforest.png",
        "Pandan Roll Cake": "./picture/pandanrollcake.png",
        "Mooncake": "./picture/mooncake.png",
        "Satay": "./picture/satay.png"
    }


    image_width, image_height = 100, 100  # 图片的大小
    table_rect = pygame.Rect(195, 620, 1070, 140)
    slot_width = table_rect.width // 6  # 每个格子的宽度
    slot_height = table_rect.height  # 每个格子的高度

    # 遍历食物列表，并将图片绘制到格子中间
    for index, item in enumerate(foodcom):
        if item == "":
            continue


        if index < 6:  # 确保不会超过6个格子
            # 获取每个格子的左上角坐标
            slot_x = table_rect.x + index * slot_width
            slot_y = table_rect.y

            # 计算图片在格子中居中的坐标
            x = slot_x + (slot_width - image_width) // 2
            y = slot_y + (slot_height - image_height) // 2

            # 根据 foodcom 中的名字查找对应的图片
            if item in food_image_mapping:
                image_file = food_image_mapping[item]
            else:
                # 如果没有找到对应的图片，使用默认图片
                image_file = "./picture/bag.png"  # 确保此图片存在

        


def main():
    global stovepot_running, steamer_running, oven_running, sound_muted
    global stovepot_start_time, steamer_start_time, oven_start_time
    global stovepot_food_index, steamer_food_index, oven_food_index
    global  machine_type, food_item, message_timer, full_slot_remind
    global stovepot_exceed_time, steamer_exceed_time, oven_exceed_time, current_machine_view
    global machine_complete_unlocked, unlocked_machine, machine_name

    stovepot_running = False
    steamer_running = False
    oven_running = False
    full_slot_remind = False
    sound_muted = False
    current_machine_view = "main_screen"

    message_timer = 0

    stovepot_start_time = 0
    steamer_start_time = 0
    oven_start_time = 0

    stovepot_food_index = -1
    steamer_food_index = -1
    oven_food_index = -1

    stovepot_exceed_time = False
    steamer_exceed_time = False
    oven_exceed_time = False

    slot_index = None
    machine_type = None
    food_item = None

    machine_name = None

    filename = "./picture/foodrak.txt"
    positions = read_file_and_get_list(filename)

    # 创建快递员组
    deliverymen = pygame.sprite.Group()
    existing_positions = list(positions)

    # 初始化快递员组
    for i, deliveryman_type in enumerate(positions):
        target_x = 250 + i * 300  # 假设每个快递员目标点依次增加
        deliveryman = Deliveryman(target_x=target_x, deliveryman_type=deliveryman_type)
        deliverymen.add(deliveryman)

    while True:
        bg_img = pygame.image.load("./picture/lobby.jpg").convert()
        screen.blit(bg_img, (0, 0))
        screen.blit(dustbin_img, (1250, 160))
        money_bar()
        happyhour_bar(hhactive)
        # waiting_table()
        profilebutton.update()
        upgrade_btn.update()
        menu_button.update()
        orderbtn.update()
        pan_default_button.update()
        steamer_button.update()
        oven_button.update()

        # Draw buttons for each machine
        stovepot_button_rect = stovepot_button_select()
        steamer_button_rect = steamer_button_select()
        oven_button_rect = oven_button_select()

        load_unlocked_food()

        ffoodlist = open("./picture/foodrak.txt","r")
        foodlist = [line.rstrip('\n') for line in ffoodlist.readlines()]  # 只去掉换行符，保留空行

        for index, item in enumerate(foodlist):
            if item == "":
                continue

            if index == 0:
                x,y = 250, 375
            elif index == 1:
                x, y= 550, 375
            elif index == 2:
                x,y = 850, 375
            
            image = pygame.image.load("./picture/bag.png")
            image = pygame.transform.scale(image, (250, 100))

            screen.blit(image, (x,y))

                # 游戏主循环中的主要处理逻辑
        new_positions = read_file_and_get_list(filename)

        # 只处理新增的外卖员类型
        if new_positions != existing_positions:
            positions = update_deliverymen(existing_positions, deliverymen, filename)
            existing_positions = new_positions  # 更新现有的 positions 列表

        
        deliverymen.update()

        # 在目标位置停下时，删除外卖员数据
        for deliveryman in deliverymen:
            if deliveryman.finished:
                deliverymen.remove(deliveryman)
                # 数据已在 update() 方法中删除，无需重复
        
        deliverymen.draw(screen)
        
        # 假设 filename 是你的食物列表文件
        food_filename = "./picture/food-complete-name.txt"
        
        # 获取文件中的食物列表
        food_list = read_food_list(food_filename)


        # 使用食物列表继续执行其他操作，比如显示食物图片
        display_food_images(food_list)  # 假设这是处理图片显示的函数


        # Handle stovepot cooking process
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
                    show_menupage()
                if orderbtn.checkForInput(pygame.mouse.get_pos()): 
                    order()
                if stovepot_button_rect.collidepoint(event.pos) and not stovepot_running:
                    click_sfx.play()
                    selectfood_page2()  # Select food from the page
                    if stovepot_food_index >= 0:    # After selecting, ensure `stovepot_food_index` is updated before processing
                        stovepot_process(stovepot_food_index)


                if steamer_button_rect.collidepoint(event.pos) and not steamer_running:
                    click_sfx.play()
                    if "STEAMER" in unlocked_machine:
                        selectfood_page3()  # Select food from the page
                        if steamer_food_index >= 0:
                            steamer_process(steamer_food_index)
                    else:
                        machine_name = "STEAMER"
                        message_timer = 120
                        handle_unlocking_machine()


                if oven_button_rect.collidepoint(event.pos) and not oven_running:
                    click_sfx.play()
                    if "OVEN" in unlocked_machine:
                        selectfood_page4()  # Select food from the page
                        if oven_food_index >= 0:
                            oven_process(oven_food_index)
                    else:
                        machine_name = "OVEN"
                        message_timer = 120
                        handle_unlocking_machine()

                # Check button input and mute/unmute sound
                if soundon_btn_rect.collidepoint(event.pos) or soundoff_btn_rect.collidepoint(event.pos):
                    mute_sound()
          
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    profile()

        if message_timer > 0:
            show_message(current_machine_message)
            message_timer -= 1
        else:
            current_machine_message = ""


        if sound_muted:
            screen.blit(soundoff_btn, soundoff_btn_rect.topleft)  
        else:
            screen.blit(soundon_btn, soundon_btn_rect.topleft)  

        
        cooking_process()
        exceed_time_collect()
        save_unlocked_food()
        save_unlocked_machines()
        update_slots(slot_index, food_item)
        pygame.display.flip()
        clock.tick(60)


def return_cooking_view():
    global stovepot_running, steamer_running, oven_running
    global current_machine_view

    # Draw cooking bars for running processes
    if stovepot_running:
        cooking_bar_stovepot.update(time.time() - stovepot_start_time, stovepot_duration)
        cooking_bar_stovepot.draw(screen)
        pastefood_stovepot(stovepot_food_index)
        draw_machine_type_button("stovepot")
        
    if steamer_running:
        cooking_bar_steamer.update(time.time() - steamer_start_time, steamer_duration)
        cooking_bar_steamer.draw(screen)
        pastefood_steamer(steamer_food_index)
        draw_machine_type_button("steamer")
        
    if oven_running:
        cooking_bar_oven.update(time.time() - oven_start_time, oven_duration)
        cooking_bar_oven.draw(screen)
        pastefood_oven(oven_food_index)
        draw_machine_type_button("oven")


    # pan_default_button.update()
    # steamer_button.update()
    # oven_button.update()
    close_button.draw(screen) 
    pygame.display.update()


def reset_machine_view():
    global stovepot_running, steamer_running, oven_running
    global stovepot_food_index, steamer_food_index, oven_food_index
    global current_machine_view

    # Reset all variables related to machine state
    stovepot_running = False
    steamer_running = False
    oven_running = False

    stovepot_food_index = -1
    steamer_food_index = -1
    oven_food_index = -1

    # Reset current machine view to main screen
    current_machine_view = "main_screen"




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