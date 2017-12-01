'''
Created on 2017. 9. 30.

@author: jihye
'''

#random_walk turtle  

import turtle
from random import randint as randi


def rectangle(x,y,w,h,pencolor='black', fillcolor=''):
    
    pen=turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.pencolor(pencolor)
    pen.fillcolor(fillcolor)
    
    pen.begin_fill()
    pen.forward(w)
    pen.left(90)
    pen.forward(h)
    pen.left(90)
    pen.forward(w)
    pen.left(90)
    pen.forward(h)
    
    pen.end_fill()
    
    
def board(n,size):
    x=-(n-1)//2*size
    y=(n-1)//2*size
    
    for i in range(n):
        for j in range(n):
            rectangle(x,y,size,size)
            x+=size
        x=-(n//2)*size ; y-=size

def randomwalk(n,size):
    pen=turtle.Turtle()
    pen.shape('turtle')
    pen.pensize(3)
    
    w_pos=0
    w_edge=n//2
    h_pos=0
    h_edge=n//2
    
    while -w_edge<=w_pos<=w_edge and -h_edge<=h_pos<=h_edge:
        where= randi(1,4)
        
        if where==1:
            pen.setheading(0)
            w_pos+=1
            
        elif where==2:
            pen.setheading(90)
            h_pos+=1
        
        elif where==3:
            pen.setheading(180)
            w_pos-=1
            
        else:
            pen.setheading(270)
            h_pos-=1
        
        pen.forward(size)
    

def main():
    n=10
    size=50
    
    wn=turtle.Screen()
    wn.screensize(600,600)
    
    board(n,size)
    randomwalk(n,size)
    
    turtle.done()
    
main()