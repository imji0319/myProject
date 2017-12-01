'''
Created on 2017. 10. 18.

@author: jihye
'''

'''1. 키보드로부터 입력받은 임의의 개수의 정수 자료를 
리스트로 저장하여 반환하는 함수 get_data()를 정 의하시오. (단, 자료는 ‘,’를 사용하여 분리한다.)'''

def get_data():
    
    word=input('임의의 개수 정수를 "," 로 분리하여 입력하시오 : ' )
    
    integer_list=word.split(',')
    
    integer_list=[eval(x) for x in integer_list] # 한번에 바꾸는 연습 

    # integer_list=list(map(eval,integer_list))
    return integer_list
    
'''2. 정수 리스트를 입력받아 평균을 구하는 함수'''
def average(data):
    sum_int=sum(data)
    mean_int=sum_int/len(data)
    
    return mean_int

'''3. 정수 리스트와 평균값을 입력받아 평균값 이상의 정수 값을 가지는 리스트를 구해 반환'''
def above_average(data,mean):
    up_mean=[x for x in data if x>=mean]
    
 
            
    return up_mean


'''4. 위에서 정의된 함수들을 사용하여, 
10개의 점수 데이터를 입력받고, 
점수를 증가순으로 배열하여 출력 하고, 
평균과 평균이상인 개수를 출력하는 main() 함수'''


def main():
    word=get_data()
    mean=average(word)
    up_mean=above_average(word,mean)
    
    #오름차
    word.sort() 
    
    print(
    '''
    입력점수 (증가순) ---> %s
    평균 : %3.2f
    평균이상인 점수의 수 :%d
    
    ''' 
    %(word, mean, len(up_mean)))

main()   

    
    