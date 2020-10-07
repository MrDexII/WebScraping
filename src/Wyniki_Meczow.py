from tkinter import OptionMenu, StringVar, Scrollbar, Listbox, Menu, Tk, END, RIGHT, LEFT, Y
import urllib.request
from bs4 import BeautifulSoup
import re
import codecs
import tkinter.font as TkFont
from tkinter.messagebox import showerror, showinfo

global Tab1
Tab1 = []
global Tab2
Tab2 = []
global Tab3
Tab3 = []

def search():
    try:
        url = "http://wyniki.interia.pl/"
        with urllib.request.urlopen(url) as htmlfile:
            htmltext = htmlfile.read()

        soup = BeautifulSoup(htmltext)

        g_data = soup.find_all(id="mainContainer")

        g1_data = g_data[0].find_all(class_=re.compile("boxMatchesDetailed"))

        for item in g1_data:

            licz = 0
            a = len(item.contents[5].find_all("span", {"class": "teamA"}))
            Tab3.append(a)

            Tab1.append(item.contents[3].find_all('span')[
                        0].text + " " + item.contents[3].find_all('span')[1].text + item.contents[3].find_all('span')[2].text)

            while licz < a:

                Tab2.append("Status: " + item.contents[5].find_all("span", {"class": "status"})[
                            licz].text + " " + item.contents[5].find_all("span", {"class": "minute"})[licz].text)
                Tab2.append(item.contents[5].find_all("span", {"class": "teamA"})[licz].text + " " + item.contents[5].find_all(
                    "span", {"class": "goals"})[licz].text + " " + item.contents[5].find_all("span", {"class": "teamB"})[licz].text)
                licz += 1
        for i in range(len(Tab3)):
            if i == 0:
                Tab3[i] = Tab3[i]*2
            else:
                Tab3[i] = Tab3[i]*2 + Tab3[i-1]
    except:
        showerror("ERROR", "Twoje wyszukiwanie nie powidlo sie")
    else:
        showinfo("Sukces", "Twoje wyszukiwanie powidlo sie")

def NewFile():
    Clear()
    search()
    s = 0
    for i, l in zip(Tab1, Tab2):
        listBox.insert(END, " ")
        listBox.insert(END, " ")
        listBox.insert(END, i)
        listBox.insert(END, " ")
        listBox.insert(END, " ")
        if i == Tab1[0]:
            for i in range(s, Tab3[s]):
                listBox.insert(END, Tab2[i])
        else:
            for i in range(Tab3[s-1], Tab3[s]):
                listBox.insert(END, Tab2[i])
        s += 1

def save_to_file():
    try:
        plik = codecs.open('Wyniki Meczow.txt', 'w', encoding='utf-8')
        s = 0
        for i, l in zip(Tab1, Tab2):
            plik.writelines(" " + "\n")
            plik.writelines(" " + "\n")
            plik.writelines(i + "\n")
            plik.writelines(" " + "\n")
            plik.writelines(" " + "\n")
            if i == Tab1[0]:
                for i in range(s, Tab3[s]):
                    plik.writelines(Tab2[i] + "\n")
            else:
                for i in range(Tab3[s-1], Tab3[s]):
                    plik.writelines(Tab2[i] + "\n")
            s += 1
        plik.close()
    except:
        showerror("ERROR", "Operacja nie powidla sie")
    else:
        showinfo(
            "Sukces", "Operacja powidlo sie.\nTwoj wynik wyszukiwania jest zapisany do pliku Wyniki Meczow.txt")

def Clear():
    listBox.delete(0, END)
    global Tab1
    Tab1 = []
    global Tab2
    Tab2 = []
    global Tab3
    Tab3 = []
    studFiles.set("Wybierz lige")

def lista(selection):
    listBox.delete(0, END)
    for i in range(len(Tab1)):
        if selection == Tab1[i]:
            listBox.insert(END, Tab1[i])
            listBox.insert(END, " ")
            if i == 0:
                for l in range(i, Tab3[i]):
                    listBox.insert(END, Tab2[l])
            else:
                for r in range(Tab3[i-1], Tab3[i]):
                    listBox.insert(END, Tab2[r])


root = Tk()
root.title("Wyniki Meczow")
root.geometry('350x450')

search()
studFiles = StringVar()
studFiles.set("Wybierz lige")
studDropDown = OptionMenu(root, studFiles, "--", *Tab1, command=lista)
studDropDown.config(width=50)
studDropDown.pack()

scrollbar = Scrollbar(root)
listBox = Listbox(root, yscrollcommand=scrollbar.set, height=25, width=50)
scrollbar.pack(side=RIGHT, fill=Y)
listBox.pack(side=LEFT, fill=Y)
scrollbar.config(command=listBox.yview)
listBox.config(yscrollcommand=scrollbar.set,
         font=TkFont.Font(family='Calibri', size=10))

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
filemenu.add_separator()
menu.add_cascade(label="Plik", menu=filemenu)
filemenu.add_command(label="Nowe wyszukiwanie", command=NewFile)
filemenu.add_command(label="Wyczysc liste", command=Clear)
filemenu.add_command(label="Zapisz do pliku", command=save_to_file)

filemenu.add_separator()
filemenu.add_command(label="Wyjscie", command=root.quit)

root.mainloop()