from bs4 import BeautifulSoup
from country import country
from countryTeam import countryTeam
import csv

import requests


class scraperCountries:
    # Variable que contiene todos los países
    _countryList = []

    def __init__(self, urlMain, urlBaseCountries):
        self._urlMain = urlMain
        self._urlBaseCountries = urlBaseCountries

    def execute(self):
        page = requests.get(self._urlMain)
        soup = BeautifulSoup(page.content, "lxml")
        # El div con id:ListDomesticLeague es el contenedor principal que contiene todos los países
        groupCountries = soup.find('div', attrs={'id': 'ListDomesticLeague'})
        # Para cada país encontrado descargo el enlace en el cual podre encontrar todos las clasificaciones
        #La dirección de las clasificaciones de cada país, se encuentran dentro de <a href>
        #Cada vez que se encuentra un <a>, estamos en un nuevo país
        for aCountries in groupCountries.find_all("a"):
            #Guardamos la url del país
            urlCountry = aCountries.get('href')
            #Guardamos el nombre del país
            countryName = aCountries.get('title')
            #Creamos una nueva url para poder descargar todos los equipos
            urlCountry = self._urlBaseCountries+urlCountry
            co = country(countryName, urlCountry)

            #Comprobamos que el país no se haya descargado, si ya se ha descargado, se ignora
            if (len(self._countryList) > 0):
                bhas = any(x.countryName == countryName for x in self._countryList)
                if (bhas == False):
                    self._countryList.append(co)
            else:
                self._countryList.append(co)

        print("Se descargara ", len(self._countryList), " paises")

        #En esta iteración se descarga cada equipo de cada país
        #En el primer bucle, se itera para cada país encontrado 
        for indice, Cou in enumerate(self._countryList):

            pageCountry = requests.get(Cou.urlCountry)
            soupCountry = BeautifulSoup(pageCountry.content, "lxml")
            #Todos los equipos están dentro del cuerpo del html
            teams = soupCountry.find('tbody')
            countryTeams = []

            #Cada fila, contiene cada equipo que hay que descargar
            for fila in teams.find_all("tr"):
                row_text = [x.text for x in fila.find_all('td')]
                
                #Descargamos cada columna, que contiene los atributos de cada equipo de futbol
                Cname = Cou.countryName
                tName = row_text[2]
                gPlayed = row_text[4]
                wHome = row_text[5]
                dHome = row_text[6]
                lHome = row_text[7]
                wAway = row_text[8]
                dAway = row_text[9]
                lAway = row_text[10]
                wTotal = row_text[11]
                dTotal = row_text[12]
                lTotal = row_text[13]
                points = row_text[14]
                position = row_text[0]

                #Creamos un nuevo objeto de equipo de futbol con los valores que se escribirán en el csv
                te = countryTeam(Cname, tName, gPlayed, wHome, dHome, lHome,
                                 wAway, dAway, lAway, wTotal, dTotal, lTotal, points, position)
                countryTeams.append(te)

                #Actualizamos la lista de equipos dentro del país
                Cou.actualizarTeams(countryTeams)
                self._countryList[indice] = Cou

        #Finalmente guardamos el csv en disco
        with open('uefa_clubs.csv', 'w', encoding='utf-8') as result_file:        
            wr = csv.writer(result_file, delimiter=',', lineterminator='\n')
            wr.writerow(["countryName","teamName","gamesPlayed","wHome","dHome","lHome","wAway","dAway","lAway","wTotal","dTotal","lTotal","points","position"])
            #Para cada pais descargado, generamos sus datos en formato csv y lo escribimos en disco
            for Cou in self._countryList:
                listaTotal = Cou.countryToCsv()
                wr.writerows(listaTotal)

        print("Fin del proceso")