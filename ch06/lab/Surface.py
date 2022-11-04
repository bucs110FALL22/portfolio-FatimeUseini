import Pygame
import Rectangle 

class Surface:
  def __init__(self, filename, x, y, h, w):
    self.rect= x,y,h,w 
    self.image= filename
  def __getRect__(self):
    Rect(self.rect)
    


    