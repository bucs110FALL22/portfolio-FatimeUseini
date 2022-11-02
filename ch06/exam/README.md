# CS110 Midterm Exam 
## SHORT DESCRIPTION: The program creates three heart snowflakes that can be altered in size. 
## KNOWN BUGS AND INCOMPLETE PARTS: N/A
## REFERENCES: N/A
## MISCELLANEOUS COMMENTS: N/A

import turtle
my_turtle = turtle.Turtle()
window = turtle.Screen()
window.colormode(255)
WHITE= (255,255,255)
PURPLE= (200,150,220)
BLUE= (137,207,240)
turtle.Screen().bgcolor(BLUE)
my_turtle.speed(100)

radius= 4
def heart():
  my_turtle.color(PURPLE)
  my_turtle.left(45)
  my_turtle.forward(10)
  my_turtle.backward(10)
  my_turtle.right(90)
  my_turtle.forward(10)
  my_turtle.circle(radius,225)
  my_turtle.left(180)
  my_turtle.circle(radius,225)
  my_turtle.left(135)
  
def angle(num_branch):
  angle=(360/num_branch)
  return angle
  return num_branch
  
def heart_snowflake(size, x_pos, y_pos, angle,num_branch):
  my_turtle.pensize(3)
  my_turtle.penup()
  my_turtle.goto(x_pos,y_pos)
  my_turtle.pendown()
  for i in range (0,num_branch):
    my_turtle.color(WHITE)
    my_turtle.forward(size)
    heart()
    my_turtle.penup()
    my_turtle.goto(x_pos,y_pos)
    my_turtle.pendown()
    my_turtle.left(angle)
        
def main():
  heart_snowflake(40,0,10,angle(8),8)
  heart_snowflake(10,-100,10,angle(5),5)
  heart_snowflake(10,100,10,angle(5),5)
  my_turtle.hideturtle()
main()

window.exitonclick()    
