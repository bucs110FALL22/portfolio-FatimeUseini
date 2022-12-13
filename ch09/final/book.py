import io
from urllib.request import urlopen

class Book1():
  def __init__(self):
     """
     Initialize class and gives an image url.
     args: self
     return: N/A
     """
     self.api_url= str('https://covers.openlibrary.org/b/isbn/9780141331973-M.jpg')
  def get(self):
    """
    Opens url and converts it into an image. 
    args: self
    return: returns an image
    """
    img = urlopen(self.api_url).read()
    book_file = io.BytesIO(img)
    return book_file
    
class Book2():
  def __init__(self):
     """
     Initialize class and gives an image url.
     args: self
     return: N/A
     """
     self.api_url= str('https://covers.openlibrary.org/b/isbn/9780141377094-M.jpg')
  def get(self):
    """
    Opens url and converts it into an image. 
    args: self
    return: returns an image
    """
    img = urlopen(self.api_url).read()
    book_file = io.BytesIO(img)
    return book_file
    
