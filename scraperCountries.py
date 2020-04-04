from bs4 import BeautifulSoup
from country import country
from countryTeam import countryTeam
import csv

import requests


class scraperCountries:
    # Variable que contiene todos los paises
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

        for aCountries in groupCountries.find_all("a"):
            urlCountry = aCountries.get('href')
            countryName = aCountries.get('title')
            urlCountry = self._urlBaseCountries+urlCountry
            co = country(countryName, urlCountry)

            if (len(self._countryList) > 0):
                bhas = any(x.countryName ==
                           countryName for x in self._countryList)
                if (bhas == False):
                    self._countryList.append(co)
            else:
                self._countryList.append(co)

        print("Se han descargado ", len(self._countryList), " paises")

        for indice, Cou in enumerate(self._countryList):

            pageCountry = requests.get(Cou.urlCountry)
            soupCountry = BeautifulSoup(pageCountry.content, "lxml")
            teams = soupCountry.find('tbody')
            countryTeams = []

            for fila in teams.find_all("tr"):
                row_text = [x.text for x in fila.find_all('td')]

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

                te = countryTeam(Cname, tName, gPlayed, wHome, dHome, lHome,
                                 wAway, dAway, lAway, wTotal, dTotal, lTotal, points, position)
                countryTeams.append(te)

                Cou.actualizarTeams(countryTeams)
                self._countryList[indice] = Cou

        with open('uefa_clubs.csv', 'w', encoding='utf-8') as result_file:
            wr = csv.writer(result_file, delimiter=',', lineterminator='\n')
            for Cou in self._countryList:
                listaTotal = Cou.countryToCsv()
                wr.writerows(listaTotal)
