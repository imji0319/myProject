'''
Created on 2017. 10. 23.

@author: jihye

'''


student_data = {'20131312':
{'name': '김은혜', 'department': '정보통계학과' ,
'enrolled': ['객체지향프로그래밍', '정보기술개론', '경영학원론'] },
'20131321':
{'name': '김효빈', 'department': '정보통계학과',
'enrolled': ['수리통계학I','행렬대수학', 'DB개론'] },
'20131312':
{'name': '김은혜', 'department': '정보통계학과' ,
'enrolled': ['객체지향프로그래밍', '정보기술개론', '경영학원론'] }
}

def a(student_data):
    result={}

    for key, value in student_data.items():
        if key not in result:
            result[key]=value
    return result

def main():
    result=a(student_data)
    for id, data in result.items():
        for info, info2 in data.items():
            if info=='enrolled' and '객체지향프로그래밍' in info2:
                print(id)
                    
main()
                
    