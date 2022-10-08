import pygame
import random
import math
pygame.init()
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


  
pygame.draw.circle(window, red, [100,100], 100)
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
window.fill(black)

#Part C

window_width=200
window_height=200
window=pygame.display.set_mode([window_width, window_height])
green= (0,255,0)
black= (0,0,0)
red= (255,0,0)
blue=(0,0,255)
white = (255, 255, 255)

red_button= pygame.draw.rect(window, red, [0, 0, 100, 200],)
blue_button = pygame.draw.rect(window, blue, [0, 100, 100, 200],)
pygame.display.flip()


while range(1):
  team= input("choose player red or blue:")
  mouse_x, mouse_y = pygame.mouse.get_pos()
  for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if blue_button.collidepoint(mouse_x, mouse_y):
          team ="blue"
          print("blue")
        else:
          team = "red"
          print("red")
      pygame.display.flip()
  

      
    
window.fill(black)
pygame.draw.rect(window, green, [0, 0, 200, 200],)
pygame.display.flip()
pygame.time.wait(300)
pygame.draw.circle(window, white, [100,100], 100)
pygame.draw.circle(window, black, [100,100], 100,1)
pygame.display.flip()


pygame.draw.line(window, black,[0,100],[400,100],2)
pygame.draw.line(window, black,[100,0],[100,200],2)
pygame.draw.line(window, black,[300,0],[300,200],2)
pygame.display.flip()
pygame.time.wait(3000)



howManyred = 0
howManyblue=0
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
    pygame.draw.circle(window, red, [x2, y2], 4)
    howManyred+=1
  else:
    pygame.draw.circle(window, black, [x2, y2], 4)
  pygame.display.flip()
  pygame.time.wait(100)
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
    howManyblue+=1
  else:
    pygame.draw.circle(window, black, [x2, y2], 4)
  pygame.display.flip()
  pygame.time.wait(100)

if howManyred>howManyblue:
  print("red player wins")
elif howManyred==howManyblue:
  print("red player and blue player tie")
else: 
  print("blue player wins")


      
pygame.display.flip()
pygame.time.wait(5000) 

print(howManyred, howManyblue)

 

    