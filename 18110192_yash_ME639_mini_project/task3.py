import pygame
import os
import math
import random
from points import *
import formular
import time

# NOTE: All lengths are in cm   ########################

#########################################################
# INPUT
A = 12      # vertical displacement of End effector ----------(|initial y-cordinate of end effector + A| < l1+l2)
k = 100     # spring constant
#########################################################

os.environ['SDL_VIDEO_CENTERED']='1'

width, height = 600, 600
SIZE = (width, height)
pygame.init()
pygame.display.set_caption("Task 3")
fps = 100
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

def deg(theta):
    rad = (math.pi/180)*theta
    return rad

m1 = 1      #kg
m2 = 1      #kg
l1 = 100    #cm
l2 = 100    #cm

t = 0
dt = 1.5

starting_point = (width//2, height//2)

x_offset = starting_point[0]
y_offset = starting_point[1]

x_i = x_offset+0.1
y_i = y_offset - 100 - A

x = x_i
y = y_i

q1 = formular.ang_q1(abs(x-x_offset), abs(y_offset - y), l1, l2)
q2 = formular.ang_q2(abs(x-x_offset), abs(y_offset - y), l1, l2)

scatter1 = []
scatter = []

restart = False

LIST_LIMIT = 100

#COLORS
BACKGROUND = (20, 20, 20)
SCATTERLINE1 = (255, 255, 255)
SCATTERLINE2 = (255, 255, 0)
POINT = (255, 0, 0)
SMALLPOINT = (0, 255, 0)
ROD = (45, 140, 245)
ARMSTROKE = 10

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


    x = x 
    y = y_i - A*math.cos(deg(math.sqrt(k) * t)) 

    q1 = formular.ang_q1(abs(x-x_offset), abs(y_offset - y), l1, l2)
    q2 = formular.ang_q2(abs(x-x_offset), abs(y_offset - y), l1, l2)

    x1 = float(x_offset + formular.pos_x1(l1, q1))
    y1 = float(y_offset - formular.pos_y1(l1, q1))

    if abs(y - y_i) < 0.5:
        A = A - 1

    if A == 0:
        time.sleep(1)
        run = False

    t += dt

    scatter1.insert(0, (x1, y1))
    scatter.insert(0, (x, y))

    if len(scatter1) > LIST_LIMIT:
        scatter1.pop()
    if len(scatter) > LIST_LIMIT:
        scatter.pop()

    pygame.draw.line(screen, ROD, starting_point, (x1, y1), ARMSTROKE)
    pygame.draw.circle(screen, SMALLPOINT, starting_point, 10)

    pygame.draw.line(screen, ROD, (x1, y1), (x, y), ARMSTROKE)

    pygame.draw.circle(screen, POINT, (int(x), int(y)), 5)
    pygame.draw.circle(screen, SMALLPOINT, (int(x1), int(y1)), 10)

    pygame.draw.line(screen, (255,255,255), (0, height//2), (width, height//2), 1)

    pygame.draw.circle(screen, POINT, (x_i, y_i), 1)

    pygame.display.update()

pygame.quit()
