import urllib
from bs4 import BeautifulSoup
import re
import codecs
from Tkinter import *



Tab1 = []
Tab2 = []
Tab3 = []

url = "http://wyniki.interia.pl/"

htmlfile = urllib.urlopen(url)
   
htmltext = htmlfile.read()
    
soup = BeautifulSoup(htmltext)

g_data = soup.find_all(id="mainContainer")

g1_data = g_data[0].find_all(class_=re.compile("boxMatchesDetailed"))
    

for item in g1_data:
    
    licz = 0
    a = len(item.contents[5].find_all("span", {"class": "team teamA"}))
    Tab3.append(a)
    
    Tab1.append(item.contents[3].find_all('span')[0].text +" "+ item.contents[3].find_all('span')[1].text + item.contents[3].find_all('span')[2].text)

        
    while licz < a:
        Tab2.append("Status: " + item.contents[5].find_all("span", {"class": "status"})[licz].text + " " + item.contents[5].find_all("span", {"class":"minute"})[licz].text)
        Tab2.append(item.contents[5].find_all("span", {"class": "team teamA"})[licz].text + " " + item.contents[5].find_all("span", {"class": "goals"})[licz].text + " " + item.contents[5].find_all("span", {"class": "team teamB"})[licz].text)
        licz += 1
    



for i in range(len(Tab3)):
    if i == 0:
        Tab3[i] = Tab3[i]*2
    else:
        Tab3[i] = Tab3[i]*2 + Tab3[i-1]
   
    
"""s = 0
for i,l in zip(Tab1,Tab2):
    print i
    if i == Tab1[0]:
        print Tab2[s:Tab3[s]]
    else:
        print Tab2[Tab3[s-1]:Tab3[s]]
    s += 1"""
s = 0
for i,l in zip(Tab1,Tab2):
    print " "
    print " "
    print i
    print " "
    print " "
    if i == Tab1[0]:
        for i in range(s,Tab3[s]):
            print Tab2[i]
    else:
        for i in range(Tab3[s-1],Tab3[s]):
            print Tab2[i]
    s += 1

    
    