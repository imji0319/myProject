'''
Created on 2017. 9. 29.

@author: jihye
'''

# 프로그래밍 과제 3 << Random Walk >> _ 20140543 임지혜

import turtle
from random import randint

def draw_rectangle(x,y,w,h,pensize=1, edge_color='black', fill_color = ''):
    mypen=turtle.Turtle()
    mypen.speed(0)
    mypen.hideturtle()
    
    mypen.pencolor(edge_color)
    mypen.pensize(pensize)
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
    
def draw_board(n,size):

    x= -(n//2)*size-size//2
    y= (n//2)*size-size//2
    
    
    for row in range(n):
        for col in range(n):
            
            draw_rectangle(x,y,size,size)
            x+=size
            
        x,y=-(n//2)*size-size//2,y-size
        
        

def start_randomwalk(n,size): 
    
    pacman=turtle.Turtle()
    
    #turtle의 화살표를 이미지를 사용할 경우 
    #screen 에 addshape으로 이미지를 등록해야함 
    image_rightOpen='image/right_open.gif'  #같은 페키지에 들어있는 이미지를 가져올 경우 
    image_leftOpen='image/left_open.gif'
    image_rightClose='image/right_close.gif'  #같은 페키지에 들어있는 이미지를 가져올 경우 
    image_leftClose='image/left_close.gif'
    image_die='image/die.gif'
    image_upOpen='image/up_open.gif'
    image_upClose='image/up_close.gif'
    image_downOpen='image/down_open.gif'
    image_downClose='image/down_close.gif'
    
    screen=turtle.Screen()
    screen.addshape(image_rightOpen)
    screen.addshape(image_leftOpen)
    screen.addshape(image_rightClose)
    screen.addshape(image_leftClose)
    screen.addshape(image_die)
    screen.addshape(image_upOpen)
    screen.addshape(image_upClose)
    screen.addshape(image_downOpen)
    screen.addshape(image_downClose)
    
    
    
    pacman.shape(image_rightOpen)
    pacman.pensize(3)
    pacman.pencolor('red')
    pacman.speed(1)
    
    
    count=0
    w_position=0 
    w_edge=n//2
    h_position=0
    h_edge=n//2
    
    while -w_edge <= w_position <= w_edge and -h_edge <= h_position <= h_edge:
        
            
        where = randint(1,4)
        rpt=5
        delta=size/rpt
        
        if where==1: # to rightward
            
            pacman.setheading(0)
            w_position+=1
                       
            for  t in range(rpt):
                if t%2 ==0:
                    pacman.shape(image_rightOpen)
                else:
                    pacman.shape(image_rightClose)
                
                pacman.forward(delta)
        
        
        elif where==2: # to leftward
            w_position-=1
            pacman.setheading(180)
        
            for  t in range(rpt):
                if t%2 ==0:
                    pacman.shape(image_leftOpen)
                else:
                    pacman.shape(image_leftClose)
                
                pacman.forward(delta)
        
        elif where==3:  # to up
            h_position+=1
            pacman.setheading(90)
        
            for  t in range(rpt):
                if t%2 ==0:
                    pacman.shape(image_upOpen)
                else:
                    pacman.shape(image_upClose)
                
                pacman.forward(delta)
        else: 
            h_position-=1
            pacman.setheading(270)
        
            for  t in range(rpt):
                if t%2 ==0:
                    pacman.shape(image_downOpen)
                else:
                    pacman.shape(image_downClose)
                                
                pacman.forward(delta)
        count+=1
        
    pacman.shape(image_die) 
    
    print (' 총 이동 횟수 : %d ' %count )     
        
    
    

def main():
    num_tile=11
    size_tile=50
    
    w= 650
    h= 650
    
    wn=turtle.Screen()
    wn.screensize(w,h)
    
    
    draw_board(num_tile,size_tile)
    start_randomwalk(num_tile, size_tile)
    turtle.done()
    
    
main()



        
