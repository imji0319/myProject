'''
Created on 2017. 9. 29.

@author: jihye
'''

# 별 그리기
 
# -*-coding : utf-8 -*- 


import turtle

def draw_star(x,y,size=50, pencolor='black'):
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
    w=520 ; h=500
    turtle.setup(w,h)
    start=-250
    size=100
    
    for n in range(5):
        if n%2 == 0 :
            draw_star(start,0,size,'blue')
        else:
            draw_star(start,0,size,'red')
        start+=size
        
    turtle.done()
    
main()

