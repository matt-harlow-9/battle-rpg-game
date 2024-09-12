import pygame
# import fighter

pygame.init()

clock = pygame.time.Clock()
fps = 60

# game window
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Battle RPG")

# load images
# - background image
background_img = pygame.image.load('img/Background/background.png').convert_alpha()
# - panel image
panel_img = pygame.image.load('img/Icons/panel.png').convert_alpha()

# draw background function
def draw_bg():
    screen.blit(background_img, (0, 0))

# draw panel function
def draw_panel():
    screen.blit(panel_img, (0, screen_height - bottom_panel))

# fighter class
class Fighter():
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0 # 0: idle, 1: attack, 2: hurt, 3: death
        self.update_time = pygame.time.get_ticks()
        # load images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'img/{self.name}/idle/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        animation_cooldown = 100
        # handle animation
        # update image
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if animation runs out, reset back to start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

knight = Fighter(200, 260, 'Knight', 30, 10, 3)
bandit1 = Fighter(550, 270, 'Bandit', 20, 6, 1)
bandit2 = Fighter(700, 270, 'Bandit', 20, 6, 1)

bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

# game run loop
run = True
while run:

    clock.tick(fps)
    
    # draw background & panel
    draw_bg()
    draw_panel()

    # draw fighters
    knight.update()
    knight.draw()
    for bandit in bandit_list:
        bandit.update()
        bandit.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()