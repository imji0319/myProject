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
    
    screen=turtle.Screen()
    
    #turtle의 화살표를 이미지를 사용할 경우 
    #screen 에 addshape으로 이미지를 등록해야함 
    #여러 이미지를 저장할때 리스트를 활용
    #이미지를 활용할때 리스트의 인덱스를 활용하여 씀 즉 따로 변수에 할당할 필요가 없어짐 
    images=['image/right_open.gif' ,'image/right_close.gif' ,'image/left_open.gif','image/left_close.gif','image/die.gif','image/up_open.gif','image/up_close.gif','image/down_open.gif','image/down_close.gif']
    
    for image in images:
        screen.addshape(image)
    

    pacman.shape(images[0])
    pacman.pensize(3)
    pacman.pencolor('red')
    pacman.speed(1)
    

    count=0
    w_position=0
    edge=n//2
    h_position=0

    
    while -edge <= w_position <= edge and -edge <= h_position <= edge:
        
            
        where = randint(1,4)
        rpt=5
        delta=size/rpt
        
        if where==1 : # to rightward
            
            pacman.setheading(0)
            w_position+=1
                       
            for  t in range(rpt):
                if t%2 ==0:
                    pacman.shape(images[0])
                else:
                    pacman.shape(images[1])
                
                pacman.forward(delta)
        
        
        elif where==2 : # to leftward
            w_position-=1
            pacman.setheading(180)
        
            for  t in range(rpt):
                if t%2 ==0:
                    pacman.shape(images[2])
                else:
                    pacman.shape(images[3])
                
                pacman.forward(delta)
        
        elif where==3 :  # to up
            h_position+=1
            pacman.setheading(90)
        
            for  t in range(rpt):
                if t%2 ==0:
                    pacman.shape(images[5])
                else:
                    pacman.shape(images[6])
                
                pacman.forward(delta)
        elif where==4 : 
            h_position-=1
            pacman.setheading(270)
        
            for  t in range(rpt):
                if t%2 ==0:
                    pacman.shape(images[7])
                else:
                    pacman.shape(images[8])
                                
                pacman.forward(delta)
        count+=1
        
    pacman.shape(images[4]) 
    
    print (' 총 이동 횟수 : %d ' %count )     
        
    
    

def main():
    num_tile=5
    size_tile=50
    
    w= 650
    h= 650
    
    wn=turtle.Screen()
    wn.screensize(w,h)
    
    
    draw_board(num_tile,size_tile)
    start_randomwalk(num_tile, size_tile)
    turtle.done()
    
    
main()



        
