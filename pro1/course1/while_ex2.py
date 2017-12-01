'''
Created on 2017. 9. 29.

@author: jihye
'''

#피보나치 수열 

def genFibonacci(n):
    past=0
    current=1
    print(past)
    print(current)
    
    k=0
    while k<n-2:
        next = past+current
        print (next)
        
        past = current
        current= next
        k+=1
        
def genLargestFiboNum(n):
    past=0
    current=1
    next=past+current
    
    while next<n:
        past=current
        current=next
        next=past+current
    return current, next

def main():
    large=genLargestFiboNum(100)
    print(large)
    
main()