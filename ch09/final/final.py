import pygame
from image import Art1
from image import Art2
from book import Book1
from book import Book2

def questions():
    """
    Asks the user to type in a response to the printed question. 
    args: none
    return: returns an image based on users response
    """
    text= ("This or That? Type in 'a' or 'b' to choose response.")
    print(text)
    while True:
      q= input("Favorite season? a) fall or b) spring: ")
      global book_img
      global art_img
      if q == "a":
        book_img= Book1()
        art_img= Art1()
        break
      elif q == "b":
        book_img= Book2()
        art_img= Art2()
        break
    return book_img

def main():
   questions()
   pygame.init()
   SCREEN_SIZE = 600
   IMG_SIZE = (600, 600)
   screen = pygame.display.set_mode((SCREEN_SIZE,SCREEN_SIZE)) 
   art_file= art_img.get()
   art_image = pygame.image.load(art_file)
   art_image = pygame.transform.scale(art_image, IMG_SIZE)
   book_file= book_img.get()
   book_image = pygame.image.load(book_file)
   book_pos= book_image.get_rect(center = screen.get_rect().center)
   screen.blit(art_image, (screen.get_rect().topleft))
   screen.blit(book_image, (book_pos))
   pygame.display.flip()
   while True:
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()
            exit()
main()