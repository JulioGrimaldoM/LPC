import os
def buscarG():
    try:
        from googlesearch import search
    except:
        os.system("pip install google")
        print("instalando...")
        print("volver a ejecutar")
        exit()
    query=input("Busqueda: ")
    print("Buscando...")
    for enlace in search(query, tld="com", num=15, stop=15, pause=5):
        print(enlace)
if __name__=="__main__":
    buscarG()
