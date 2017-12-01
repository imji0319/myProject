'''
Created on 2017. 9. 17.

@author: jihye
'''

#문자 회문(palindrome) 찾기

#-*- coding:utf-8 -*-

user_str=input('글자를 입력하시오 :')

str_len=len(user_str)

for i in range(0,str_len-1):
    if user_str[i]==user_str[str_len-1+i]:
        print('palindrome')
    else :
        print('not a palindrome')
            
            
        
