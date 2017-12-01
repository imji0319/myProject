'''
Created on 2017. 9. 19.

@author: jihye
'''

from random import randint

num1=randint(0,9)
num2=randint(0,9)
num3=randint(0,9)

user_num1=int(input('first num  : '))
user_num2=int(input('second num  : '))
user_num3=int(input('third num  : '))



if (user_num1 in (num1,num2,num3)) and (user_num2 in (num1,num2,num3)) and (user_num3 in (num1,num2,num3)):
    print('1등')
elif (user_num1 in (num1,num2,num3)) and (user_num2 in (num1,num2,num3) ):
    print('2등')
elif (user_num1 in (num1,num2,num3)) and (user_num3 in (num1,num2,num3)):
    print('2등')
elif (user_num2  in (num1,num2,num3)) and (user_num3 in (num1,num2,num3)):
    print('2등')
elif user_num1 in (num1,num2,num3):
    print('3등')
elif user_num2 in (num1,num2,num3):
    print('3등')
elif user_num3 in (num1,num2,num3):
    print('3등')
else:
    print('incorrect')