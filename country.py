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
    
    def actualizarTeams(self, x):
        self._teams = x

    def countryToCsv(self):
        datos_csv=[]
        for ct in self._teams:
            datos_csv.append(ct.countryTeamToCsv())
        return datos_csv
            
            