'''
Created on 2017. 9. 29.

@author: jihye
'''
# 세개의 주사위 

# -*-coding : utf-8 -*-

import random

def toss_three_die():
    die1_spot=random.randint(1,6)
    die2_spot=random.randint(1,6)
    die3_spot=random.randint(1,6)
    
    if die1_spot==die2_spot and die1_spot==die3_spot and die2_spot==die3_spot:
        return True
    else:
        return False
    
    
def main():
    N=10000
    count=0
    
    for toss in range(N):
        if toss_three_die():
            count+=1
    print('세개의 주사위 던진 횟수 : %d' %N)
    print('세개의 주사위 눈이 서로 같게 나온 횟수 : %d, 비율 : %.5f' %(count,count/N))
    
main()