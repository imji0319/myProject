import re
import urllib.request
import urllib.parse


def bind_url():
    defaultURL='https://openapi.naver.com/v1/search/image.xml?'
    sort='sort=sim'
    start='&start=1'
    display='&display=5'
    query='&query=' + urllib.parse.quote_plus(str(input("검색어를 입력하세요")))
    fullURL=defaultURL+sort+start+display+query
    return fullURL

def fetch_contents_from_url():
    url=bind_url()
    headers={
    'Host':'openapi.naver.com',
    'User-Agent':'curl/7.43.0',
    'Accept':'*/*',
    'Content-Type':'application/xml',
    'X-Naver-Client-Id':'FJEDI42sGXO5KGNQ_yXg',
    'X-Naver-Client-Secret':'WkEXhqWrBL'
    }
    req=urllib.request.Request(url,headers=headers)
    f=urllib.request.urlopen(req)
    resultXML=f.read()
    return resultXML

def extract_text_in_tags(tags,tagname="title"):
    txt=[]
    reg="[^<"+tagname+">][^<]+"
    print(reg)
    for tag in tags:
        txt.append(re.search(reg,tag).group())
    print(txt)
    return txt

def get_contents_from_html():
    html=fetch_contents_from_url()
    #print(html)
    """
    bs4 사용하지 않고 파싱하는 방법
    
    정규식을 사용해서 parsing 할 수있음
    """

    title_tags=re.findall("<title>[^<]+</title>",html.decode("utf-8"))
    link_tags=re.findall("<link>[^<]+</link>",html.decode("utf-8"))
    #print(link_tags)

    titles=extract_text_in_tags(title_tags,tagname="title")
    links=extract_text_in_tags(link_tags,tagname="link")
    #이미지가 있는 링크를 가져와서 html로 보이도록 하는 것
    
    

    f=open("C:\\temp\\image.html","w")
    f.write("<html><head><title>네이버이미지웹크롤링</title></head><body>")

    for i in range(1,len(titles)):
        f.write("<p>"+titles[i]+"</p>")
        f.write("<img src="+links[i]+"/>")
    f.write("</body></html>")
    f.close()

get_contents_from_html()
    
    
