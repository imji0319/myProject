'''
Created on 2017. 11. 19.

@author: jihye
'''
import numpy as np

#주어진 임의의 자연수 N보다 작은 소수를 모두 구하는 함
def find_prime(n):
    is_prime=np.ones(n)
    is_prime[:2]=0

    max_num=int(np.sqrt(n))
    for m in range(2, max_num+1):
        is_prime[2*m::m]=0
        
    p_num_list=[i for i in range(n) if is_prime[i]==1]
    
    return np.array(p_num_list)

def main():
    N=20
    prime_number=find_prime(N)
    print(prime_number)
    
main()