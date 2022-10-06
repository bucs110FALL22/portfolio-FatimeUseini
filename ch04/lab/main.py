import pygame
pygame.init()
import math 
window_width=200
window_height=200
window=pygame.display.set_mode([window_width, window_height])
red= (0,255,0)
window.fill(red)

num_sides=(360)
side_length=(100)
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

BLACK= (0,0,0)
pygame.draw.rect(window, BLACK, [0, 0, 100, 100], 1)
pygame.display.flip()

pygame.draw.rect(window, BLACK, [100, 0, 100, 100], 1)
pygame.display.flip()

pygame.draw.rect(window, BLACK, [100, 100, 100, 100], 1)
pygame.display.flip()

pygame.draw.rect(window, BLACK, [0, 100, 100, 100], 1)
pygame.display.flip()
pygame.time.wait(300)