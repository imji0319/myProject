'''
Created on 2017. 9. 29.

@author: jihye
'''
# 동전던지기 H, T의 횟수와 비율 

# -*- coding :utf-8 -*-

import random

def toss_coin(n):
    num_heads = 0
    num_tails = 0
    
    for k in range(n):
        i = random.randint(1,2)
        if i == 1:
            num_heads+=1
        else:
            num_tails+=1
            
    return num_heads, num_tails

def main():
    N=1000000 
    heads, tails = toss_coin(N)
    
    print('동전 던진 횟수 : %d' %N)
    print('앞면의 나온 횟수 : %d, 비율 : %.5f ' %(heads, heads/N))
    print('뒷면이 나온 횟수 : %d, 비율 : %.5f' %(tails, tails/N))
    
main()