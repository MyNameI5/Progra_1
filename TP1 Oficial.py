import requests
from bs4 import BeautifulSoup

#Entradas: nombreIndice(las iniciales del indice cuyos datos van a ser extraidos)
#Salidas: la informacion financiera sobre el indice deseado
#Restricciones: "nombreIndice" solo puede ser 'DJI', 'NDX', 'BVSP', 'DAX', 'STOXX50E', 'FTSE', 'IBEX' o 'N225'.

def infoIndice(nombreIndice):
    parametros_deBusqueda= {'DJI': 'us-30', 'NDX': 'nq-100', 'BVSP': 'bovespa', 'DAX': 'germany-30', 'STOXX50E': 'eu-stoxx50', 'FTSE': 'uk-100','IBEX':'spain-35', 'N225': 'japan-ni225'}

    if nombreIndice in parametros_deBusqueda:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} #Evita ser reconocido como un programa
        parametros = parametros_deBusqueda[nombreIndice]
        url = 'https://es.investing.com/indices/' + parametros
        url = requests.get(url , headers = headers)
        html = url.text #obtiene el html en forma de texto

        print('Fuente de datos: ' + url.url + '\n')

        soup = BeautifulSoup(html, 'html.parser') #ordena el html en una fotma legible
  
    
        for tags in soup.find_all('div', class_="top bold inlineblock"):

            datosPrecio = tags.find_all('span', attrs={'dir':"ltr"})
            precioActual = datosPrecio[0]
            diferencia = datosPrecio[1]
            diferencia_enPorcentaje = datosPrecio[2]                 

        datos = soup.find_all('ul', class_="bold")

        datos = datos[0].find_all('li')

        precioCierre = datos[0]
        precioApertura = datos[1]
        rangoDiario = datos[2]
    
        print ('Valor: ' + '\t' +'\t' + str(precioActual.text))
        print ('Diferencia: ' + '\t' + str(diferencia.text))
        print ('Diferencia % ' + '\t' + str(diferencia_enPorcentaje.text))
        print(precioCierre.text)
        print(precioApertura.text)
        print(rangoDiario.text)

    else:
        print('Error, ingrese un índice válido')


#Entradas: nombreIndice(las iniciales del indice cuyos datos van a ser extraidos)
#Salidas: informacion financiera sobre las empresas relacionadas con "nombreIndice"
#Restricciones: "nombreIndice" solo puede ser 'DJI', 'NDX', 'BVSP', 'DAX', 'STOXX50E', 'FTSE', 'IBEX' o 'N225'.
        
def empresasIndice(nombreIndice):
    parametros_deBusqueda= {'DJI': 'us-30', 'NDX': 'nq-100', 'BVSP': 'bovespa', 'DAX': 'germany-30', 'STOXX50E': 'eu-stoxx50', 'FTSE': 'uk-100','IBEX':'spain-35', 'N225': 'japan-ni225'}

    if nombreIndice in parametros_deBusqueda:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} #Evita ser reconocido como un programa
        parametros = parametros_deBusqueda[nombreIndice]
        url = 'https://es.investing.com/indices/' + parametros + '-components'
        url = requests.get(url , headers = headers)
        html = url.text     #obtiene el html en forma de texto

        print('Fuente de datos: ' + url.url + '\n') 
     
        soup = BeautifulSoup(html, 'html.parser') #ordena el html en una fotma legible

        table = soup.find_all('table', attrs={"id":"cr1"})

        for tags in table:
            cuerpo = tags.find_all("tbody")

        for tr in cuerpo:
            tr = tr.find_all("tr")


        print("Nombre" + "\t" + "\t" + "\t" + "  |Último" + "\t" + "  |Máximo" + "  |Mínimo" + " |Var" + "\t" + " |Var %" + "\t" + "  |Vol.")
        for td in tr:
            contenidos = td.find_all("td")
            contenidos = contenidos[1:8]
        
            nombre = contenidos[0].text
            ultimo =contenidos[1].text
            maximo = contenidos[2].text 
            minimo =contenidos[3].text
            variacion = contenidos[4].text
            variacion_porcentaje = contenidos[5].text
            volumen = contenidos[6].text

            print(nombre + "\t" + "\t" + "\t" + ultimo + "\t" + maximo + "\t" + minimo + "\t" + variacion + "\t" + variacion_porcentaje +"\t" + volumen)

    else:
        print('Error, ingrese un índice válido')


#Entradas: codigoEmpresa(el codigo de la empresa a investigar), nombreIndice(el nombre del indice al que pertenece la empresa)
#Salidas: las ultimas noticias, el directivo y las empresas relacionadas de la empresa especificada
#Restricciones: "codigoEmpresa" debe pertenecer al indice .

def noticiasEmpresa(codigoEmpresa, nombreIndice):
    print(noticias(codigoEmpresa, nombreIndice))
    print('///////////////////////////////////////////////////////////////////' + '\n')
    print('///////////////////////////////////////////////////////////////////')
    print(directivo(codigoEmpresa, nombreIndice))
    



#Funciones para realizar la #3
def noticias(codigoEmpresa, nombreIndice):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} #Evita ser reconocido como un programa
    
    url = 'https://www.google.com/finance/company_news?q='+ nombreIndice+ '%3'+ codigoEmpresa+'&ei'
    url = requests.get(url , headers = headers)
    html = url.text #obtiene el html en forma de texto
    print('NOTICIAS')
    print('Fuente de datos: ' + url.url + '\n')

    soup = BeautifulSoup(html, 'lxml')
    
    numero_noticia = 0
    while numero_noticia <= 9:
        for noticias in soup.find_all('div', attrs ={'class' : 'sfe-section', 'id':'news-main'}):
            tags = noticias.find_all('div', attrs= {'class':'g-section news sfe-break-bottom-16'})
            print(tags[numero_noticia].text)
            print('---------------------------------------')
        numero_noticia += 1
        

def directivo(codigoEmpresa, nombreIndice):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} #Evita ser reconocido como un programa
    
    url = 'https://www.google.com/finance?q=' + nombreIndice+ '%3'+ codigoEmpresa+'&ei'
    url = requests.get(url , headers = headers)
    html = url.text #obtiene el html en forma de texto

    soup = BeautifulSoup(html, 'html.parser')

    directivo = soup.find_all('div', id = 'management')

    print('DIRECTIVOS')
    print('Fuente de datos: ' + url.url + '\n')
    print (directivo[0].text)

