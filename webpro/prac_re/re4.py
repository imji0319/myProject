'''
Created on 2018. 1. 3.

@author: jihye
'''

import re
r=re.compile("^[a-zA-Z]\w+")
while True:
    str1=input("ID입력")
    if r.search(str1)==None:
        print("잘못입력")
        continue
    else:
        idw=str1
        print(idw)
        break