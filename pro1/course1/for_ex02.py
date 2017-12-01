'''
Created on 2017. 9. 29.

@author: jihye
'''

# 동전던지기 
# -*- coding : utf-8 -*-

from random import randint as randi #함수이름을 새로지정할때 'as'

def GenCoinToss(n):
    s=''
    for k in range(n):
        i = randi(0,1)
        if i==0 :
            s= s+'H'
        else:
            s+='T'
            
    return s

#샌드위치열 확인함

def isSandwich(t):
    n =len(t)
    Meat = t[1:n-1]
    Type1= t[0]=='H' and t[n-1]=='H'
    Type1= Type1 and Meat.count('T') == n-2
    
    Type2 = t[0]=='T' and t[n-1]=='T'
    Type2 = Type2 and Meat.count('H') == n-2
    
    return Type1 or Type2 


def main():
    s = GenCoinToss(100)
    
    k=0
    n=len(s)
    t=s[0:5]
    while k+5 <= n and (not isSandwich(t)):
        k+=1
        t=s[k:k+5]
        
    if k+5==n+1:
        print('there is no sandwich')
        
    else:
        print('there is a length-5 sandwich')
        print(t)
        
    
    
main()