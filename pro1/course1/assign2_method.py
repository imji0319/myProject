'''
Created on 2017. 9. 27.

@author: jihye
'''


import turtle

from math import sqrt


def draw_line(x1,y1,x2,y2,color='black'):
    
    mypen=turtle.Turtle()
    mypen.color(color)
    
    mypen.penup()
    mypen.goto(x1,y1)
    
    mypen.pendown()
    mypen.goto(x2,y2)
    
    mypen.hideturtle()
    
def draw_squarePolygon(x,y,radius, side=None, edge_color='black',fill_color = None, degree=0):
    
    mypen=turtle.Turtle()
    mypen.begin_fill()
    mypen.pencolor(edge_color)
    mypen.fillcolor(fill_color)
    
    mypen.penup()
    mypen.goto(x,y)
    mypen.setheading(degree)
    mypen.pendown()
    
    mypen.circle(radius,steps=side)
    mypen.end_fill()
    mypen.hideturtle()
    

def draw_rectangle(x,y,w,h,edge_color='black', fill_color='None'):
    mypen=turtle.Turtle()
    mypen.begin_fill()
    mypen.pencolor(edge_color)
    mypen.fillcolor(fill_color)
    
    mypen.penup()
    mypen.goto(x,y)
    mypen.pendown()
    
    mypen.forward(w)
    mypen.left(90)
    mypen.forward(h)
    mypen.left(90)
    mypen.forward(w)
    mypen.left(90)
    mypen.forward(h)
    
    mypen.end_fill()
    mypen.hideturtle()

