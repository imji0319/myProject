'''
Created on 2018. 1. 8.

@author: jihye
'''

def map_scale(): 
    n=int(input("지도의 크기 입력하시오 : ")) 
    while True:
        if 1<=n<=16:
            break
        else:
            n=int(input("지도의 크기 입력하시오 : "))
                  
    return n

def arr(n):
    array=[]
    
    for i in range(n):
        num=int(input("정수를 입력하시오 : "))
        
        while True:
            if  0 <= num <= (pow(2,n)-1) :
                break
            else:
                num=int(input("이진수의 길이가 n 이하의 정수를 입력하시오 : "))
            
        array.append(num)
            
    return array

def or_bin(n,arr1,arr2):
    array=[]
    for i in range(n):
        array.append(arr1[i]|arr2[i])
    
    return array

def print_bin(array):
    
    result=""
    result_arr=[]
    pr_arr=[bin(i)[2:] for i in array]

    for i in pr_arr:
        for a in range(len(i)):
            if i[a] =="1":
                result = result+"#"
            else :
                result = result+" "
        
        result_arr.append(result)
        result=""
        
    return result_arr

    
def main():
    n=map_scale()
    
    arr1=arr(n)
    arr2=arr(n)
    
    or_arr_bin=or_bin(n,arr1,arr2)
    
    result=print_bin(or_arr_bin)
    
    print("지도의 한변 크기 : %d" %n )
    print(arr1)
    print(arr2)
    print(result)
    
main()
    

