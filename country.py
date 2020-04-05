#Clase que modela un País, contiene una lista de equipos de fútbol
from countryTeam import countryTeam

class country:
    _teams=[]
    def __init__(self, countryN, url):
        self._countryName= countryN
        self._urlCountry = url
        self._teams=[]
        
    @property
    def countryName(self):
        return self._countryName    

    @property
    def urlCountry(self):
        return self._urlCountry    
    
    #Actualiza el atributo teams que contiene la lista de equipos de futbol
    def actualizarTeams(self, x):
        self._teams = x

    #Retorna todos los equipos de futbol del pais en formato csv
    def countryToCsv(self):
        datos_csv=[]
        for ct in self._teams:
            datos_csv.append(ct.countryTeamToCsv())
        return datos_csv
            
            