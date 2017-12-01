'''
Created on 2017. 9. 18.

@author: jihye
'''

#오륜기그리기

import turtle

def draw_circle(x,y,color,r,size=3):
    pen=turtle.Turtle()
    pen.hideturtle()
    
    
    
    pen.pensize(size)
    
    pen.pencolor(color)
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.circle(r)
    

def main():
    draw_circle(-110,-25, 'blue', 45)
    draw_circle(0,-25, 'black', 45)
    draw_circle(110,-25, 'red', 45)
    draw_circle(-55,-75, 'yellow', 45)
    draw_circle(55,-75, 'green', 45)
    
    turtle.done()
    
main()
