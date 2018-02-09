'''
Created on 2018. 1. 4.

@author: jihye
'''
#urllib : 웹 상의 문서나 파일 즉 데이터를 가져올 수 있는 라이브러리

import urllib.request #웹 서버에 요청하기 
import urllib.parse #인코딩 
req=urllib.request

d=req.urlopen("http://wikidocs.net/")
status=d.getheaders()
for i in status:
    print(i)

a=urllib.parse.quote_plus("dnjkaㅇ무ㅏㅓㅇ dnka")
b=urllib.parse.quote("dnjkaㅇ무ㅏㅓㅇ dnka")

print(a)
print(b)