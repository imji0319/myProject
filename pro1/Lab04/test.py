'''
Created on 2017. 10. 26.

@author: jihye
'''

num='1234567890'
up_word='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low_word='abcdefghijklmnopqrstuvwxyz'
word=up_word + low_word
special_word='!#$%&():;<=>?@[\\]^_~'

def D1(password):
    
    count=0
    for i in password:
        count+=word.count(i)
        
    if count == len(password):
        D1=len(password)
    else:
        D1=0
            
    return count, D1

def main():
    count,d1=D1('add23asd')
    print(count,d1)
    
main()