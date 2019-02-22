import urllib
from bs4 import BeautifulSoup
import re
import codecs
from Tkinter import *



def search():
    global Tab
    Tab = []
    url = "http://wyniki.interia.pl/"

    htmlfile = urllib.urlopen(url)
   
    htmltext = htmlfile.read()
    
    soup = BeautifulSoup(htmltext)

    g_data = soup.find_all(id="mainContainer")

    g1_data = g_data[0].find_all(class_=re.compile("boxMatchesDetailed"))
    

    for item in g1_data:
    
        licz = 0
        a = len(item.contents[5].find_all("span", {"class": "team teamA"}))
    
        Tab.append(item.contents[3].find_all('span')[0].text +" "+ item.contents[3].find_all('span')[1].text + item.contents[3].find_all('span')[2].text)
        Tab.append(" ")
        Tab.append(" ")
        Tab.append(" ")
        
        while licz < a:
            Tab.append("Status: " + item.contents[5].find_all("span", {"class": "status"})[licz].text + " " + item.contents[5].find_all("span", {"class":"minute"})[licz].text)
            Tab.append(item.contents[5].find_all("span", {"class": "team teamA"})[licz].text + " " + item.contents[5].find_all("span", {"class": "goals"})[licz].text + " " + item.contents[5].find_all("span", {"class": "team teamB"})[licz].text)
            Tab.append(" ")
            licz += 1
        Tab.append(" ")
        Tab.append(" ")
        
def do_pliku(tablica):
    plik = codecs.open('Wyniki Meczow.doc','w', encoding='utf-8')
    for i in tablica:
        plik.writelines(i + "\n")
    plik.close()

search()
do_pliku(Tab)

root = Tk()
licz = 0
#root.geometry('450x450')
root.title("Wyniki Meczow")
S = Scrollbar(root)
T = Listbox(root, yscrollcommand = S.set ,height=25, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
for i in Tab:
    quote = Tab[licz]
    T.insert(END, quote)
    licz +=1
root.mainloop(  )