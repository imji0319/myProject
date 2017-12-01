'''
Created on 2017. 10. 11.

@author: jihye
'''

import turtle

def draw_rectangle(x,y,w,h,edge_color='black',fill_color=''):
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
