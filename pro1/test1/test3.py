
"""
어떤 수 A 가 있다고 하자 A에 다른 B를 곱하면 모든 자리의 수가 1인 숫자들이 있다. 
이번 문제는 A의 배수 중에서 모든 자리의 수가 1인 숫자들 중에서 가장 작은 수 C를 찾는 것이다. 

어떤 수 A를 입력 받아 C가 1이 몇 개 인지 출력하는 프로그램을 작성하시오. 

"""

def howmany(a):
    
    import re 
    
    b=1 
    while True:
        c = a*b
        l=len(str(c))
        
        m=re.match('^[1]*$',str(c))
        if bool(m) :
            return c 
            break
        else:
            b+=1
            
            
            
def ones(a):
    num = howmany(a)
    return len(str(num))
    
print(ones(3))
print(ones(21))
        
            
        