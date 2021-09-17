# Your name: Cooper Drobnich
# Your student id: 84266316
# Your email:
# List who you worked with on this homework: *Looked up how to draw ellipse and half circle online

# import the turtle functions for use in this program
# don't need to use the module name
from turtle import *


def draw_scene(turtle):
    Eye(turtle, 0, -200, "white", 200)
    Eye(turtle, -50, 10, "black", 15)
    Eye(turtle, 50, 10, "black", 15)
    Eye(turtle, -50, 25, "white", 2)
    Eye(turtle, 50, 25, "white", 2)
    KingCrown(turtle, -84, 200, "gold")
    KingJewel(turtle, 8, 260, 180, "blue")
    KingJewel(turtle, -12, 260, 0, "blue")
    KingJewel(turtle, -70, 240, 90, "red")
    KingJewel(turtle, 65, 260, 270, "red")
    KingHand(turtle, -200, 0, "white", 60, 180)
    KingHand(turtle, 180, -30, "white", 60, 270)
    KingEyebrow(turtle, -50, 60, "black", 135, 30, 10)
    KingEyebrow(turtle, 45, 65, "black", 45, 30, 10)
    KingMouth(turtle, -110, -10, "red", 0)
    KingBigTeeth(turtle, -95, -12, 0, "black", "white")
    KingSmallTeeth(turtle, -35, -12, 0, "black", "white")
    KingSmallTeeth(turtle, 5, -12, 0, "black", "white")
    KingBigTeeth(turtle, 45, -12, 0, "black", "white")
    KingTongue(turtle, 0, -80, "pink", 60, 180)
    TongueLine(turtle)
    Initials(turtle, "white")
    exitonclick()
    
def Eye(turtle, xpos, ypos, color, radius):
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def KingCrown(turtle, xpos, ypos, color):
    turtle.penup()
    turtle.setheading(90)
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(90)
    for sides in range(2):
        turtle.right(120)
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(60)
    turtle.setheading(270)
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(164)
    turtle.end_fill()

def KingJewel(turtle, xpos, ypos, setheading, color):
    turtle.penup()
    turtle.setheading(setheading)
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for sides in range(3):
        turtle.forward(20)
        turtle.right(120)
    turtle.end_fill()

def KingHand(turtle, xpos, ypos, color, radius, setheading):
    turtle.penup()
    turtle.setheading(setheading)
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for index in range(2):
        turtle.circle(radius, 90)
        turtle.circle(radius//2, 90)
    turtle.end_fill()

def KingEyebrow(turtle, xpos, ypos, color, setheading, width, height):
    turtle.penup()
    turtle.setheading(setheading)
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for sides in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
def KingMouth(turtle, xpos, ypos, color, setheading):
    turtle.penup()
    turtle.setheading(setheading)
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.right(90)
    for side in range(180):
        turtle.forward(2)
        turtle.left(1)
    turtle.left(90)
    turtle.forward(230)
    turtle.end_fill()

def KingBigTeeth(turtle, xpos, ypos, setheading, outline, color):
    turtle.penup()
    turtle.setheading(setheading)
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.color(outline, color)
    turtle.begin_fill()
    for sides in range(3):
        turtle.forward(60)
        turtle.right(120)
    turtle.end_fill()

def KingSmallTeeth(turtle, xpos, ypos, setheading, outline, color):
    turtle.penup()
    turtle.setheading(setheading)
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.color(outline, color)
    turtle.begin_fill()
    for sides in range(3):
        turtle.forward(40)
        turtle.right(120)
    turtle.end_fill()

def KingTongue(turtle, xpos, ypos, color, radius, setheading):
    turtle.penup()
    turtle.setheading(setheading)
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for index in range(2):
        turtle.circle(radius, 90)
        turtle.circle(radius//2, 90)
    turtle.end_fill()
  
def TongueLine(turtle):
    turtle.penup()
    turtle.setheading(225)
    turtle.color("black")
    turtle.pensize(2)
    turtle.goto(5, -100)
    turtle.pendown()
    turtle.forward(45)  

def Initials(turtle, color):
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(250,-250)
    turtle.pendown()
    turtle.color(color)
    turtle.backward(30)
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(30)
    turtle.penup()
    turtle.goto(270,-250)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(20)
    turtle.right(45)
    turtle.forward(35)
    turtle.right(45)
    turtle.forward(20)
    turtle.right(45)
    turtle.forward(30)
    turtle.penup()



    


    
        
    
   
    
    """
    Write a function to draw a scene for a fall holiday.  For example,
    you can draw something for Halloween.

    Feel free to modify the arguments of this function as you like,
    but you should pass in the turtle object at the very least.

    You can earn extra credit for signing your
    art with your initials in block letters. See the instructions for
    more details.
    """

    pass

def main():
    space = Screen()
    KingBoo = Turtle()
    KingBoo.screen.screensize(1000,600)
    KingBoo.screen.bgcolor("black")
    KingBoo.pencolor("white")
    draw_scene(KingBoo)
    
    """

    Make sure to create a Screen object, a Turtle object,
    and call draw_scene.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting until you close the drawing window.

    TIP: You can call the .bgcolor() method on your Screen instance to change
    the background color. 
    """

    pass


# Only run the main function if this file is executed (not imported)
if __name__ == '__main__':
    main()
