'''
Created on 2017. 10. 11.

@author: jihye
'''

# -*- coding : utf-8 -*-

def gen_fibonacci(n):
    past=0
    current=1
    fibo_list=[past,current]
    
    k=0
    
    while k<n-2:
        next = past+current
        fibo_list.append(next)
        past = current
        current= next
        
        k+=1
    return fibo_list


import turtle
import draw_rectangle

def fibo_rect(n):

    fibo_list=gen_fibonacci(n)
    y=0
    
    for i in range(len(fibo_list)):
        x=-fibo_list[i]/2
        
        if i%2==0:
            draw_rectangle.draw_rectangle(x,y,fibo_list[i],30,'blue','blue')
        else:
            draw_rectangle.draw_rectangle(x,y,fibo_list[i],30,'red','red')
            
        
        y-=30
        
        
def main():
    w= 500
    h= 1000
    
    wn=turtle.Screen()
    wn.screensize(w,h)
    
    fibo_rect(15)
    print(gen_fibonacci(15))
    turtle.done()
    
main()        