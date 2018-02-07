'''
Created on 2018. 2. 7.

@author: jihye
'''

answer=0

for i in range(1000):
    if i %3 == 0 or i%5 ==0:
        answer+=i
        
print(answer)