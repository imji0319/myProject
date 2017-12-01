'''
Created on 2017. 11. 8.

@author: jihye
'''
# array 처리 연습
import numpy as np
import matplotlib.pyplot as plt

#1. 
def main():
    fev_obs=np.loadtxt('data/fev.txt',comments='#',delimiter=None, skiprows=0) #comments : default # , skiprows=0
    
    print(fev_obs)
    fev_obs_T=fev_obs.T
    age, fev, height, gender, smoking = fev_obs.T
    smoke=fev[smoking==0]
    print(smoke,len(smoke))
    '''
    print(fev_obs)
    
    #2.    
    print(len(fev_obs))
    #3.
    female_flag=fev_obs[fev_obs_T[3]==0]
 
    male_flag=fev_obs[fev_obs_T[3]==1]
    
    
    print('female :' , len(female_flag), 'male :' , len(male_flag))
    print('Total : ' ,len(female_flag)+len(male_flag))
    #4.
    smoker=fev_obs[fev_obs_T[4]==1]
    nonsmoker=fev_obs[fev_obs_T[4]==0]
    print('smoker : ', len(smoker) , 'nonsmoker : ' , len(nonsmoker))
    print('Total : ' ,len(smoker)+len(nonsmoker))
    
    #5.
    above10=fev_obs[fev_obs_T[0]>=10]
    below10=fev_obs[fev_obs_T[0]<10]
    print(above10)
    print(below10)
    print('10세 이상 :' ,len(above10), ', 10세 미만 : ',len(below10)) '''
    #6

    ''' 
    x=np.arange(1,len(female_flag)+1)
    y=np.arange(1,len(male_flag)+1)
    
    
    plt.plot(x,female_flag[:,1],'ro')
    plt.plot(y,male_flag[:,1],'bo')
    plt.show() 
    '''
main()
