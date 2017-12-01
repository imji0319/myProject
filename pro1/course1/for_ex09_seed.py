'''
Created on 2017. 9. 29.

@author: jihye
'''
# seed 함
# -*- coding: utf-8 -*-

import random

def main():
    n=5
    random.seed(0)
    
    for r in range(n):
        num=random.uniform(-1,1)
        print(num)
        
main()

        