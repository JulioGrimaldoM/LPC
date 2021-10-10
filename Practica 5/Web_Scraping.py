import requests
from bs4 import BeautifulSoup
import os
#Escribimos el link de cualquier pagina 
url=input("url del sitio web: ")
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