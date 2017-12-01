'''
Created on 2017. 10. 18.

@author: jihye
'''

#프로그래밍 과제 05 _ 20140543 임지혜
import math 
num='1234567890'
up_word='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low_word='abcdefghijklmnopqrstuvwxyz'
word=up_word + low_word
special_word='!#$%&():;<=>?@[\\]^_~'

# 1. 가점 기준과 감점 기준 점수를 산정하는 함수
##가산 기준 
def A1(password):
    
    A1=min(3*len(password),45)
    return A1

def A2(password):
    
    up_count=0 ; low_count=0
       
    for i in password: # 영문 숫자 count 

        up_count+=up_word.count(i)
        low_count+=low_word.count(i)
            
    eng_count=up_count+low_count

    A2 = math.floor(40*(1-low_count/eng_count)*(1-up_count/eng_count))
    
    return A2
                       
def A3(password):
    num_count=0
    for i in password:
        num_count+=num.count(i)
    
    A3=4*num_count
    return A3
        
    
def A4(password):
    special_count=0
    for i in password:
        special_count+=special_word.count(i)
            
    A4=6*special_count
    return A4

def A5(password):
    word=password[1:len(password)-1]
    count=0
    for i in word:
        count+=special_word.count(i)
        count+=num.count(i)
    A5=3*count
    return A5

def A6(password):  
    num_count=0 ; sp_count=0 ; word_count=0
    
    for i in password:
        num_count+=num.count(i)
        sp_count+=special_word.count(i)
        word_count+=word.count(i)
        
    if num_count > 0 and sp_count >0 and  word_count>0: 
        A6=10
    else:
        A6=0   
    return A6
    
##감점 기준 
def D1(password):
    
    count=0
    for i in password:
        count+=word.count(i)
        
    if count == len(password):
        D1=len(password)
    else:
        D1=0
            
    return D1
    
    '''
    숫자나 특수문자가 하나라도 나타나면 점수가 0기 되기 때문에 끝까지 읽는 것보다 나타나는 순간 종료하는 것이 더 나
    flag=True
    for ch in password:
        if ch in num or ch in special_word:
            flag=False
            break # 반복을 종료할 때 
    if flag:
        score=len(password)
    else:
        score=0
    return score
    
    

    for ch in password:
        if ch in num or ch in special_word:
            return 0
    
    return len(password)
    '''

def D2(password):
    count=0
    for i in password:
        count+=num.count(i)
        
    if count == len(password):
        D2=len(password)
    else:
        D2=0
            
    return D2
    
    
def D3(password):
    count=0
    for i in password:
        i_count=password.count(i)
        if i_count==1:
            count+=1
                                
    D3=3*(len(password)-count)
    
    return D3

def D4(password):
    length=len(password)        
    count=0
    
    for i in range(1,length):
        if password[i-1] in up_word and password[i] in up_word :
            count+=1
        if password[i-1] in low_word and password[i] in low_word :
            count+=1
        if password[i-1] in num and password[i] in num :
            count+=1
        if password[i-1] in special_word and password[i] in special_word :
            count+=1
       
       
    D4=2*count
    return D4

    
def D5(password):
    count=0

    for i in range(3,len(password)):
        if password[i-3:i] in num:
            count+=1
    
    D5=3*count
    return D5    

###유형1 
def D6(password):
    str_list='qwertyuiopdml'
    count=0
    
    for i in range(3,len(password)):
        if password[i-3:i] in str_list:
            count+=1
    
    D6=3*count
    return D6  

    
def D7(password):
    str_list='asdfghjkl'
    count=0
    
    for i in range(3,len(password)):
        if password[i-3:i] in str_list:
            count+=1
    
    D7=3*count
    return D7 
 
def D8(password):
    str_list='zxcvbnm'
    count=0
    
    for i in range(3,len(password)):
        if password[i-3:i] in str_list:
            count+=1
    
    D8=3*count
    return D8
    
    
# 2. 키보드를 통해 비밀번호를 입력받은 후, 허용된 문자로 구성된 비밀번호를 반환하는 함수 get_password()

def get_password():
    
    password=input('비밀번호를 입력해주세요 : ')
    
    un_passed=[x for x in password if (x not in word) and (x not in num) and (x not in special_word)]
            
    while len(un_passed) > 0:
        
        print('허용되지 않은 문자 를 사용하셨습니다.  %s 를 다시 입력해주세요.'  %un_passed)
        password=input('새로운 비밀번호를 입력해주세요 : ')
        
        un_passed=[x for x in password if x not in word and x not in num and x not in special_word]
        
           
    return password

    '''
    is_valid=False:
    while not is_valid:
        password=input('비밀번호 :')
        invalid=[]
        for ch in password:
            if not (ch in num or ch in word or ch in special_word:
                invaild.append(ch)
        if len(invalid)>0:
            print('허용하지 않은 문자를 사용했습니다.' , invaild, '다시 입력하세요')
        else:
            is_valid = True
    return password
    
    '''
        
# 3. 입력된 비밀번호의 강도를 계산하고, 비밀 번호의 강도가 60점 미만인 경우 다시 적정한 강도를 가지는 비밀 번호를 입력받는 과정을 반복하는 프로그램

def cal_password(password):
    a_sum=A1(password)+A2(password)+A3(password)+A4(password)+A5(password)+A6(password)
    m_sum=D1(password)+D2(password)+D3(password)+D4(password)+D5(password)+D6(password)+D7(password)+D8(password)
    strength=a_sum-m_sum
    
    return strength
    

def main():
    
    password=get_password()
    strength=cal_password(password)
    
    print( '비밀번호 : %s' %password)
    
    while strength < 60 :

        print('비밀번호 강도 수준 : %d' %strength)
        print('---> 비밀번호 강도 수준이 낮습니다 . 비밀번호를 다시 입력하세요. ')
        password=get_password()
        strength=cal_password(password)
    
    print(
'''비밀번호 강도 수준 : %d 
비밀번호 강도 수준이 적합니다. ''' 
    %strength)
        
    
    
    
main()
    
    
    
    
    