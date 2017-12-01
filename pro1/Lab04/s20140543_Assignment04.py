'''
Created on 2017. 10. 12.

@author: jihye
'''


# 프로그래밍 과제_4_20140543 임지혜 

#1 문자열을 받아 리스트로 변환

def str_change():
    
    word=input('짝수 문자열을 입력하시오 : ')
    word_list=[]
    
    while len(word)%2 != 0:
        print('짝수 문자열이 아닙니다.')
        word=input('짝수 문자열을 입력하시오 : ')
        
    for i in word:
        word_list.append(i)
        
    return word_list

#2 리스트 섞기

def perfect_shuffle(origin):
    
    length=len(origin)
    half_1=origin[:length//2]
    half_2=origin[length//2:]
    change_word=[]
    
    for i in range(length//2):
        change_word.append(half_1[i])
        change_word.append(half_2[i])
            
    return origin, change_word

#3 원래 리스트로 복원하는 소요 횟수 

def num_perfect_shuffle(origin,shuffled):
    
    count=0

    while origin != shuffled:
        half_1, half_2 = shuffled[:len(shuffled)//2] , shuffled[len(shuffled)//2:]
        
        
        shuffled=[]
        
        for i in range(len(origin)//2):
            shuffled.append(half_1[i])
            shuffled.append(half_2[i])
            
        count+=1
    
    return shuffled, count



def main():
    origin=str_change()
    origin,shuffled_list = perfect_shuffle(origin) #origin, change_word
    
    
    shuffled, count = num_perfect_shuffle(origin,shuffled_list)
    print (
    '''
    처음 리스트 : %s
    섞인 리스트 : %s
    복원 리스트 : %s
    복원 횟수 : %d
    ''' 
    %(origin, shuffled_list, shuffled, count))

     
    
main()
    
    
    
    
    



