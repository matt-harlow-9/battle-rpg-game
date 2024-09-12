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
        img = pygame.image.load(f'img/{self.name}/idle/0.png')
        self.image = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)

knight = Fighter(200, 260, 'Knight', 30, 10, 3)

# game run loop
run = True
while run:

    clock.tick(fps)
    
    # draw background & panel
    draw_bg()
    draw_panel()

    # draw fighters
    knight.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()