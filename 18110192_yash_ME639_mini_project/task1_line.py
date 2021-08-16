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
m = 1      # slope of desired line
c = 100    # y-intercept of desired line ----------(|c| < l1+l2)
#########################################################

os.environ['SDL_VIDEO_CENTERED']='1'

width, height = 600, 600
SIZE = (width, height)
pygame.init()
pygame.display.set_caption("Task 1 (Linear Trajectory)")
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

scatter1 = []
scatter = []

restart = False

LIST_LIMIT = 300

#COLORS
BACKGROUND = (20, 20, 20)
SCATTERLINE1 = (255,255,255)
SCATTERLINE2 = (255, 255, 0)
POINT = (255, 0, 0)
SMALLPOINT = (0, 255, 0)
ROD = (45, 140, 245)
ARMSTROKE = 10

starting_point = (width//2, height//2)

x_offset = starting_point[0]
y_offset = starting_point[1]

m = -m
c = -c

y = 0
if m == 0:
    x = -100
else:
    x = -c/m

q1_i = formular.ang_q1(x, y, l1, l2)
q2_i = formular.ang_q2(x, y, l1, l2)

q1 = q1_i
q2 = q2_i

x = float(x_offset + formular.pos_x(l1, l2, q1, q2))
y = float(y_offset - formular.pos_y(l1, l2, q1, q2))

theta = 0

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
        q1 = q1_i
        q2 = q2_i
        x = float(x_offset + formular.pos_x(l1, l2, q1, q2))
        y = float(y_offset - formular.pos_y(l1, l2, q1, q2))
        scatter1 = []
        scatter = []
        restart = False

    if m < 0:
        x = x + 1
        y = y_offset + (m*(x - x_offset) + c)        
    if m >= 0:
        x = x - 1
        y = m*x + c
    
    if x == x_offset:
        x = x_offset-0.1

    q1 = formular.ang_q1((x-x_offset), (y_offset - y), l1, l2)
    q2 = formular.ang_q2((x-x_offset), (y_offset - y), l1, l2)

    x1 = float(x_offset + formular.pos_x1(l1, q1))
    y1 = float(y_offset - formular.pos_y1(l1, q1))

    p = [x_offset, y_offset]
    q = [x, y]
    dist = math.dist(p, q)

    if dist > l1+l2 - 1:
        time.sleep(1)
        restart = True

    scatter1.insert(0, (x1, y1))
    scatter.insert(0, (x, y))


    for point in scatter:
        plot = Points(point[0], point[1], screen, SCATTERLINE1, scatter)
        plot.draw()

    if len(scatter1) > LIST_LIMIT:
        scatter1.pop()
    if len(scatter) > LIST_LIMIT:
        scatter.pop()

    pygame.draw.line(screen, ROD, starting_point, (x1, y1), ARMSTROKE)
    pygame.draw.circle(screen, SMALLPOINT, starting_point, 10)

    pygame.draw.line(screen, ROD, (x1, y1), (x, y), ARMSTROKE)

    pygame.draw.circle(screen, POINT, (int(x), int(y)), 5)
    pygame.draw.circle(screen, SMALLPOINT, (int(x1), int(y1)), 10)

    pygame.draw.line(screen, (128,0,128), (0, height//2), (width, height//2), 1)
    pygame.draw.line(screen, (128,0,128), (width//2, 0), (width//2, height), 1)

    pygame.draw.circle(screen, (255, 255, 255), (x_offset, y_offset+c), 2)

    pygame.display.update()

pygame.quit()
