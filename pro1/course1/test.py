'''
Created on 2017. 9. 26.

@author: jihye
'''


import turtle

from math import sqrt


def draw_line(mypen,x1,y1,x2,y2,color='black'):
    
    mypen.color(color)
    
    mypen.penup()
    mypen.goto(x1,y1)
    
    mypen.pendown()
    mypen.goto(x2,y2)
    
    mypen.hideturtle()
    
def draw_squarePolygon(mypen,x,y,radius, side=None, edge_color='black',fill_color = None, degree=0):
    
    
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
    

def draw_rectangle(mypen,x,y,w,h,edge_color='black', fill_color='None'):
    
    
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


def draw_star(mypen,x,y,size, edge_color='black', fill_color=None):
    
    
    mypen.pencolor(edge_color)
    mypen.fillcolor(fill_color)
    
    mypen.setheading(108)
    mypen.penup()
    mypen.goto(x,y)
    mypen.pendown()
    mypen.begin_fill()
    
    
    for i in range(5):
        mypen.forward(size)
        mypen.right(144)

    mypen.end_fill()
    mypen.hideturtle()
    


def main():

    wn=turtle.Screen()
    
    wn.screensize(1500,1500) 
    
    mypen=turtle.Turtle()


    draw_rectangle(mypen,-200,-150,400,150,fill_color='dark orange')
    draw_rectangle(mypen,-100,100,200,100,fill_color='DodgerBlue3')
    draw_rectangle(mypen,-50,200,100,50,fill_color='yellow2')
    draw_rectangle(mypen,-25,250,50,50,fill_color='yellow2')
    
    draw_squarePolygon(mypen,-150,0,75*sqrt(3)/3,side=3,fill_color='dark green',degree = 240)
    draw_squarePolygon(mypen,-75,0,75*sqrt(3)/3,side=3,fill_color='dark green',degree = 240)
    draw_squarePolygon(mypen,0,0,75*sqrt(3)/3,side=3,fill_color='dark green',degree = 240)
    draw_squarePolygon(mypen,75,0,75*sqrt(3)/3,side=3,fill_color='dark green',degree = 240)
    
    draw_squarePolygon(mypen,-175,0,25,fill_color='red')
    draw_squarePolygon(mypen,175,0,25,fill_color='red')
    
    draw_star(mypen,0,300,75,fill_color='light green')

    
    
    turtle.done()
    
main()
    
    