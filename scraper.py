from scraperCountries import scraperCountries

#Las url desde donde se descargara la informacion
urlMain = "https://es.uefa.com/memberassociations/leaguesandcups/index.html"
urlBaseCountry ="https://es.uefa.com"
sc = scraperCountries(urlMain,urlBaseCountry)
sc.execute()
