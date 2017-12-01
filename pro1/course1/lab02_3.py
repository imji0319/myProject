# -*- coding : utf-8 -*-
'''
Created on 2017. 9. 20.

@author: jihye
'''

#강의자료 – 매개변수를 사용한 함수 정의 연습 문제를 프로그램하시오.

import turtle

def draw_line(x1,y1,x2,y2, pen_color='black'):
    
    mypen=turtle.Turtle()
    mypen=color(pen_color)
    
    mypen.penup()
    mypen.goto(x1,y1)
    
    mypen.pendown()
    mypen.goto(x2,y2)
    
    mypen.hideturtle()
    


def draw_squarePloygon(x,y, radius, side, pen_color='black', fill_color=None):
    
    mypen=turtle.Turtle()
    mypen.pencolor(pen_color)
    mypen.fillcolor(fill_color)
    
    mypen.penup()
    mypen.goto(x,y)
    mypen.pendown()
    
    mypen.circle(radius,steps=side)
    mypen.hideturtle()
    

def draw_rectangle(x,y,w,h,pen_color='black',fill_color=None):
    
    mypen=turtle.Turtle()
    mypen.pencolor(pen_color)
    mypen.fillcolor(fill_color)
    
    mypen.penup()
    mypen.goto(x,y)
    mypen.pendown()
    
    
def main():
    
    
    