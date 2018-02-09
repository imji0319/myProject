'''
Created on 2018. 2. 9.

@author: jihye
'''

def even_fibo(num):
    
    past=1
    current=2
    
    fibo=[1,2]
    
    next=0
    
    while next <= num:
        next=past+current
        fibo.append(next)
        past=current
        current=next
        
    answer=0
    for i in fibo:
        if i % 2 == 0:
            answer+=i
            
    return answer

print(even_fibo(4000000))