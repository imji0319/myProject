'''
Created on 2018. 1. 4.

@author: jihye
'''
def day_input():
    day=input("년,월,일 을 입력하시오: ")
    return day

def year_sum(day):
#지난 연도 합
    yearsum=0
    year=int(day[:4])
    for i in range(1,year):
        if i%4==0:
            if i%400==0:
                yearsum+=366
            elif i%100==0:
                yearsum+=365
            else:
                yearsum+=366
        else:
            yearsum+=365
    
    return yearsum
         
def month_sum(day):
    monthsum=0
    month=int(day[4:6])
    year=int(day[:4])
    #지난달까지의 총 일수

    if year%4==0 and year%400==0 and year%100 != 0:
        for i in range(1,month):
            if i==2:
                monthsum+=29
            elif i in (4,6,9,11):
                monthsum+=30
            elif  i in (1,3,5,7,12):
                monthsum+=31
    else:
        for i in range(1,month):
            if i==2:
                monthsum+=28
            elif i in (4,6,9,11):
                monthsum+=30
            elif i in (1,3,5,7,12):
                monthsum+=31
    return monthsum

def dday(day):
    #요일구하기 
    dday=int(day[6:])
    return dday

def date_mode(daysum):  
     
    week=""
    if daysum%7==0:
        week="일"
    elif daysum%7==1:
        week="월"
    elif daysum%7==2:
        week="화"
    elif daysum%7==3:
        week="수"
    elif daysum%7==4:
        week="목"
    elif daysum%7==5:
        week="금"
    elif daysum%7==6:
        week="토"
    return week

def main():
    day=day_input()
    year=year_sum(day)
    month=month_sum(day)
    date=dday(day)
    day_sum=year+month+date
    week=date_mode(day_sum)
    print("%s의 요일은 %s요일 입니다." %(day,week))
    
    
    
main()  
        
        