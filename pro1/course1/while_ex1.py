'''
Created on 2017. 9. 29.

@author: jihye
'''

# 스트릭(streaks) 여부

def isStreak(s,k,n):
    t=s[k:k+n]
    if k+n>len(s):
        return False
    elif t.count('H')<n and t.count('T') <n:
        return False
    elif k>0 and s[k-1]==s[k] : 
        return False
    elif k+n<len(s) and s[k+n-1]==s[k+n]:
        return False
    else:
        return True 

    

def FindStreak(s,n):
    k=0
    
    while k<len(s) and (not isStreak(s,k,n)):
        k+=1
    
    if k<len(s):
        return k 
        
    else:
        return -1 
    
def main():
    s =' HTHHHTTHTHTHTTT'
    istreak = FindStreak(s,2)
    print ('%s 에는 길이 2-Streak 이 있고 그 streak은 %d 번에 있다. ' %(s,istreak) )

main()
    