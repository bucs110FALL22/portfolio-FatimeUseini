import pygame
import random
pygame.init()
import math 
window_width=200
window_height=200
window=pygame.display.set_mode([window_width, window_height])
green= (0,255,0)
window.fill(green)


#Part A
black= (0,0,0)
red= (255,0,0)
blue=(0,0,255)
white = (255, 255, 255)

num_sides=(360)
side_length=(100)
offset=(100)
coords=[]
for i in range(num_sides):
  theta = (2.0 * math.pi * (i))/num_sides
  x= side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([int(x),int(y)])
circle = pygame.draw.polygon(window,red,coords,)
pygame.display.flip()


for i in range(num_sides):
  theta = (2.0 * math.pi * (i))/num_sides
  x= side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([int(x),int(y)])

circle = pygame.draw.polygon(window,black,coords,1)
pygame.display.flip()

pygame.draw.rect(window, black, [0, 0, 100, 100], 1)
pygame.display.flip()

pygame.draw.rect(window, black, [100, 0, 100, 100], 1)
pygame.display.flip()

pygame.draw.rect(window, black, [100, 100, 100, 100], 1)
pygame.display.flip()

pygame.draw.rect(window, black, [0, 100, 100, 100], 1)
pygame.display.flip()


#Part B

for i in range(10):
  x2= random.randrange(200)
  y2= random.randrange(200)
  coordinates= (x2,y2)
  x1= 100
  y1= 100
  center=(x1,y1)
  distance_from_center=math.hypot(x1-x2, y1-y2)
  is_in_circle = distance_from_center <= window_width/2
  if is_in_circle:
    pygame.draw.circle(window, blue, [x2, y2], 4)
  else:
    pygame.draw.circle(window, black, [x2, y2], 4)
  pygame.display.flip()
  pygame.time.wait(100)


pygame.time.wait(3000)

#Part C

window_width=400
window_height=400
window=pygame.display.set_mode([window_width, window_height])
green= (0,255,0)
black= (0,0,0)
red= (255,0,0)
blue=(0,0,255)
white = (255, 255, 255)


pygame.draw.rect(window, white, [0, 0, 200, 200],)
pygame.display.flip()
pygame.draw.circle(window, red, [100,100], 100)
pygame.draw.circle(window, black, [100,100], 100,1)
pygame.display.flip()

pygame.draw.rect(window, black, [200, 0, 200, 200],)
pygame.display.flip()
pygame.draw.circle(window, blue, [300,100], 100)
pygame.draw.circle(window, black, [300,100], 100,1)
pygame.display.flip()

pygame.draw.line(window, black,[0,100],[400,100],2)
pygame.draw.line(window, black,[100,0],[100,200],2)
pygame.draw.line(window, black,[300,0],[300,200],2)
pygame.display.flip()
pygame.time.wait(3000)

