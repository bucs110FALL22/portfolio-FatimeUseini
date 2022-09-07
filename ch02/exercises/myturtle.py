import turtle
my_turtle = turtle.Turtle() #Factories
my_turtle.shape("turtle")

my_turtle.penup()
my_turtle.bk(100)
my_turtle.pendown()
my_turtle.color("purple")
num_sides =int(input("Please enter the number of sides:"))
length= 50
angle = 360/ num_sides
for i in [angle]*num_sides:
  my_turtle.forward(length)
  my_turtle.left(i)

my_turtle.penup()
my_turtle.forward(100)
my_turtle.pendown()
my_turtle.color("red")
num_sides =int(input("Please enter the number of sides:"))
length= 50
angle = 360/ num_sides
for i in [angle]*num_sides:
  my_turtle.forward(length)
  my_turtle.left(i)
window = turtle.Screen()
window.exitonclick()