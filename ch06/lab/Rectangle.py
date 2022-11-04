class Rectangle:
  def __init__(self, x=0, y=0, height=0, width=0):
    self.x= x
    self.y= y
    self.width= width
    self.height= height
    if self.x<0:
      self.x=0
    if self.y<0:
      self.y=0
    if self.width<0:
      self.width=0
    if self.height<0:
      self.height=0
  def __str__(self): 
    return str.format("(x:{},y:{}) height:{} width:{}".format(self.x, self.y, self.height, self.width,))


r = Rectangle(10, 10, 10, 10)
assert((r.x, r.y, r.height, r.width) == (10,10,10,10))
r = Rectangle(-1, 1, 1, 1)
assert((r.x, r.y, r.height, r.width) == (0,1,1,1))
r = Rectangle(1, -1, 1, 1)
assert((r.x, r.y, r.height, r.width) == (1,0,1,1))
r = Rectangle(1, 1, -1, 1)
assert((r.x, r.y, r.height, r.width) == (1,1,0,1))
r = Rectangle(1, 1, 1, -1)
assert((r.x, r.y, r.height, r.width) == (1,1,1,0))
