import pygame
display = pygame.display.set_mode()
upper_limit=20
iters={'pos_int':'iterations'}


for n in range(2,upper_limit+1):
  pos_int=n
  num=[n]
  x=0
  count=x
  while n>1:
    x +=1
    if n%2==0:
      n = n/2
    else:
      n = 3*n+1
      num.append(n)
  iterations= x
  iters= (pos_int,iterations)
  print(iters)
  

color=(0,0,0)
coordinates= (iters)
pygame.draw.lines(display, color, False, coordinates)
new_display = pygame.transform.flip(display, False, True)
display.blit( new_display , (0, 0) )
