'''
Created on 2018. 3. 18.

@author: jihye
'''
from boto import config

"""
Code 31. 관광지 별 주요 입장객 정보 
"""

import os
import sys
import urllib.request
import datetime
import time 
import json 
# from config import *
import math 

def get_request_url(url):
    
    req = urllib.request.Request(url)
    
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 :
            print ("[ %s ] Url Request Success" %datetime.datetime.now())
            return response.read().decode('utf-8')
        
    except Exception as e:
        print(e) 
        print(" [%s] Error for URL : %s " %(datetime.datetime.now(),url))
        return None
    

    
#[CODE 1]

def getTourPointVisitor(yyyymm,sido,gungu,nPagenum,nltems):
    
    end_point= "http://openapi.tour.go.kr/openapi/service"
   
    parameters="?_type=json&serviceKey=" + access_key
    parameters +="&YM=" + yyyymm
    parameters +="&SIDO=" + urllib.parse.quote(sido)
    parameters +="&GUNGU=" +urllib.parse.quote(gungu)
    parameters +="&RES_NM=&pageNo=" + str(nPagenum)
    parameters +="&numOfRows=" + str(nltems)
    
    url = end_point + parameters
    retData=get_request_url(url)
    
    if (retData == None):
        return None
    else:
        return json.loads(retData)
    
    
#[CODE 2]

def getTourPointData(item,yyyymm,jsonResult):
    
    addrCd = 0 if 'addrCd' not in item.keys() else item['addrCd']
    gungu = '' if 'gungu' not in item.keys() else item['gungu']
    sido = '' if 'sido' not in item.keys() else item['sido']
    resNm = '' if 'resNm' not in item.keys() else item['resNm']
    rnum = 0 if 'rnum' not in item.keys() else item['rnum']
    ForNum = 0 if 'csForCnt' not in item.keys() else item['csForCnt']
    NatNum = 0 if 'csNatCnt' not in item.keys() else item['csNatCnt']
    
    jsonResult.append({'yyyymm':yyyymm,
                       'addrCd':addrCd,
                       'gungu':gungu,
                       'sido':sido,
                       'resNm':resNm,
                       'rnum':rnum,
                       'ForNum':ForNum,
                       'NatNum':NatNum})
    
    
    return 

def main():
    jsonResult = []
    
    sido="서울특별시"
    gungu=''
    nPagenum=1
    nTotal=0
    nltems=100
    nStartYear=2011
    nEndYear=2018
    
    for year in range(nStartYear,nEndYear):
        for month in range(1,13):
            yyyymm = "{0}{1:0>2}".format(str(year),str(month))
            nPagenum=1
            
            #[CODE 3]
            
            while True:
                jsonData=getTourPointVisitor(yyyymm,sido,gungu,nPagenum,nltems)
                
                if (jsonData['response']['header']['resultMsg'] == 'OK') :
                    nTotal = jsonData['response']['body']['totalCount']
                    
                    if nTotal== 0:
                        break
                    
                    for item in jsonData['response']['body']['items']['item']:
                        getTourPointData(item,yyyymm,jsonResult)
                        
                    nPage = math.ceil(nTotal/100)
                    if (nPagenum == nPage):
                        break
                    
                    nPagenum+=1
                else:
                    break
    with open('%s_관광지입장정보_%d_%d.json' %(sido,nStartYear,nEndYear-1),'w',encoding='utf-8') as outfile:
        
        retJson=json.dumps(jsonResult,
                           indent=4,
                           sort_keys=True,
                           ensure_ascii=False)
        
        outfile.write(retJson)
        
    print("%s_관광지입장정보_%d_%d.json SAVED" %(sido,nStartYear,nEndYear-1))

if __name__ == '__main__':
    main()  
                
                    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

            

