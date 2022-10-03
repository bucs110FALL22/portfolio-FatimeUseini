import turtle 
import random
my_turtle = turtle.Turtle() #Factories
my_turtle.shape("turtle")
my_turtle.color("purple")
screen=turtle.screensize(100,100)
true= turtle.isvisible()
while true:
  if random.randrange(2)==0:
     my_turtle.left(90)
     my_turtle.forward(50)
  elif random.randrange(2)==1:
     my_turtle.right(90)
     my_turtle.forward(50)



window= turtle.Screen()
window.exitonclick()