class Character(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("")
    self.rect = self.image.get_rect()
    self.x = self.rect.x
    self.y = self.rect.y
    self.damage = 60
    self.speed = 5 

  def pos (self):
    return f"{self.x, self.y}"
  def moveLeft (self):
    if keyPressed("left"):
      self.x -=1
  def moveRight (self):
    if keyPressed("right"):
      self.x +=1
  def moveDown(self):
    if keyPressed("down"):
      self.y -=1
  def moveUp(self):
    if keyPressed("up"):
      self.y +=1 


class Enemy:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.image = ""
    self.rect = self.image.get_rect()
    self.health = 100
    self.alive = True
  def pos (self):
    return f"{self.x, self.y}"

