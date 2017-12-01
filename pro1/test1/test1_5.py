'''
Created on 2017. 9. 18.

@author: jihye
'''
'''프로그래밍 과제1 - 1.키보드를 통해 입력받은 단어에 대해 다음과 같은 규칙에 의해 
복수형을 만들어 출력하는 프로그램을 작성하시오. '''

word=input('문자를 입력하시오 : ')

if word[-1]=='y':
    plural=word[:-1]+'ies'
elif word[-2:]=='ro' and 'to' and 'no':
    plural=word+'es'
elif word[-1]=='s' and 'h' and 'x':
    plural=word+'es'
elif word[-2:]=='fe':
    plural=word[:-2]+'ves'
else:
    plural=word+'s'

print('문자열 (명사 단수) : %s , "%s" 의 복수형 : %s' %(word, word, plural))
