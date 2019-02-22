from Tkinter import *
import urllib
from bs4 import BeautifulSoup
import re
import codecs
import tkFont
from tkMessageBox import showerror, showinfo



def NewFile():
    global Tab
    Tab = []
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
            
       
        T.delete(0,END)
        licz = 0    
        for i in Tab:
            quote = Tab[licz]
            T.insert(END, quote)
            licz +=1
    except:
        showerror("ERROR","Operation Failed")
    else:
        showinfo("Success","Operation Successful")
    
def save_to_file():
    try:
        plik = codecs.open('Wyniki Meczow.doc','w', encoding='utf-8')
        for i in Tab:
            plik.writelines(i + "\n")
        plik.close()
    except:
        showerror("ERROR","Operation failed")
    else:
        showinfo("Success","Operation successful.\nYour information is stored in file called Wyniki Meczow.doc ")

def Clear():
    T.delete(0,END)
    global Tab
    Tab = []

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