import requests, os, bs4

def img(pg,idp):
    url = pg
    os.makedirs('Imagenes', exist_ok=True)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    ID="#"+idp
    print(ID)
    comicElem = soup.select(ID+" img")
    if comicElem == []:
        print('No se encontró.')
    else:
        comicUrl = comicElem[0].get('src')
        print('Descargando %s...' % (comicUrl))
        response = requests.get(comicUrl)
        if response.status_code == 200:
            imageFile = open(os.path.join('Imagenes', os.path.basename(comicUrl)), 'wb')
            for chunk in response.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
    print("Exito")
if __name__=="__main__":
    ur=input("Escribe la url")
    ide=input("Escribe el ID")
    img(ur,ide)

