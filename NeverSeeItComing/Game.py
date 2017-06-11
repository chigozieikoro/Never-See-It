import pygame
import time
import random
from pygame.locals import *

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
display_width = 800
display_height = 600

size = (display_width, display_height)
high_score = 0
color_black = (0,0,0)
color_white = (255, 255, 255)
color_red = (255,0,0)
color_green = (0,255,0)
color_blue = (0,0,255)

gameDisplay = pygame.display.set_mode(size)

pygame.display.set_caption('Last Surprise')

cat_image = pygame.image.load('Morgana.png')
pygame.mixer.music.load("Last Surprise.ogg")
pygame.mixer.music.play(-1,0)
morgana_width = 125
morgana_height = 120

def blit_cat(x,y):
    gameDisplay.blit(cat_image,(x,y))

def generate_obstacle(x, y, width, height, color):
    pygame.draw.rect(gameDisplay, color, [x,y,width,height])

def jump():
    pass

def point_count(pts, color):
    score = pygame.font.SysFont(None, 25).render("Current Score: %d" %(pts), True, color)
    gameDisplay.blit(score, (600,0))



def game_over():
    push_message("Let's Not Do That Today")
def push_message(string):#puts a message on the screen when game ends
    text_to_display = pygame.font.Font('freesansbold.ttf', 70)
    text_surface, text_rectangle = text_objects(string, text_to_display)
    text_rectangle.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(text_surface, text_rectangle)
    pygame.display.update()

    time.sleep(2)
    game_loop()

def text_objects(string, font):
    surface = font.render(string, True, color_black)
    return surface, surface.get_rect()

def collision(player_x, player_y, player_w, player_h, obj_x, obj_y, obj_w, obj_h):
    if obj_x < player_x + player_w and obj_y < player_y + player_h and player_x < obj_x + obj_w and player_y < obj_y + obj_h:
        return True
    else:
        return False

def game_loop():
    x = display_width * 0.45
    y = display_height * 0.8
    y_change = 0
    x_change = 0
    score = 0
    complete = False
    initial_obstacle_x = 800
    initial_obstacle_y = 500
    obstacle_width = 100
    obstacle_height = 100
    game_speed = -10
    number_dodge = 0
    while not complete:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_SPACE:
                    pass


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        y += y_change
        x += x_change


        gameDisplay.fill(color_white)
        generate_obstacle(initial_obstacle_x,initial_obstacle_y,obstacle_width, obstacle_height, color_black)
        initial_obstacle_x += game_speed
        blit_cat(x, y)
        point_count(score, color_red)
        if initial_obstacle_x < -300: #if it goes offscreen, reset it
            score += 100
            number_dodge+=1
            jump_or_duck = random.randint(0,1)
            if(jump_or_duck == 0):
              initial_obstacle_y = 500
              #initial_obstacle_x = 800
            else:
                initial_obstacle_y = 400
            game_speed-=(number_dodge * .2)
            #initial_obstacle_y = 500
            initial_obstacle_x = 800
        if x > display_width - morgana_width or x < 0 or y < 0:
            game_over()
        if collision(x, y, morgana_width, morgana_height, initial_obstacle_x, initial_obstacle_y, obstacle_width, obstacle_height):
            game_over()

        #print(event)

        pygame.display.update()

        clock.tick(60)

game_loop()
pygame.quit()
quit()