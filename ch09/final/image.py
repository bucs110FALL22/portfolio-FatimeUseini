import io
from urllib.request import urlopen

class Art1():
  def __init__(self):   
     """
     Initialize class and gives an image url.
     args: self
     return: N/A
     """
     self.api_url= "https://images.metmuseum.org/CRDImages/ep/original/DT1567.jpg"
  def get(self):
    """
    Opens url and converts it into an image. 
    args: self
    return: returns an image
    """
    img = urlopen(self.api_url).read()
    art_file = io.BytesIO(img)
    return art_file
    
class Art2():
  def __init__(self): 
     """
     Initialize class and gives an image url.
     args: self
     return: N/A
     """
     self.api_url= "https://images.metmuseum.org/CRDImages/dp/original/DP802556.jpg"
  def get(self):
    """
    Opens url and converts it into an image. 
    args: self
    return: returns an image
    """
    img = urlopen(self.api_url).read()
    art_file = io.BytesIO(img)
    return art_file