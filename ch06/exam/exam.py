import turtle
my_turtle = turtle.Turtle()
window = turtle.Screen()
window.colormode(255)
white= (255,255,255)
blue1= (11,20,50)
blue2= (137,207,240)
turtle.Screen().bgcolor(blue2)
my_turtle.color(white)

radius= 4
def heart():
  my_turtle.color(blue1)
  my_turtle.left(45)
  my_turtle.forward(10)
  my_turtle.backward(10)
  my_turtle.right(90)
  my_turtle.forward(10)
  my_turtle.circle(radius,220)
  my_turtle.left(180)
  my_turtle.circle(radius,220)
  my_turtle.left(45)

def angle(num_branch):
  angle=(360/num_branch)
  return angle
  return num_branch

def heart_snowflake(size, x_pos, y_pos,angle, num_branch):
  my_turtle.pensize(3)
  my_turtle.penup()
  my_turtle.goto(x_pos,y_pos)
  my_turtle.pendown()
  for i in range (num_branch-1):
    my_turtle.forward(size)
    heart()
    my_turtle.color(white)
    my_turtle.penup()
    my_turtle.goto(x_pos,y_pos)
    my_turtle.pendown()
    my_turtle.left(angle)
        
def main():
  heart_snowflake(25,0,10,angle(8),8)
main()

window= turtle.Screen()
window.exitonclick()    

