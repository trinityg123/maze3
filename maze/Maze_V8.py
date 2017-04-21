# Imports//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import pygame
import intersects
from Walls import *
from Coins import *

# Initialize game engine///////////////////////////////////////////////////////////////////////////////////////////////////////////////
pygame.init()


# Window//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
HEIGHT = 725
WIDTH = 1275
SIZE = (WIDTH, HEIGHT)
TITLE = "MAZE"

pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(SIZE)


# Timer//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
clock = pygame.time.Clock()
refresh_rate = 60


# Colors//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
WHITE = (255, 255, 255)
GREEN = (68, 104, 4)
BLACK = (0, 0, 0)
RED = (68, 0, 0)

# Make a player

class Player():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.points = 0
        
        self.vx = 0
        self.vy = 0

    def get_rect(self):
        return [self.x, self.y, self.w, self.h]

    def move_horizontal(self, vx):
        self.vx = vx

    def move_vertical(self, vy):
        self.vy = vy

    def stop(self):
        self.vx = 0

    def move_and_process_walls(self):
        self.x += self.vx
        
        for w in walls:
            if intersects.rect_rect(self, w):
                if self.vx > 0:
                    self.x = w.x - self.w
                elif self.vx < 0:
                    self.x = w.x + w.w

        self.y += self.vy

        for w in walls:            
            if intersects.rect_rect(self, w):
                if self.vy > 0:
                    self.y = w.y - self.h
                if self.vy < 0:
                    self.y = w.y + w.h
                self.vy = 0

    def draw(self):
        pygame.draw.rect(screen, RED, [self.x, self.y, self.w, self.h])
 

# Make game objects
player = Player(26, 26, 20, 20)

player_vx = 0
player_vy = 0
player_speed = 3


# Game loop/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    if pressed[pygame.K_UP]:
        player.move_vertical(player_speed)
    elif pressed[pygame.K_DOWN]:
        player.move_vertical(-player_speed)
    else:
        player.stop()

    if left:
        player.move_horizontal(-player_speed)
    elif right:
        player.move_horizontal(player_speed)
    else:
        player.stop()

# Game Logic

    
    if (len(coins) == 0):
        print("You Win")
                
    screen.fill(BLACK)


    '''coin intersects'''
    for c in coins:
        if intersects.rect_rect(player, c):
            coins.remove(c)


    #drawing

    for w in walls: #draw walls
        pygame.draw.rect(screen, GREEN, w)

    for c in coins:
        pygame.draw.rect(screen, WHITE, c)

    
    player.draw()
    # Update window
    pygame.display.update()
    clock.tick(refresh_rate)
    

# Close window and quit//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
pygame.quit()


    
