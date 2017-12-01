'''
Created on 2017. 9. 18.

@author: jihye
'''

''' 프로그래밍 과제1 - 2. 번호 맞추기 게임을 위해 1자리 정수 3개를 랜덤하게 생성한다. 
사용자로 부터 3개의 1자리 정수를 입력 받아 
3개 모두 맞추면1등,2개만 맞추면2등,1개만 맞추면 3등이 되는 번호 맞추기 게임을 작성하라. '''

from random import randint

num1=randint(0,9)
num2=randint(0,9)
num3=randint(0,9)

user_num1=int(input('first num  : '))
user_num2=int(input('second num  : '))
user_num3=int(input('third num  : '))

if (user_num1==num1 and num2 and num3) and (user_num2==num1 and num2 and num3) and (user_num3==num1 and num2 and num3):
    print('1등')
elif (user_num1==num1 and num2 and num3) and (user_num2==num1 and num2 and num3):
    print('2등')
elif (user_num1==num1 and num2 and num3) and (user_num3==num1 and num2 and num3):
    print('2등')
elif (user_num2==num1 and num2 and num3) and (user_num3==num1 and num2 and num3):
    print('2등')
elif user_num1==num1 and num2 and num3:
    print('3등')
elif user_num2==num1 and num2 and num3:
    print('3등')
elif user_num3==num1 and num2 and num3:
    print('3등')
else:
    print('incorrect')