'''
Created on 2017. 10. 11.

@author: jihye
'''
greeting='hello'

for ch in greeting :
    print(ch)
    
for index in range(len(greeting)):
    print(greeting[index])


int_list=[10,20,30,40]

sum_value=0

for value in int_list:
    print(value)
    sum_value+=value
    
print(sum_value)


sum_value=0
for index in range(len(int_list)):
    print(int_list[index])
    sum_value+=int_list[index]
    
print(sum_value)