'''
Created on 2017. 9. 17.

@author: jihye
'''
#프로그래밍 연습문제 2

#-*- coding : utf-8 -*-

from random import randint

user_num1=int(input('첫번째 두 자리 정수를 입력하시오 '))
user_num2=int(input('두번째 두 자리 정수를 입력하시오 '))
user_num3=int(input('세번째 두 자리 정수를 입력하시오 '))

user_num=[user_num1, user_num2, user_num3]

n1=randint(10,99)
n2=randint(10,99)
n3=randint(10,99)

num=[n1,n2,n3]

correct=0
for i in user_num:
    for j in num:
        if i==j:
            correct+1
if correct==3:
    print('1등')
elif correct==2:
    print('2등')
elif correct==1:
    print('3등')
else:
    print('꼴등')
    