# -*- coding:utf-8 -*- 

'''
Created on 2017. 9. 20.

@author: jihye
'''
import turtle

mypen=turtle.Turtle()
mypen.pencolor('black')
mypen.fillcolor('blue')
mypen.pensize(5)
    
mypen.penup()
mypen.goto(90,90)
mypen.pendown()
    
mypen.circle(40)
mypen.hideturtle()

turtle.done()