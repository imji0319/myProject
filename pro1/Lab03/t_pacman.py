'''
Created on 2017. 9. 29.

@author: jihye
'''
import turtle
from random import randint

def draw_rectangle(x, y, w, h, color='black', fill_color='white', size=1):
    pen = turtle.Turtle()
    pen.pencolor(color)
    pen.fillcolor(fill_color)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.forward(w)
    pen.left(90)
    pen.forward(h)
    pen.left(90)
    pen.forward(w)
    pen.left(90)
    pen.forward(h)
    pen.left(90)
    pen.hideturtle()
    
    
def draw_board(n, size):
    x = -(n//2 * size) - size//2 
    y = -(size//2)
    
    for tile in range(n):
        draw_rectangle(x, y, size, size)
        x += size
def start_randomwalk(n, size):
    pacman=turtle.Turtle()
    
    # shape에 대한 이미지 등록
    image_rightOpen = 'image/right_open.gif' 
    image_rightClose = 'image/right_close.gif' 
    image_leftOpen = 'image/left_open.gif' 
    image_leftClose = 'image/left_close.gif' 
    image_die = 'image/die.gif'
    
    
    screen = turtle.Screen()
    screen.addshape(image_rightOpen)
    screen.addshape(image_rightClose)
    screen.addshape(image_leftOpen)
    screen.addshape(image_leftClose)
    screen.addshape(image_die)
    
    pacman.shape(image_rightOpen)
    pacman.speed(1)
    pacman.penup()
    
    position = 0
    edge = n//2
    
    while -edge<=position<=edge:
        where = randint(0,1)
        rpt = 5
        delta = size/rpt
        
        
        if where==0:        # to rightward
            position += 1
            pacman.setheading(0)
        #pacman.forward(size)

            for n in range(rpt):
                if n%2==0:
                    pacman.shape(image_rightOpen)
                else:
                    pacman.shape(image_rightClose)
                pacman.forward(delta)
        
        else:
            position -=1
            pacman.setheading(180)
            
            for n in range(rpt):
                if n%2==0:
                    pacman.shape(image_leftOpen)
                else:
                    pacman.shape(image_leftClose)
                pacman.forward(delta)
                
    
    pacman.shape(image_die)
    
    
                
                
                
                
def main(): 
    num_tile = 5
    size_tile = 50
    w = (num_tile+3)*size_tile
    h = 3*size_tile
    turtle.setup(w, h)
    draw_board(num_tile, size_tile)
    start_randomwalk(num_tile, size_tile)
    turtle.done()
    
    
main()