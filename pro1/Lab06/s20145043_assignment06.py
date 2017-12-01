'''
Created on 2017. 10. 23.

@author: jihye
'''
#프로그래밍 과제 6 _ 20140543 임지혜 

import turtle
from random import randint


def tile_position(tile):
    tile_data=open(tile,'r')
    tile_position_str=tile_data.read()

    tile_str_position=tile_position_str.split(',')
    tile_position=[]
    for tile in tile_str_position:
        tile=tile.replace('(','')
        tile=tile.replace(')','')
        
        tmp=tile.split()
        tmp[0] ,tmp[1] = int(tmp[0]) , int(tmp[1])
        tile_position.append(tuple(tmp))
    
    tile_data.close()
    return tile_position
    
    
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

def draw_board(tile_pos,tile_size,tile_num): 
    # 흑백타일 만들기
    # tile_position 에 해당하면 검은색 파일 
    #절대적 위치 
    x= -(tile_num//2)*tile_size-tile_size//2
    y= (tile_num//2)*tile_size-tile_size//2
    #논리적 위치 
    x_pos=-(tile_num//2)
    y_pos=tile_num//2
    
    for row in range(tile_num):
        for col in range(tile_num):
            if (x_pos,y_pos) in tile_pos:
                draw_rectangle(x,y,tile_size,tile_size,fill_color='black')
            else:
                draw_rectangle(x,y,tile_size,tile_size)
            x+=tile_size
            x_pos+=1
        
        x_pos,y_pos=-(tile_num//2),y_pos-1    
        x,y=-(tile_num//2)*tile_size-tile_size//2,y-tile_size
        
def gem_find_randomwalk(tile_pos,size,n):
    #tile_pos : 미로 파일 
   
    
    images=['image/right_open.gif' ,'image/right_close.gif' ,'image/left_open.gif','image/left_close.gif','image/die.gif','image/up_open.gif','image/up_close.gif','image/down_open.gif','image/down_close.gif','image/goldbox.gif']

    pacman=turtle.Turtle()  
    screen=turtle.Screen()
    
    
    for image in images:
        screen.addshape(image)

    pacman.shape(images[0])
    pacman.penup()
    pacman.speed(1)
    pacman.goto(-(n//2)*size,(n//2)*size)
    

    count=0

    pacman_position = [-(n//2),n//2] 
    gem_position=((n//2),-(n//2))
    edge=(n//2)
    
    
    while tuple(pacman_position) != gem_position:

        where = randint(1,4)
        rpt=5
        
        delta=size/rpt

        if where==1  and -edge <= pacman_position[0]+1 <= edge and -edge <= pacman_position[1] <= edge and  (pacman_position[0]+1,pacman_position[1]) not in tile_pos: # to rightward
            
            pacman.setheading(0)
            for  t in range(rpt):
                if t%2 ==0:
                    pacman.shape(images[0])
                else:
                    pacman.shape(images[1])
                    
                pacman.forward(delta)
                
            pacman_position[0]+=1
            
        
        elif where==2  and -edge <= pacman_position[0] -1 <= edge and -edge <= pacman_position[1] <= edge and  (pacman_position[0]-1,pacman_position[1]) not in tile_pos: # to leftward
            
            pacman.setheading(180)
            for  t in range(rpt):
                if t%2 ==0:
                    pacman.shape(images[2])
                else:
                    pacman.shape(images[3])
                    
                pacman.forward(delta)
                
            pacman_position[0]-=1
        
        elif where==3  and -edge <= pacman_position[0] <= edge and -edge <= pacman_position[1]+1 <= edge and  (pacman_position[0],pacman_position[1]+1) not in tile_pos:  # to up
            
            pacman.setheading(90)
            for  t in range(rpt):
                if t%2 ==0:
                    pacman.shape(images[5])
                else:
                    pacman.shape(images[6])
                pacman.forward(delta)
            pacman_position[1]+=1
            
            
            
        elif where==4  and -edge <= pacman_position[0] <= edge and -edge <= pacman_position[1]-1 <= edge and  (pacman_position[0],pacman_position[1]-1) not in tile_pos: #to down
            pacman.setheading(270)
            for  t in range(rpt):
                if t%2 ==0:
                    pacman.shape(images[7])
                else:
                    pacman.shape(images[8])
                    
                pacman.forward(delta)
                
            pacman_position[1]-=1
            
        count+=1      
    pacman.shape(images[9])
    return count


def main():
    tile=tile_position('tile.txt')
    draw_board(tile,50,11)
    count=gem_find_randomwalk(tile,50,11)
    print('이동횟수 %d' %count)
    turtle.done()
    
    
main()