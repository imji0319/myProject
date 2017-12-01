'''
Created on 2017. 9. 17.

@author: jihye
'''

def myMax(num1,num2):
    if num1>num2:
        result=num1
    else :
        result=num2
    return result

def main():
    x=5
    y=2
    k=myMax(x,y)
    print('The maxinum between %d and %d is %d' %(x,y,k))
    
main()
