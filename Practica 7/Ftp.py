from ftplib import FTP, FTP_PORT
from typing import List
#Lo siento profe pero no pude hacer bien esta practica se me hizo muy dificil hacer la filtracion para solo tener los archivos txt
data=[]
data1=[]
ftp = FTP()
ftp.connect("ftp.heanet.ie", 21)
ftp.login('anonymous', '')
ftp.dir()
ftp.cwd('pub')
ftp.dir(data.append)
ftp.cwd('/')
ftp.cwd("mirrors")
ftp.dir(data1.append)
print("Archivos de pub: "+ data)
print("Archivos de mirrors: "+ data1)
ftp.close()
