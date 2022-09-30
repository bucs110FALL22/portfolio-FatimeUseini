import turtle #1. import modules
import random

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
x = random.randrange(0,101)
michelangelo.forward(x)
michelangelo.goto(-100,20)
leonardo.forward(x)
leonardo.goto(-100,-20)

for i in range(20):
  x = random.randrange(0,11)
  michelangelo.forward(x)
  leonardo.forward(x)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
window.exitonclick()

# PART B - complete part B here
import pygame
pygame.init()
WINDOW_SIZE=[300,300]
window = pygame.display.set_mode(WINDOW_SIZE)
green= (0,255,0)
window.fill(green)
import math 

num_sides=(3)
side_length=(40)
offset=(100)
coords=[]
for i in range(num_sides):
  theta = (2.0 * math.pi * (i))/num_sides
  x= side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([int(x),int(y)])
red= (255,0,0)
square = pygame.draw.polygon(window,red,coords,2)
pygame.display.flip()
pygame.time.wait(300)
window.fill(green)

num_sides=(4)
side_length=(40)
offset=(100)
coords=[]
for i in range(num_sides):
  theta = (2.0 * math.pi * (i))/num_sides
  x= side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([int(x),int(y)])
red= (255,0,0)
square = pygame.draw.polygon(window,red,coords,2)
pygame.display.flip()
pygame.time.wait(300)
window.fill(green)

num_sides=(6)
side_length=(40)
offset=(100)
coords=[]
for i in range(num_sides):
  theta = (2.0 * math.pi * (i))/num_sides
  x= side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([int(x),int(y)])
red= (255,0,0)
square = pygame.draw.polygon(window,red,coords,2)
pygame.display.flip()
pygame.time.wait(300)
window.fill(green)

num_sides=(9)
side_length=(40)
offset=(100)
coords=[]
for i in range(num_sides):
  theta = (2.0 * math.pi * (i))/num_sides
  x= side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([int(x),int(y)])
red= (255,0,0)
square = pygame.draw.polygon(window,red,coords,2)
pygame.display.flip()
pygame.time.wait(300)
window.fill(green)

num_sides=(360)
side_length=(40)
offset=(100)
coords=[]
for i in range(num_sides):
  theta = (2.0 * math.pi * (i))/num_sides
  x= side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([int(x),int(y)])
red= (255,0,0)
square = pygame.draw.polygon(window,red,coords,2)
pygame.display.flip()
pygame.time.wait(300)