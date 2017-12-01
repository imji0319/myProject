'''
Created on 2017. 9. 18.

@author: jihye
'''


import turtle

def draw_rectangle(x,y,w,h):
    myPen=turtle.Turtle()
    myPen.hideturtle()
    myPen.penup()
    myPen.goto(x,y)
    myPen.pendown()
    myPen.forward(w)
    myPen.left(90)
    myPen.forward(h)
    myPen.left(90)
    myPen.forward(w)
    myPen.left(90)
    myPen.forward(h)

    
draw_rectangle(-100,100,50,50)
draw_rectangle(-50,100,50,50)
draw_rectangle(0,100,50,50)
draw_rectangle(50,100,50,50)
    
turtle.done()