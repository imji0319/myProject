'''
Created on 2017. 11. 29.

@author: jihye
'''
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def relation(t,a,b,c):
    return a*np.cos(2*np.pi*t+b)+c
    
def relation_predict(t,a,b,c):
    
    value=a*np.cos(2*np.pi*t+b)+c
    return value

def main():
    temperature=np.loadtxt('data/temperature.txt')
    date,temp=temperature.T
    plt.figure(figsize=(10,6))
    
    plt.plot(date,temp)
    temper=temp[np.abs(temp)<90]
    year=date[np.abs(temp)<=90]

    

    plt.plot(year,temper,ms=1)
    #plt.show()
    
    temper=temper[np.logical_and(date>=2008,date<=2012)]
    date=year[np.logical_and(date>=2008,date<=2012)]

    param,parmas_cov=opt.curve_fit(relation,date,temper)
    print (param)
    
    
    print( ' 평균 기온 : ' , np.mean(temper))
    cold_temp=np.min(temper)
    cold_date=date[temper==cold_temp]
    hot_temp=np.max(temper)
    hot_date=date[temper==hot_temp]
    
    #10/360 -> 앞뒤로 10개 총 20
    cold_season=date[np.logical_and(date<=cold_date+10/360,date>=cold_date-10/360)]
    hot_season=date[np.logical_and(date<=hot_date+10/360, date>=hot_date-10/360)]
    hot_pred=relation_predict(hot_season,param[0],param[1],param[2])
    cold_pred=relation_predict(cold_season,param[0],param[1],param[2])
    hot_mean=np.mean(hot_pred)
    cold_mean=np.mean(cold_pred)
    
    print('추운 시기 예상 평균기온 : ' , cold_mean ,' 더운 시기 예상 평균 기온 ' , hot_mean)
    
    
    plt.show()

main() 