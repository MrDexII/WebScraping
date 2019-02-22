from Tkinter import *
import urllib
from bs4 import BeautifulSoup
import re
import codecs
import tkFont
from tkMessageBox import showerror, showinfo

global Tab1
Tab1 = []
global Tab2
Tab2 = []
global Tab3
Tab3 = []

def NewFile():
    global Tab1
    Tab1 = []
    global Tab2
    Tab2 = []
    global Tab3
    Tab3 = []
    url = "http://wyniki.interia.pl/"
    try:
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

            
       
        T.delete(0,END)
        for i in range(len(Tab3)):
            if i == 0:
                Tab3[i] = Tab3[i]*2
            else:
                Tab3[i] = Tab3[i]*2 + Tab3[i-1] 
        s = 0
        for i,l in zip(Tab1,Tab2):
            T.insert(END, i)
            T.insert(END, " ")
            if i == Tab1[0]:
                for i in range(s,Tab3[s]):
                    T.insert(END, Tab2[i])
            else:
                for i in range(Tab3[s-1],Tab3[s]):
                    T.insert(END, Tab2[i])
            s += 1   
            
    except:
        showerror("ERROR","Operation Failed")
    else:
        showinfo("Success","Operation Successful")
    
def save_to_file():
    try:
        plik = codecs.open('Wyniki Meczow.doc','w', encoding='utf-8')
        s = 0
        for i,l in zip(Tab1,Tab2):
            plik.writelines(" " + "\n")
            plik.writelines(" " + "\n")
            plik.writelines(i + "\n")
            plik.writelines(" " + "\n")
            plik.writelines(" " + "\n")
            if i == Tab1[0]:
                for i in range(s,Tab3[s]):
                    plik.writelines(Tab2[i] + "\n")
            else:
                for i in range(Tab3[s-1],Tab3[s]):
                    plik.writelines(Tab2[i] + "\n")
            s += 1
        plik.close()
    except:
        showerror("ERROR","Operation failed")
    else:
        showinfo("Success","Operation successful.\nYour information is stored in file called Wyniki Meczow.doc ")

def Clear():
    T.delete(0,END)
    global Tab1
    Tab1 = []
    global Tab2
    Tab2 = []
    global Tab3
    Tab3 = []

root = Tk()
root.title("Wyniki Meczow")
S = Scrollbar(root)
T = Listbox(root, yscrollcommand = S.set ,height=25, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set,font = tkFont.Font(family='Calibri',size=10))

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
filemenu.add_separator()
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New Search", command=NewFile)
filemenu.add_command(label="Clear List", command=Clear)
filemenu.add_command(label="Save to File", command=save_to_file)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)



root.mainloop()