from Rectangle import Rectangle

class Surface:
  def __init__(self, filename, x, y, height, width):
    self.rect= Rectangle(x, y, height, width)
    self.image= str(filename)
  def getRect(self):
    return self.rect
    


    