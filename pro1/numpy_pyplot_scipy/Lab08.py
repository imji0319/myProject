'''
Created on 2017. 11. 22.

@author: jihye
'''


import numpy as np
import matplotlib.pyplot as plt

def fev_box(data):

    plt.boxplot(data)
    
def fev_histogram(data,num):

    plt.hist(data,bins=num,alpha=0.7)
    
    
    


def main():
    n=5
    plt.figure(figsize=(10,4))
    x=np.linspace(0,np.pi*4,1000)
    y=np.zeros(1000)

    for i in np.arange(1,n*2,2):
        y+=(1/i)*np.sin(i*x)
        plt.plot(x,(1/i)*np.sin(i*x))
    

    plt.plot(x,y,linewidth=2)
    
    ax=plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    

    plt.xlim(0,4*np.pi)
    plt.ylim(-1.1,1.1)
    plt.xticks(np.linspace(0,np.pi*4,5),['',r'$\pi$',r'$2\pi$',r'$3\pi$',r'$4\pi$'])
    plt.yticks(np.linspace(-1.0,1.0,5))
    plt.show()
    
    fev_data=np.loadtxt('data/fev.txt')
    age,fev,height,gender,smoker= fev_data.T
    
    plt.subplot(1,2,1)
    fev_box(fev)
    plt.subplot(1,2,2)
    fev_histogram(fev ,40)
    plt.grid()
    plt.show()
    
    


main()

