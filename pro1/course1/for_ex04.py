'''
Created on 2017. 9. 29.

@author: jihye
'''

# 원 타일 만들기

import turtle

def draw_spuarePolygon(x,y,radius,side, pencolor='black',fillcolor=''):
    mypen=turtle.Turtle()
    
    mypen.pencolor(pencolor)
    mypen.fillcolor(fillcolor)
    
    mypen.speed(0)
    mypen.hideturtle()
    
    mypen.penup()
    mypen.goto(x,y)
    mypen.pendown()
    
    mypen.pendown()
    mypen.begin_fill()
    mypen.circle(radius,steps=side)
    mypen.end_fill()
    
def main():
    
    distance=50
    radius=20
    x,y=-100,100
    
    for row in range(7):
        for col in range(row+1):
            if (row+col)%2==0:
                draw_spuarePolygon(x,y,radius,None,fillcolor='red')
            else:
                draw_spuarePolygon(x,y,radius,None,fillcolor='blue')
            x+=distance
            
        x,y = -100,y-distance   
    
    turtle.done()
    
main()
    