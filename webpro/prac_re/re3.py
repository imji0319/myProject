'''
Created on 2018. 1. 3.

@author: jihye
'''
import re

#findall() ->> 리스트 반환 
#finditer ->> 매칭되는 해당문자열 모두와 각 위치값 리턴 

#split : 주어진 문자열을 특정 패턴 기준분 

p=re.compile('[a-z]+')
result=p.findall("life is too short")
print(result)
print(re.findall("\d+","서진수는 1975년 10월 23일 입니다.^^ "))

result=p.finditer("life is too short")
print(result)
for i in result:
    print(i.group())
    print(i.span())

print(re.split('[:]+',"Apple Orange : Grape Cherry"))
print(re.split('[: ]+',"Apple Orange : Grape Cherry"))

print(re.sub('-','**',"123432-2342344"))