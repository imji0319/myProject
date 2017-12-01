# -*- coding: utf-8 -*-
'''
Created on 2017. 9. 23.

@author: jihye
'''
#프로그래밍 과제 2 _ 20140543 임지
#생일축하메세지와 생일축하케익 


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
    
def draw_squarePolygon(x,y,radius, side=None, edge_color='black',fill_color = '', degree=0):
    
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
    

def draw_rectangle(x,y,w,h,edge_color='black', fill_color = ''):
    mypen=turtle.Turtle()
    
    mypen.pencolor(edge_color)
    mypen.fillcolor(fill_color)
    mypen.begin_fill()
    
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


def draw_star(x,y,size, edge_color='black', fill_color=''):
    
    mypen=turtle.Turtle()
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


    draw_rectangle(-200,-150,400,150,fill_color='dark orange')
    draw_rectangle(-150,0,300,100,fill_color='DodgerBlue3')
    draw_rectangle(-100,100,200,100,fill_color='DodgerBlue3')
    draw_rectangle(-50,200,100,50,fill_color='yellow2')
    draw_rectangle(-25,250,50,50,fill_color='yellow2')
    
    draw_squarePolygon(-150,0,75*sqrt(3)/3,side=3,fill_color='dark green',degree = 240)
    draw_squarePolygon(-75,0,75*sqrt(3)/3,side=3,fill_color='dark green',degree = 240)
    draw_squarePolygon(0,0,75*sqrt(3)/3,side=3,fill_color='dark green',degree = 240)
    draw_squarePolygon(75,0,75*sqrt(3)/3,side=3,fill_color='dark green',degree = 240)
    
    draw_squarePolygon(-175,0,25,fill_color='red')
    draw_squarePolygon(175,0,25,fill_color='red')
    
    draw_star(0,300,75,fill_color='light green')

    
    turtle.done()
    
    
main()
    
    