import Buscar,Descargar_IMG, os, requests, bs4, Buscador_google, Informacion, Web_Scraping, Evenntos

if __name__=="__main__":
    print("=======Bienvenido======")
    print("Estos son todos los archivos .txt")
    Buscar.encontrar()
    print("Opciones \n 1)Leer el Archivo \n 2)agregar \n 3)eliminar \n 4)Web scraping \n 5)Salir ")
    op=int(input("Que quieres hacer "))
    while op!=5:
        if op==1:
            arc=input("Escribe el nombre del archivo ")
            Buscar.read(arc)
        elif op==2:
            arc=input("Escribe el nombre del archivo ")
            exc=str(input("Quieres buscar desde google y/n"))
            if exc=="y":
                Buscador_google.buscarG()
                Buscar.agregar(arc)
            else:
                Buscar.agregar(arc)   
        elif op==3:
            arc=input("Escribe el nombre del archivo ")
            Buscar.eliminar(arc)
        elif op==4:
            print("<--------Bienvenido al Web scraping-------->")
            print("Opciones \n 1)Noticias \n 2)Informacion \n 3)Descaargar imagenes \n 4)Eventos \n 5)Salir")
            ops=int(input("Que quieres hacer "))
            while ops!=5:
                if ops==1:
                    pagina=input("Escribe la url ")
                    Web_Scraping.noticias(pagina)
                elif ops==2:
                    pagina=input("Escribe la url ")
                    Informacion.Datos_Daniel(pagina)
                elif ops==3:
                    pagina=input("Escribe la url ")
                    ide=input("Escribe el id ")
                    Descargar_IMG.img(pagina,ide)
                elif ops==4:
                    Evenntos.event()
                    
                print("Opciones \n 1)Noticias \n 2)Informacion \n 3)Descaargar imagenes \n 4)Eventos \n 5)Salir")
                ops=int(input("Que quieres hacer "))
        print("Opciones \n 1)Leer el Archivo \n 2)agregar \n 3)eliminar \n 4)Web scraping \n 5)Salir ")
        op=int(input("Que quieres hacer "))

print("Adios")
        
