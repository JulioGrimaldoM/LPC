from tkinter import *
import requests
from bs4 import BeautifulSoup
import os

#funciones
def Web_Scraping():
    try:
        print(text.get())
        url=text.get()
        respuesta=requests.get(url)
        soup=BeautifulSoup(respuesta.content, "html.parser")
        #obtenemos los parrafos de la pagina
        txt=soup.find_all("p")
        title=soup.title.string
        parr=len(txt)
        for i in range(parr):
            #Creamos el arcivo txt con el nombre que tiene la pagina web
            f=open("%s.txt"%(title),"a")
            #el linesep nos ayuda en poner un espacio y respetemos los saltos de linea
            #porque sino nos pone todo junto en el archivo txt
            print(txt[i].getText()+os.linesep)
            f.write(txt[i].getText()+ os.linesep)
            f.close()
    except Exception as e:
        print(str(e))

#Frame raiz
raiz=Tk()
raiz.title("Web Scraping")
miframe=Frame(raiz,width=1200,height=600)
miframe.pack()

text=Entry(miframe)
text.grid(row=0,column=1,padx=10,pady=10)

label=Label(miframe,text="Url:")
label.grid(row=0,column=0,sticky="e",padx=10,pady=10)

#boton 1
boton1=Button(miframe, text="iniciar", borderwidth=2,command=lambda:Web_Scraping())
boton1.grid(row=2,column=2, padx=10,pady=10)

raiz.mainloop()
