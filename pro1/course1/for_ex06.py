'''
Created on 2017. 9. 29.

@author: jihye
'''
#주사 던지기 : 특정 눈의 횟수와 비율 
# -*-coding : utf-8 -*-

import random

def toss_die(n):
    spot_1, spot_2, spot_3,spot_4,spot_5,spot_6 =0,0,0,0,0,0
    for k in range(n):
        i =random.randint(1,6)
        if i ==1 :
            spot_1+=1
        elif i==2:
            spot_2+=1
        elif i==3:
            spot_3+=1
        elif i==4:
            spot_4+=1
        elif i==5:
            spot_5+=1
        else:
            spot_6+=1
            
    return spot_1, spot_2, spot_3,spot_4,spot_5,spot_6

def main():
    N=1000000
    s_1, s_2, s_3, s_4, s_5, s_6= toss_die(N)
    print('주사위 던진 횟수 : %d' %N)
    print('5의 눈이 나온 횟수 : %d, 비율 : %.5f ' %(s_5, s_5/N))
    
main()