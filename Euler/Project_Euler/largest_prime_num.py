'''
Created on 2018. 2. 9.

@author: jihye
'''

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def largest_prime_number(num):
    factor=[]
    for i in range(2,num):
        if num % i == 0:
            factor.append(i)

    answer=[]     
    for i in factor:
        prime=[]
        for j in range(1,i+1):
            if i % j == 0:
                prime.append(j)
            
        if len(prime) == 2:
            answer.append(i)
    
    return  answer[-1]
    
print(largest_prime_number(600851475143))