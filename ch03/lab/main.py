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
side_length=(10)
offset=(10)
for i in range(1):
  theta = (2.0 * math.pi * (i))/num_sides
  x1 = side_length * math.cos(theta) + offset
  y1 = side_length * math.sin(theta) + offset
  theta = (2.0 * math.pi * (i))/num_sides
  x2 = side_length * math.cos(theta) + offset
  y2 = side_length * math.sin(theta) + offset
  theta = (2.0 * math.pi * (i))/num_sides
  x3 = side_length * math.cos(theta) + offset
  y3 = side_length * math.sin(theta) + offset
coords=[(x1,y1),(x2,y2),(x3,y3)]
black= (0,0,0)
pygame.draw.polygon(window,black,coords)

  