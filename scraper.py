from scraperCountries import scraperCountries

urlMain = "https://es.uefa.com/memberassociations/leaguesandcups/index.html"
urlBaseCountry ="https://es.uefa.com"
sc = scraperCountries(urlMain,urlBaseCountry)
sc.execute()
