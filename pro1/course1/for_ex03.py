'''
Created on 2017. 9. 29.

@author: jihye
'''

#꽃잎 그리기
# -*- coding : utf-8 -*-

import turtle

#꽃잎 하나 그리기 
def draw_petal(pen, r, angle):
    pen.speed(0)
    for i in range(2):
        pen.begin_fill()
        pen.circle(r, extent=angle)
        pen.left(180-angle)
        pen.end_fill()
        
def draw_flower(pos, n, r, angle, color):
    
    pen=turtle.Turtle()
    pen.fillcolor(color)
    pen.speed(1)
    pen.hideturtle()
    
    pen.penup()
    pen.forward(pos)
    pen.pendown()
    for i in range(n):
        draw_petal(pen, r, angle)
        pen.left(360/n)
        
def main():
    draw_flower(-200,6,200,30,'red')
    draw_flower(0,9,120,45,'pink')
    draw_flower(200,12,100,60,'violet')
    
    turtle.done()
    
main()
