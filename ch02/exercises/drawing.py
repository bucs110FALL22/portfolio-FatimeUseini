import turtle
myturtle = turtle.Turtle() #Factories
myturtle.shape("turtle")

color= input("Pick Color?:")
myturtle.color(color)
sides= int(input("Please input the number of sides: "))
length= int(input("Input side length:"))
angle= 360/sides
for i in range(sides):
 myturtle.forward(length)
 myturtle.left(angle)
window = turtle.Screen()
window.exitonclick()