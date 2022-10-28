import turtle
my_turtle = turtle.Turtle()
window = turtle.Screen()
window.colormode(255)


def snowflake(size, x_pos, y_pos,l):
  angle= size*2
  my_turtle.penup()
  my_turtle.goto(x_pos,y_pos)
  my_turtle.pendown()
  blue= (137, 207, 240)
  my_turtle.color(blue)
  my_turtle.pensize(5)
  r= int(360/angle)
  for i in range (r):
    my_turtle.forward(size)
    my_turtle.left(45)
    my_turtle.forward(10)
    my_turtle.backward(10)
    my_turtle.right(90)
    my_turtle.forward(10)
    my_turtle.backward(10)
    my_turtle.left(l)
    my_turtle.backward(size)
    my_turtle.left(angle)
  
snowflake(25,0,0,45)
snowflake(20,70,10,45)
window= turtle.Screen()
window.exitonclick()    

