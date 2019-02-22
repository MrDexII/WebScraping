import urllib
from bs4 import BeautifulSoup
import re

url = "http://wyniki.interia.pl/"
htmlfile = urllib.urlopen(url)

htmltext = htmlfile.read()

soup = BeautifulSoup(htmltext)

g_data = soup.find_all(id="mainContainer")

g1_data = g_data[0].find_all(class_=re.compile("boxMatchesDetailed"))


for item in g1_data:
    
    licz = 0
    a = len(item.contents[5].find_all("span", {"class": "teamA"}))
    r = len(item.contents[5].find_all("span", {"class": "teamB"}))
    
    if a == r:
        print "ok"
        print a
        print r
    else:
        print "bad"
        print r
        print a
   
    print(item.contents[3].find_all('span')[0].text +" "+ item.contents[3].find_all('span')[1].text + item.contents[3].find_all('span')[2].text)
    print (" ")
    print (" ")
    print (" ")
    
    while licz < a:
       
        print ("Status: " + item.contents[5].find_all("span", {"class": "status"})[licz].text + " " + item.contents[5].find_all("span", {"class":"minute"})[licz].text)
        print (item.contents[5].find_all("span", {"class": "teamA"})[licz].text + " " + item.contents[5].find_all("span", {"class": "goals"})[licz].text + " " + item.contents[5].find_all("span", {"class": "teamB"})[licz].text)
        print (" ")
        licz += 1
    print (" ")
    print(" ")