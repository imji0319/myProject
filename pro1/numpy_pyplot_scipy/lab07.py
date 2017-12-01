'''
Created on 2017. 11. 15.

@author: jihye
'''
import numpy as np
import matplotlib.pyplot as plt
import codecs


def get_data(filename):
    
    fcp=codecs.open(filename,encoding='cp1252')
    pop_data=np.loadtxt(fcp)
    pop_data[:,2]=np.round(pop_data[:,2]*2.54,decimals=1)
    
    return pop_data

def basic_stat(pop_data):
    #logical_and : True False의 1차원 array 
    #array에서 여러 원소에 조건을 정할때 logical_or/ logical_and 활용
    #단 두개까지 비교 가능
    
    '''
    group1=np.logical_and(pop_data[:,1]<10,pop_data[:,3]==0)
    group1=np.logical_and(group1,pop_data[:,4]==0)
    
    group2=np.logical_and(pop_data[:,1]<10,pop_data[:,3]==0)
    group2=np.logical_and(group2,pop_data[:,4]==1)
    
    
    group3=np.logical_and(pop_data[:,1]<10,pop_data[:,3]==1)
    group3=np.logical_and(group3,pop_data[:,4]==0)
    
    group4=np.logical_and(pop_data[:,1]<10,pop_data[:,3]==1)
    group4=np.logical_and(group4,pop_data[:,4]==1)
    
    group5=np.logical_and(pop_data[:,1]>=10,pop_data[:,3]==0)
    group5=np.logical_and(group5,pop_data[:,4]==0)
    
    group6=np.logical_and(pop_data[:,1]>=10,pop_data[:,3]==0)
    group6=np.logical_and(group6,pop_data[:,4]==1)
    
    group7=np.logical_and(pop_data[:,1]>=10,pop_data[:,3]==1)
    group7=np.logical_and(group7,pop_data[:,4]==0)
    
    group8=np.logical_and(pop_data[:,1]>=10,pop_data[:,3]==1)
    group8=np.logical_and(group8,pop_data[:,4]==1)
    
    
    
    g1=pop_data[group1]
    g2=pop_data[group2]
    g3=pop_data[group3]
    g4=pop_data[group4]
    g5=pop_data[group5]
    g6=pop_data[group6]
    g7=pop_data[group7]
    g8=pop_data[group8] '''
    
    condition=[(0,0),(0,1),(1,0),(1,1)]
    
    groups=[]
    for x,y in condition:
        flag=np.logical_and(pop_data[:,1]<10,pop_data[:,3]==x)
        flag=np.logical_and(flag,pop_data[:,4]==y)
        
        groups.append(pop_data[flag])
    
    for x,y in condition:
        flag=np.logical_and(pop_data[:,1]>=10,pop_data[:,3]==x)
        flag=np.logical_and(flag,pop_data[:,4]==y)
        groups.append(pop_data[flag])
        
    for i in np.arange(8):
        a=groups[i]
        if len(a)>0:
            print('group',str(i+1),'호기량 통계량')
            print('평균',a[:,1].mean())    
            print('평균',np.mean(a[:,1])) 
            print('중앙값',np.median(a[:,1]))
            print('최소값',np.min(a[:,1]))   
            print('최대값',np.max(a[:,1]))
            print('표준편차',np.std(a[:,1]))
            
        
            
        if len(a)>0:
            print('group',str(i+1),'키 통계량')
            print('평균',a[:,2].mean())    
            print('평균',np.mean(a[:,2])) 
            print('중앙값',np.median(a[:,2]))
            print('최소값',np.min(a[:,2]))   
            print('최대값',np.max(a[:,2]))
            print('표준편차',np.std(a[:,2]))
        
        print("")  
            
    return groups

def histoplot(position, x,lgnd, bins_data):
    plt.subplot(2,1,position)
    plt.tight_layout()
    
    plt.hist(x,bins=bins_data,alpha=0.5, label=lgnd)
    plt.legend()
    plt.grid()
    plt.xlabel('FEV')
    plt.ylabel('frequency')   
 
 
 
def main():
    fev_data=get_data('data/fev.txt')
    age,fev,height,gender,smoker= fev_data.T
    
    bins_data=np.arange(fev.min(),fev.max(),0.2)
    male_fev,female_fev=fev[gender==1],fev[gender==0]
    nonsmoker_fev,smoker_fev=fev[smoker==0],fev[smoker==1]
    histoplot(1,female_fev,'Famale',bins_data)
    histoplot(1,male_fev,'Male',bins_data)    

    histoplot(2,nonsmoker_fev,'Nonsmoker',bins_data)
    histoplot(2,smoker_fev,'Smoker',bins_data)
    
    plt.show()

    
main()
    