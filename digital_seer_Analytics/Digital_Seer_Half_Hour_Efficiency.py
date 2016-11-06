# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:57:58 2017

@author: ralall
"""
import requests
import os
import json
def half_hour_efficiency(date):
    day=str(date["periodEnd"])
    proxy = 'http://proxy-src.research.ge.com:8080'
    os.environ['RSYNC_PROXY'] = "proxy-src.research.ge.com:8080"
    os.environ['http_proxy'] = proxy
    os.environ['HTTP_PROXY'] = proxy
    os.environ['https_proxy'] = proxy
    os.environ['HTTPS_PROXY'] = proxy
    os.environ['no_proxy'] = ".ge.com"
    response1 = requests.get("https://dev-digitalseer-ms.run.aws-usw02-pr.ice.predix.io/getRadiationData")
    response = requests.get("https://dev-digitalseer-ms.run.aws-usw02-pr.ice.predix.io/fetchRediationDataTable?periodEnd="+day)
    d=response.json()
    size=len(d["forecasts"])
    s1inv1=[]
    s1inv2=[]
    s2inv1=[]
    s2inv2=[]
    s3inv1=[]
    s3inv2=[]
    s4inv1=[]
    s4inv2=[]
    exinv1=[]
    exinv2=[]
    sr_sez_11=[]
    sr_sez_12=[]
    sr_sez_21=[]
    sr_sez_22=[]
    sr_sez_31=[]
    sr_sez_32=[]
    sr_sez_41=[]
    sr_sez_42=[]
    sr_sez_ex1=[]
    sr_sez_ex2=[]
    uniqueNames = []
    q=response1.json()
    #q=p["power"]
    size1=len(q["power"])
#    print size1
     
    
    datep=str(q["power"][0]["date"])
#    print datep
    n=len(q["power"][0]["data"])
#    print n
    x=0   
    for i in range(0,size,1):  
        adate=str(d["forecasts"][i]["period_end"]) #d["forecasts"]
        #print adate
        if(datep == adate): 
              uniqueNames.append(d["forecasts"][i]["ghi"]); 
              #print uniqueNames
              for i in range(0,size1,1): 
                  while(x<n):
                      building=str(q["power"][i]["data"][x]["name"])
                      if(building=="SEZ-Building1"):
                            s1inv1.append(q["power"][i]["data"][x]["Inverter1"])
                            s1inv2.append(q["power"][i]["data"][x]["Inverter2"])
#                            print s1inv1
#                            print s1inv2
                      elif(building=="SEZ-Building2"):
                           s2inv1.append(q["power"][i]["data"][x]["Inverter1"])
                           s2inv2.append(q["power"][i]["data"][x]["Inverter2"])
#                           print ("s2inv1",s2inv1)
#                           print ("s2inv2",s2inv2)
                      elif(building=="SEZ-Building3"):
                          s3inv1.append(q["power"][i]["data"][x]["Inverter1"])
                          s3inv2.append(q["power"][i]["data"][x]["Inverter2"])
#                          print ("s3inv1",s3inv1)
#                          print ("s3inv2",s3inv2)
                      elif(building=="SEZ-Building4"):
                          s4inv1.append(q["power"][i]["data"][x]["Inverter1"])
                          s4inv2.append(q["power"][i]["data"][x]["Inverter2"])
                      elif(building=="Everglades"):
                          exinv1.append(q["power"][i]["data"][x]["Inverter1"])
                          exinv2.append(q["power"][i]["data"][x]["Inverter2"])
#                          print ("ex1",exinv1)
#                          print ("ex2",exinv2)
                      x+=1
  
    for count in uniqueNames:
            sum1=369.4208*count
            sr_sez_11.append(sum1)#input power fron inverter 1 scz 1                   
            sum2=136.1024*count
            sr_sez_12.append(sum2)#input power fron inverter 2 scz 1
            sum3=349.9776*count
            sr_sez_21.append(sum3)#input power fron inverter 1 scz 2
            sum4=349.9776*count
            sr_sez_22.append(sum4) #input power fron inverter 2 scz 2 
            sum5=311.0912*count
            sr_sez_31.append(sum5)#input power fron inverter 1 scz 3
            sum6=295.53664*count
            sr_sez_32.append(sum6)#input power fron inverter 2 scz 3
            sum7=320.8128*count
            sr_sez_41.append(sum7)#input power fron inverter 1 scz 4
            sum8=124.43648*count
            sr_sez_42.append(sum8)#input power fron inverter 2 scz 4
            sum9=388.864*count
            sr_sez_ex1.append(sum9)#input power fron inverter 1 scz 5
            sum=388.864*count
            sr_sez_ex2.append(sum)#input power fron inverter 2 scz 5
            print sr_sez_32
    eff12=[]       
    eff21=[]
    eff22=[]
    eff31=[]
    eff32=[]
    eff41=[]
    eff42=[]
    eff51=[]
    eff52=[]
    eff11=[]
    msg=""
#    print sr_sez_21
    s1=len(s1inv1)   
#    print "the data in the list="+str(s1)
#    print ("***************** Efficiency for building SEZ 1************\n")
    for x in range(0,s1,1):
        try:
            efficiency=sr_sez_11[x]/s1inv1[x]
#            print efficiency
            eff11.append(efficiency)
            efficiency1=sr_sez_12[x]/s1inv2[x]
#            print efficiency1
            eff12.append(efficiency1)
        except:
            msg=str("Division by 0(zero) caused exception")  
            pass
            
    s2=len(s2inv1)   
#    print "the data in the list="+str(s2)
#    print ("***************** Efficiency for building SEZ 2************\n")
    for x in range(0,s2,1):
        try:
            efficiency=sr_sez_21[x]/s2inv1[x]
#            print efficiency
            eff21.append(efficiency)
            efficiency1=sr_sez_22[x]/s2inv2[x]
#            print efficiency1
            eff22.append(efficiency1)
        except:
            msg=str("Division by 0(zero) caused exception")  
            pass
    s3=len(s3inv1)   
#    print "the data in the list="+str(s3)
#    print ("***************** Efficiency for building SEZ 3************\n")
    for x in range(0,s3,1):
        try:
            efficiency=sr_sez_31[x]/s3inv1[x]
#            print efficiency
            eff31.append(efficiency)
            efficiency1=sr_sez_32[x]/s3inv2[x]
#            print efficiency1
            eff32.append(efficiency1)
        except:
            msg=str("Division by 0(zero) caused exception")  
            pass
    s4=len(s4inv1)   
#    print "the data in the list="+str(s4)
#    print ("***************** Efficiency for building SEZ 4************\n")
    for x in range(0,s4,1):
        try:
            efficiency=sr_sez_41[x]/s4inv1[x]
#            print efficiency
            eff41.append(efficiency)
            efficiency1=sr_sez_42[x]/s4inv2[x]
#            print efficiency1
            eff42.append(efficiency1)
        except:
            msg=str("Division by 0(zero) caused exception")  
            pass
    s5=len(exinv1)   
#    print "the data in the list="+str(s5)
#    print ("***************** Efficiency for ext road************\n")
    for x in range(0,s5,1):
        try:
            efficiency=sr_sez_ex1[x]/exinv1[x]
#            print efficiency
            eff51.append(efficiency)
            efficiency1=sr_sez_ex2[x]/exinv2[x]
#            print efficiency1
            eff52.append(efficiency1)
        except:
            msg=str("Division by 0(zero) caused exception")  
            pass
               
    return(json.dumps({"Efficiency_INV_1-Building_1":eff11,"Efficiency_INV_2-Building_1":eff12,"Efficiency_INV_1-Building_2":eff21,"Efficiency_INV_2-Building_2":eff22,
                      "Efficiency_INV_1-Building_3":eff31,"Efficiency_INV_2-Building_3":eff32,"Efficiency_INV_1-Building_4":eff41,"Efficiency_INV_2-Building_4":eff42,
                      "Efficiency_INV_1-Everglades":eff51,"Efficiency_INV_2-Everglades":eff52,"Error Message":msg}))               
