import pygame
import os
import math
import random
from points import *
import formular
import time

# NOTE: All lengths are in cm   ########################

os.environ['SDL_VIDEO_CENTERED']='1'

width, height = 600, 600
SIZE = (width, height)
pygame.init()
pygame.display.set_caption("Task 2")
fps = 30
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

def deg(theta):
    rad = (math.pi/180)*theta
    return rad

m1 = 1      #kg
m2 = 1      #kg
l1 = 100    #cm
l2 = 100    #cm

q1 = 1
q2 = 45

scatter1 = []
scatter = []

restart = False

#COLORS
BACKGROUND = (20, 20, 20)
SCATTERLINE1 = (255, 255, 255)
SCATTERLINE2 = (255, 255, 0)
POINT = (255, 0, 0)
SMALLPOINT = (0, 255, 0)
ROD = (45, 140, 245)
ARMSTROKE = 10

starting_point = (width//2, height//2)

x_offset = starting_point[0]
y_offset = starting_point[1]

Fx = 1
Fy = 1

T1 = round(formular.Torque_1(Fx, Fy, l1/100, q1), 3)
T2 = round(formular.Torque_1(Fx, Fy, l2/100, q2), 3)

font = pygame.font.Font('freesansbold.ttf', 16)
text_T1 = font.render('Torque T1 = {}'.format(T1), True, (0,255,0), (0,0,0))
text_T2 = font.render('Torque T2 = {}'.format(T2), True, (0,255,0), (0,0,0))
textRect_T1 = text_T1.get_rect()
textRect_T2 = text_T2.get_rect()
textRect_T1.center = (x_offset//2, 2.5*y_offset//2)
textRect_T2.center = (x_offset//2 - 7, 2.7*y_offset//2)

text_wall = font.render('Wall', True, (0,0,255), (0,0,0))
textRect_wall = text_wall.get_rect()
textRect_wall.center = (starting_point[0]-130, y_offset//2)

run = True

while run:
    clock.tick(fps)

    screen.fill(BACKGROUND)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_r:
                restart = True

    if restart == True:
        q1 = 1
        q2 = 45
        scatter1 = []
        scatter = []
        restart = False


    x = float(x_offset + formular.pos_x(l1, l2, q1, q2))
    y = float(y_offset - formular.pos_y(l1, l2, q1, q2))
    
    x1 = float(x_offset + formular.pos_x1(l1, q1))
    y1 = float(y_offset - formular.pos_y1(l1, q1))

    q1 += 1.3
    q2 += 2
    screen.blit(text_T1, textRect_T1)
    screen.blit(text_T2, textRect_T2)
    screen.blit(text_wall, textRect_wall)
    if starting_point[0]-100 - 5 < x < starting_point[0]-100 + 5:
        time.sleep(1)
        restart = True

    scatter1.insert(0, (x1, y1))
    scatter.insert(0, (x, y))

    pygame.draw.line(screen, ROD, starting_point, (x1, y1), ARMSTROKE)
    pygame.draw.circle(screen, SMALLPOINT, starting_point, 10)


    pygame.draw.line(screen, ROD, (x1, y1), (x, y), ARMSTROKE)

    pygame.draw.circle(screen, POINT, (int(x), int(y)), 5)
    pygame.draw.circle(screen, SMALLPOINT, (int(x1), int(y1)), 10)

    #wall
    pygame.draw.line(screen, (0,0,255), (starting_point[0]-100, starting_point[1]),
                    (starting_point[0]-100, starting_point[1]-250), ARMSTROKE)

    pygame.draw.line(screen, (255,255,255), (0, height//2), (width, height//2), 1)

    pygame.display.update()

pygame.quit()
