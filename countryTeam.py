class countryTeam:
    def __init__(self, country, teamName, gamesPlayed, wHome, dHome, lHome, wAway, dAway, lAway, wTotal, dTotal, lTotal, points,position):
        self._countryName= country	#pais
        self._teamName = teamName	#nombre del equipo
        self._gamesPlayed=gamesPlayed	#partidos jugados
        self._wHome=wHome		#partidos ganados en casa
        self._dHome=dHome		#partidos empatados en casa
        self._lHome=lHome		#partidos perdiods en casa
        self._wAway=wAway		#partidos ganados fuera
        self._dAway=dAway		#partidos empatados fuera
        self._lAway=lAway		#partidos perdidos fuera
        self._wTotal=wTotal		#partidos totales ganados
        self._dTotal=dTotal		#partidos totales empatados
        self._lTotal=lTotal		#partidos totales perdidos
        self._points=points		#puntos obtenidos
        self._position=position		#posición en la clasificación

    @property
    def country(self):
        return self._country    

    @property
    def teamName(self):
        return self._teamName    

    ##########Falta añadir todas las demas propiedades

    @property
    def gamesPlayed(self):
        return self._gamesPlayed

    @property
    def wHome(self):
        return self._wHome

    @property
    def dHome(self):
        return self._dHome

    @property
    def lHome(self):
        return self._ldHome

    @property
    def wAway(self):
        return self._wAway

    @property
    def dAway(self):
        return self._dAway

    @property
    def lAway(self):
        return self._lAway

    @property
    def wTotal(self):
        return self._wTotal

    @property
    def dTotal(self):
        return self._dTotal

    @property
    def lTotal(self):
        return self._lTotal

    @property
    def points(self):
        return self._points

    @property
    def position(self):
        return self._position
    

    def countryTeamToCsv(self):
        datos_csv=[self._countryName,self._teamName,self._gamesPlayed,self._wHome,self._dHome,self._lHome,self._wAway,self._dAway,self._lAway,self._wTotal,self._dTotal,self._lTotal,self._points,self._position]
        return datos_csv