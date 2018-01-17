'''
Created on 2018. 1. 3.

@author: jihye
'''
###re.search + re.match    


import re

r=re.compile("[pP]")
print(r.search("pizza")) #search는 어디서 처음 나타는지 알려줌/부분 문자
print(r.search("apple"))

print(r.match("apple"))
print(r.match("apPle"))

print(r.match("pP"))
print(r.match("pizza")) #match 첫문자를 찾는 것 /문자열 시작부

print(re.search("\d+","1034"))
print(re.search("\d+","1034").group())
print(re.search("\d+"," asfl123").group())

m=re.match("[0-9]+","1034")
print(m.group())

m=re.match("[0-9]+","1034    ")
print(m.group())

'''
m=re.match(r'[\t]*[0-9]+',"    1034    ")
print(m.group()) 값 없어print 불
'''
m=re.match(r'[\s]*(\d+)',"    1231    ")
print(m.group())
print(m.group(0)) #group()와 동
print(m.group(1)) #괄호의 갯수보다 +1 개 group 존재 하고 n 는 괄호의 갯수만큼 

#.
r=re.compile("a.c")
print(r.search("abc"))
print(r.search("afc"))
print(r.search("ac"))

#?
r=re.compile("ck?w")
print(r.search("cw"))
print(r.search("ckw"))
print(r.search("ckkw"))

#*
r=re.compile("ck*w")
print(r.search("cw"))
print(r.search("ckw"))
print(r.search("ckkw"))
print(r.search("kw"))

#+
r=re.compile("ck+w")
print(r.search("cw"))
print(r.search("ckw"))
print(r.search("ckkw"))
print(r.search("ckbw"))

#^
r=re.compile("^c")
print(r.search("cw"))
print(r.search("kw"))
#[^] 해당패턴 제
print(re.search("[^ab]","apple"))
print(re.search("[^ab]","bread"))
print(re.search("[^ab]","orange"))

#$
r=re.compile("c$")
print(r.search("cw"))
print(r.search("kwc"))

#[]
print(re.search("[가-사]","강원도에서" )) 
print(re.search("[가-사]","원도에서" ))
#한글은받침까지포함에서 다 만들어

print(re.search("\d+","햄버거가 무려 7000원 이나 하다니 "))


p=re.compile("python")
m=p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())



