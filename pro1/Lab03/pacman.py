'''
Created on 2017. 9. 27.

@author: jihye
'''

import turtle
from random import randint 

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




def draw_board(n,size):
    x= -(n//2)*size-size//2
    y= -size//2
    
    for t in range(n):
        draw_rectangle(x,y,size,size)
        x += size
        
        
def start_randomwalk(n,size): 
    
    pacman=turtle.Turtle()
    
    #turtle의 화살표를 이미지를 사용할 경우 
    #screen 에 addshape으로 이미지를 등록해야함 
    image_rightOpen='image/right_open.gif'  #같은 페키지에 들어있는 이미지를 가져올 경우 
    image_leftOpen='image/left_open.gif'
    image_rightClose='image/right_close.gif'  #같은 페키지에 들어있는 이미지를 가져올 경우 
    image_leftClose='image/left_close.gif'
    image_die='image/die.gif'
    
    screen=turtle.Screen()
    screen.addshape(image_rightOpen)
    screen.addshape(image_leftOpen)
    screen.addshape(image_rightClose)
    screen.addshape(image_leftClose)
    screen.addshape(image_die)
    
    
    pacman.shape(image_rightOpen)
    pacman.speed(1)
    pacman.penup()
    
    position=0 
    edge=n//2
    
    while -edge <= position <= edge:
        where = randint(0,1)
        rpt=5
        delta=size/rpt
        
        if where==0: # to rightward
            
            pacman.setheading(0)
            position+=1
            
                    
            for  t in range(rpt):
                if t%2 ==0:
                    pacman.shape(image_rightOpen)
                else:
                    pacman.shape(image_rightClose)
                
                pacman.forward(delta)
             
        else: # to leftward
            position-=1
            pacman.setheading(180)
        
            for  t in range(rpt):
                if t%2 ==0:
                    pacman.shape(image_leftOpen)
                else:
                    pacman.shape(image_leftClose)
                
                pacman.forward(delta)
                    
    pacman.shape(image_die)      
        
    
    

def main():
    num_tile=5
    size_tile=50
    
    w= (num_tile + 3 )*size_tile + 50
    h= size_tile*3
    
    turtle.setup(w,h)
    
    draw_board(num_tile,size_tile)
    start_randomwalk(num_tile, size_tile)
    turtle.done()
    
main()