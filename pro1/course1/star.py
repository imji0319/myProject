'''
Created on 2017. 9. 25.

@author: jihye
'''

import turtle
def draw_star(x,y,size=50,pencolor='black'):
    mypen=turtle.Turtle()
    mypen.showturtle()
    mypen.color(pencolor)
    
    mypen.penup()
    mypen.goto(x,y)
    mypen.pendown()
    mypen.begin_fill()
    
    for n in range(5):
        mypen.forward(size)
        mypen.right(144)
        
    mypen.end_fill()
    mypen.hideturtle()
    
def main():
    draw_star(50,50)
    
    turtle.done()
    
main()