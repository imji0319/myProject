
'''
Created on 2017. 9. 29.

@author: jihye
'''

#uniform 분포
#-*- coding : utf-8 -*-

import random 

def uniform_simulation(n,a,b,L,R):
    count=0
    
    for r in range(n):
        random_num=random.uniform(a,b)
        if L<=random_num<=R:
            count+=1
        
    return count

def main():
    N=10000
    a,b=0,1000
    L,R=100,500
    
    num_inbound=uniform_simulation(N,a,b,L,R)
    p=num_inbound/N
    fraction=(R-L)/(b-a)
    
    print ('전체 구간 [%d, %d]에서 구간[%d,%d]의 수가 뽑힌 비율 : %.5f' %(a,b, L,R,p))
    print ('전체 구간 [%d, %d]에서 구간[%d,%d]의 수가 뽑힌 비율 : %.5f' %(a,b,L,R, fraction))
   
main() 
    
    
    