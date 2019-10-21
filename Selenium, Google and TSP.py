import pandas as pd
import datetime
import tsp
import os
import csv
import base64
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = False
temppath=r# path of operation
majorlist=[]
filename=temppath+"\\"#CSV file of locations
data=pd.read_csv(filename)
y=data.shape
z=data.columns
for i in range(y[1]):
    majorlist=data.iloc[:,i]
    length=len(majorlist)
    distancematrix= [[[] for x in range(length)] for y in range(length)]
    timematrix= [[[] for x in range(length)] for y in range(length)]
    driver = webdriver.Chrome(executable_path=temppath+"\\chromedriver.exe", options = options)
    for i in range(len(distancematrix)):
        for j in range(i):
            if distancematrix[i][j]==[]:
                import time
                if i==j:
                    distancematrix[i][i]=0
                    timematrix[i][i]=0
                else:
                    time.sleep(1)
                    driver.get("https://www.google.com/maps")
                    location=driver.find_element_by_xpath('//*[@id="searchboxinput"]')
                    location.send_keys(majorlist[i])
                    time.sleep(1)
                    search=driver.find_element_by_xpath('//*[@id="searchbox-directions"]')
                    search.click()
                    time.sleep(1)
                    transport=driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[2]/button/div[1]')
                    transport.click()
                    time.sleep(1)
                    destination= driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input')
                    destination.send_keys(majorlist[j])
                    from selenium.webdriver.common.keys import Keys
                    destination.send_keys(Keys.RETURN)
                    time.sleep(4)
                    nn=driver.find_element_by_xpath('//*[@id="section-directions-trip-0"]')
                    nn.click()
                    time.sleep(4)
                    distance=driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[3]/div[1]/h1/span[1]/span[2]/span')
                    time=driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[3]/div[1]/h1/span[1]/span[1]')
                    k=distance.text
                    k=k.replace(" km","")
                    k=float(k)
                    distancematrix[i][j]=k
                    distancematrix[j][i]=k
                    m=time.text
                    if 'h' in m and 'min' in m:
                        m=m.split()
                        m[0]=int(m[0])*60
                        m[2]=int(m[2])+int(m[0])
                        timematrix[i][j]=m[2]
                        timematrix[j][i]=m[2]
                    if 'h' in m and 'min' not in m:
                        m=m.split()
                        m[0]=int(m[0])*60
                        timematrix[i][j]=int(m[0])
                        timematrix[j][i]=int(m[0])
                    if'h' not in m and 'min' in m:
                        m=m.split()
                        timematrix[i][j]=int(m[0])
                        timematrix[j][i]=int(m[0])

    driver.close()
    mat=timematrix  #Matrix created
    r = range(len(mat))
    dist = {(i, j): mat[i][j] for i in r for j in r}
    x=tsp.tsp(r, dist)
    l=[]
    for i in range(len(timematrix[0])-1):
        l.append(timematrix[x[1][i]][x[1][i+1]])
    timespent=[]
    for i in range(len(majorlist)):
        print("Enter visit duration in for :",majorlist[i])
        timespent.append(int(input("in minutes")))
    start=int(input("Enter starting hour : 8 or 9\n"))
    end=int(input("Enter ending hour 10 or 11\n"))
    limit=((end+12)-start)*60+480
    value=sum(l)+sum(timespent)
    