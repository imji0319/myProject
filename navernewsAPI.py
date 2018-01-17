import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


defaultURL='https://openapi.naver.com/v1/search/news.xml?'
sort='sort=sim'
start='&start=1'
display='&display=2'
query='&query=' + urllib.parse.quote_plus(str(input("검색어를 입력하세요")))

fullURL=defaultURL+sort+start+display+query
filename=input("저장할 파일 경로와 파일명을 입력하시오")
file=open(filename,"w",encoding="utf-8")

headers={
    'Host':'openapi.naver.com',
    'User-Agent':'curl/7.43.0',
    'Accept':'*/*',
    'Content-Type':'application/xml',
    'X-Naver-Client-Id':'FJEDI42sGXO5KGNQ_yXg',
    'X-Naver-Client-Secret':'WkEXhqWrBL'
    }


req=urllib.request.Request(fullURL,headers=headers)
f=urllib.request.urlopen(req)
resultXML=f.read()
print(resultXML)#원문확인 


xmlsoup= BeautifulSoup(resultXML,'html.parser')
items=xmlsoup.find_all('item')


for i in items:
    file.write('______________________________________\n')
    file.write('뉴스제목 : ' + i.title.get_text(strip=True)+'\n')
    file.write('요약내용 : ' + i.description.get_text(strip=True)+'\n')
    file.write('원문링크 : ' + i.link.get_text(strip=True)+'\n')
    file.write('\n')

file.close()


