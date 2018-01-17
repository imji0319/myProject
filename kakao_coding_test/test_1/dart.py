'''
Created on 2018. 1. 10.

@author: jihye
'''

import re
while True:
    string=input("""1~10사이의 정수와 
문자 S,D,T 중 하나와 *,# 으로 구성된 문자열을 입력하시오 """)

#문자열 분리 
    pat=re.compile("\d{1,2}[S,D,T][*,#]?")

#전체 문자열에서 3개로 분리 
    result=re.findall(pat,string)

    num=re.compile('\d{1,2}')
    ex_num=re.compile('[S,D,T]')


    sumlist=[]
    for i in range(3):

        result_re=re.findall(num,result[i])
        result_ex=re.findall(ex_num,result[i])

        r=int(result_re[0])
        s=str(result_ex[0])

        if s == 'S':
            r=pow(r,1)
            
        elif s == 'D':
            r=pow(r,2)
            
        elif s == 'T':
            r=pow(r,3)
 
        sp=re.findall('\W',result[i])
    
        if sp==["*"]:
            r*=2
        
        elif sp==['#']:
            r*=(-1)
        
        sumlist.append(r)
       
    sp=[]
    for i in range(3):
        sp.append(re.findall('\W',result[i]))

    for i in range(2):
    
        if sp[i+1]==['*']:
            sumlist[i]*=2
        elif sp[i]==['*'] and sp[i+1]==['*']:
            sumlist[i]*=2

        elif sp[i]==['#'] and sp[i+1]==['*']:
            sumlist[i]*=2
    

    print('합 : ',sum(sumlist))
  
        
        
    
            

        