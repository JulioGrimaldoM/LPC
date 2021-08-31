import os
def read(archivo):
    try:
        archivo=archivo+".txt"
        print("El contenido es: ")
        file=open(archivo,"r")
        for line in file:
            print(line, end="")
    except FileNotFoundError:
        print("No se encontro")

def encontrar():
    count = 0
    for dirpath, dirnames, filenames in os.walk("."):
        for name in filenames:
            if ".txt" in name:
                print ("Archivo",count+1,":",name)
                count=count+1
                        
def agregar(var):
    var=var+".txt"
    file=open(var,"a")
    while True:
        url=input("Escribe la url que quieres agregar al "+var+" ")
        file.write(url+"\n")
        con=input("Quieres agregar mas y/n ")
        if con!="y":
            break

def eliminar(var):
    read(var)
    var=var+".txt"
    dele=str(input("Que url quieres eliminar "))
    with open(var, "r") as f:
        lines = f.readlines()
    with open(var, "w") as f:
        for line in lines:
            if line.strip("\n") != dele:
                f.write(line)

if __name__=="__main__":
    arc=input("Escribe el archivo ")
    encontrar()
    read(arc)
    eliminar(arc)
    agregar(arc)

    
