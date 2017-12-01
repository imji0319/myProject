'''
Created on 2017. 9. 20.

@author: jihye
'''
#주어진 명사(문자열)에 대해 복수형을 구해 반환하는 get_plural() 함수를 정의하시오.

def get_plural(word):
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
    
    return plural
    
def main():
    word=input('문자를 입력하시오 : ')
    plural=get_plural(word)
    
    print(word, plural)
    
main()