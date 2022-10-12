import turtle
window = turtle.Screen()
def drawEqShape(turtleobject,num_sides=0,side_length=0):
  for i in range(num_sides):
    turtleobject.forward(side_length)
    turtleobject.left(360/num_sides)


my_turtle = turtle.Turtle()
my_turtle.color("green")
my_turtle.shape("turtle")
num_sides= int(input("How many sides?:"))
side_length= int(input("Side Length?:"))
drawEqShape(my_turtle, num_sides, side_length)
window.exitonclick()


  