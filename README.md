<H1>GitHub de la práctica Web Scraping de la asignatura Tipología y Ciclo de Vida de los Datosdel Master en Data Science</br></br></H1>
<p><h2>Autores:  </h2></p>
          <b>Xus Garcia de la Vega Matas</b> &nbsp; github: https://github.com/xusgvm</br>
          <b>Anddy Aldave Valle</b> &nbsp;github: https://github.com/aaldaveva</p>

El objetivo de la práctica consiste en la extracción de las clasificaciones de equipos de fútbol profesional en todas las ligas europeas 

<p>Para ejecutar el script es necesario instalar la siguientes bibliotecas:</p>
<pre>
pip install requests
pip install lxml
pip install beautifulsoup4
</pre>
El script principal se debe ejecutar de la siguiente forma:
<pre>
python scraper.py
</pre>
<p>Los campos que extraemos son:</p>
<ul>
          <li>País</li>
          <li>Equipo de Fútbol</li>
          <li>Partidos Jugados</li>
          <li>Partidos ganados en casa</li>
          <li>Partidos empatados en casa</li>
          <li>Partidos perdiods en casa</li>
          <li>Partidos ganados fuera</li>
          <li>Partidos empatados fuera</li>
          <li>Partidos perdidos fuera</li>
          <li>Partidos totales ganados</li>
          <li>Partidos totales empatados</li>
          <li>Partidos totales perdidos</li>
          <li>Puntos obtenidos</li>
          <li>Posición en la clasificación</li>
</ul>          
<h3>1. Explicar en qué contexto se ha recolectado la información. Explique porque el sitio web elegido proporciona dicha información.</h3>

El máximo organismo europeo a nivel futbolístico es la UEFA (Unión de Asociaciones Europeas de Fútbol) y esta se encarga de organizar los distintos campeonatos que se puedan realizar en Europa, así como promover, desarrollar y controlar cualquier aspecto a nivel de dicho deporte.

Cualquier site a parte de tener una interfaz amigable, una navegación fácil e intuitiva, un buen diseño… debe tener un contenido de calidad. Esto último implica que la información que se facilite debe estar destinada al usuario, aportándoles valor y que puedan profundizar sobre el tema. Y lo más importante, que sean veraces. 

La UEFA consigue trasladar estas características en su página oficial; donde podemos encontrar un apartado de noticias, las distintas competiciones que organiza con sus correspondientes resultados, las clasificaciones, videos resúmenes y un largo etcétera, todo ello relacionado con la actividad que desarrollan. De esta forma consiguen trasladar al usuario toda su actividad.

En la práctica que nos atañe, hemos trabajado en el apartado relacionado con los miembros de dicha asociación. Donde por un lado se puede ver el resumen de las principales ligas y en la parte derecha, el enlace a todas las ligas que forman parte del organismo. 

Este último apartado  es donde se ha focalizado la recolección de datos, de los que se han creado los distintos códigos para tener una clasificación por países y dentro de cada uno de ellos, los equipos que lo forman. Para cada uno de los equipos se ha recopilado la información relacionada a la liga que pertenece, obteniendo así la posición en la clasificación, los partidos jugados, los puntos, etc.


<h3>Definir un titulo para el dataset. Elegir un titulo que sea descriptivo.</h3>

Clasificación actualizada de equipos de fútbol profesional en las ligas europeas
 
<h3>Descripción del dataset. Desarrollar una descripción breve del conjunto de datos que se ha extraído (es necesario que esta descripción tenga sentido con el título elegido).</h3>

Un dataset es un una colección de datos, normalmente tabulada. En este caso el conjunto de datos procede de la página oficial del mayor organismo futbolístico a nivel europeo. 

La información que pública la UEFA corresponde, entre otra, a todas las ligas con sus correspondientes clasificaciones de los equipos según los partidos que han jugado.

Los datos extraídos corresponden precisamente a todos los equipos de estas ligas europeas con los puntos, posiciones, partidos… de cada uno de ellos. De ahí que se haya escogido el nombre anteriormente mencionado: Clasificación actualizada de equipos de fútbol profesional en las ligas europeas.


<h3>Representación grafica. Presentar una imagen o esquema que identifique el dataset visualmente.</h3>

 

<h3>Contenido. Explicar los campos que incluye el dataset, el periodo de tiempo de los datos y como se ha recogido.</h3>

Para la creación del dataset, se ha accedido a la web de trabajo y se ha descargado mediante la librería BeautifulSoup. Para cada link que encontramos, se guarda el link que será el que va a contener la información por países. 

Por países vamos obteniendo de forma iterativa los equipos que componen dicho país con los correspondientes datos de la clasificación. Por cada equipo obtenido, se guarda la información en un vector que contendrá todos los atributos y que posteriormente, una vez recopilados en su totalidad [los equipos] los guardaremos en el csv.

Dado que los partidos se disputan semanalmente, el periodo del tiempo de datos normal sería entre 7 y 10 días. Pero se podría dar una situación excepcional que esta semana no se disputara la competición por cualquier razón, por ejemplo, elecciones, huelga… con lo que estableceríamos un periodo de 15-20 días.

El dataset incluye los siguientes campos:

Variable	Descripción
countryName	País al cual pertenece el equipo
teamName	Nombre del equipo de fútbol
gamesPlayed	partidos jugados
wHome	partidos ganados en casa
dHome	partidos empatados en casa
lHome	partidos perdidos en casa
wAway	partidos ganados fuera de casa
dAway	partidos empatados fuera de casa
lAway	partidos perdidos fuera de casa
wTotal	partidos totales ganados
dTotal	partidos totales empatados
lTotal	partidos totales perdidos
points	total de puntos obtenidos
position	posición en la clasificación

<h3>Agradecimientos. Presentar al propietario del conjunto de datos. Es necesario incluir citas de investigación o análisis anteriores (si los hay).</h3>

La UEFA (Unión de Federaciones Europeas de Fútbol), es la confederación europea de asociaciones nacionales de fútbol y máximo organismo de este deporte en el continente europeo. Agrupa a todas las federaciones nacionales a lo largo de toda Europa.

Fue fundada en 1954 y es la encargada de organizar los campeonatos nacionales de Europa, la Eurocopa masculina y femenina, la Liga de Campeones masculina y femenina y la Europa League.

Sus objetivos principales, además de organizar los principales campeonatos de Europa, son: promover el fútbol en espíritu de unidad, solidaridad, paz, comprensión y juego limpio sin ningún tipo de discriminación y apoyar y salvaguardar a las federaciones por el bienestar general de fútbol europeo.

Hemos realizado un análisis del fichero robots.txt ubicado en https://es.uefa.com/robots.txt ya que en este fichero se indican las restricciones que deberíamos tener en cuenta cuando realizamos un rastreado y hemos comprobado que nuestro directorio https://es.uefa.com/memberassociations no está restringido y por lo tanto, es apto para poder ser rastreado a través de una herramienta como la que hemos desarrollado.

Existen diversas webs que resumen las clasificaciones de las principales ligas europeas como son: Alemania, España, Italia, Inglaterra, Francia, Holanda, pero no hemos encontrado ninguna que informe de las clasificaciones de todos los países europeos que están asociados a la UEFA.
Las webs que hemos encontrado que muestran la clasificación de las principales ligas europeas son:
-	https://www.mismarcadores.com
-	https://www.superdeporte.es/deportes/futbol/
-	https://www.scoreboard.com/es/futbol/
 
<h3>Inspiración. Explique por qué es interesante este conjunto de datos y qué preguntas se pretenden responder.</h3>

El fútbol es el deporte más popular no solo del continente europeo sino del mundo, se estima que tiene más de 4 mil millones de seguidores, alcanzando cifras del 60% de la población total. 
Por ello, consideramos que la extracción de cualquier tipo de información de fuentes oficiales asociadas al fútbol y generación de datos listos para ser analizados por distintas plataformas, webs, prensa, aplicaciones móviles, etc., puede llegar a tener una repercusión muy importante teniendo en cuenta la cantidad de usuarios finales a quienes les puede llegar la información a través de diferentes medios.

Las preguntas que se pretenden responder son:
-	¿Qué liga europea de fútbol es la más competida y complicada de ganar? ¿Y la más fácil?
-	¿Qué liga europea de fútbol tiene más goles de media? 
-	¿Qué país tiene la liga de fútbol con más equipos en primera división? ¿Y el que menos?
-	¿Qué equipo / equipos de fútbol europeo son los más goleadores? ¿Y los menos goleados?
-	¿Qué equipos son los mejores en casa a nivel de cada país y también a nivel de toda Europa?
-	¿Qué equipos son los mejores fuera de casa a nivel de cada país y también a nivel de toda Europa?
-	¿Hay equipos invictos (que no han perdido aún) en Europa?
-	A final de temporada, se puede realizar un comparativo entre todas las ligas y poder responder: 
o	Qué equipo de Europa ha obtenido la mejor puntuación, el más goleador y el menos goleado? ¿Cuántos puntos hacen falta de media para ser campeón en cada país europeo?
-	Debido a la situación actual por la pandemia del COVID-19:
o	¿Qué ligas se pueden dar por finalizadas, según la diferencia de puntos entre los primeros clasificados?
o	¿Cuántas jornadas faltan para dar por terminadas las ligas europeas de fútbol por países?

<h3>Licencia.   Seleccione   una   de estas licencias   para   su   dataset   y   explique   el motivo de su selección:</h3>

Consideramos que nuestro dataset debería tener una licencia del tipo Released Under CC BY-NC-SA 4.0 License. La elección de esta licencia se basa en:
-	Cualquier persona o empresa que la utilice deberá reconocer la autoría de quienes construyeron el dataset y también indicar si realizaron cambios o no en el mismo. De esta forma se nos reconocerá nuestro trabajo.
-	No permitimos el uso comercial, ya que, no nos gustaría que otras empresas obtengan beneficios económicos a costa de nuestro trabajo.
-	Los nuevos desarrollos o adaptaciones realizadas sobre nuestro dataset, deberá difundir nuestras contribuciones de la misma forma que la licencia original, de tal forma, que se seguirá reconociendo nuestra autoría, después de cualquier actualización.

Teniendo en cuenta que, de todos los tipos de licencias proporcionados en el enunciado, la única que se ajusta a nuestro modo de trabajo y reconocimiento seleccionamos Released Under CC BY-NC-SA 4.0 License.

<h3>Código. Adjuntar el código con el que se ha generado el dataset, preferiblemente en Python o, alternativamente, en R.</h3>

El código fue desarrollado en Python utilizando el Entorno de Desarrollo Integrado (IDE) Wing Personal 7.2, el código fuente se encuentra en el fichero comprimido código.zip y también en el repositorio de github: 	https://github.com/aaldaveva/web-scraping

