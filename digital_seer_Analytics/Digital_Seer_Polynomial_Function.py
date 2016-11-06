# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:00:17 2017

@author: ralall
"""

import requests
import os
import json
import numpy as np
def polynomial(data):
    day=str(data["periodEnd"])
    proxy = 'http://proxy-src.research.ge.com:8080'
    os.environ['RSYNC_PROXY'] = "proxy-src.research.ge.com:8080"
    os.environ['http_proxy'] = proxy
    os.environ['HTTP_PROXY'] = proxy
    os.environ['https_proxy'] = proxy
    os.environ['HTTPS_PROXY'] = proxy
    os.environ['no_proxy'] = ".ge.com"
    response = requests.get("https://dev-digitalseer-ms.run.aws-usw02-pr.ice.predix.io/fetchRediationDataTable?periodEnd="+day)
    d=response.json()
    size=len(d["forecasts"])
#    print size
    ghi=[]
    time=[]
    result=[]
    time_range=[]
   
    min_count=0
    start_range=data["start"]
    end_range=data["stop"]
    for i in range(0,size,1):  
        
            ghi.append(d["forecasts"][i]["ghi"])
            time.append(min_count)
            min_count+=30
    print time 
    print("*******************************************************")
    print ghi
    #fit the data with a 20th degree polynomial
    z7=np.polyfit(time,ghi,17)
#    print z7
    p7 = np.poly1d(z7) 
#    print p7
    
    for a in xrange(start_range,end_range+1):
        
            time_range.append(a)
            predict7=(p7(a))
            result.append(predict7)
        
        
#    print result
##        print(zip(time_range,result))
#    for b in result:
#        if(b<0):
#            newResult.append(0)
#        elif(b>0):
#            newResult.append(b)

#   
    final=json.dumps({"time_range":time,"predicted_value":result})
    return final


    
    
    