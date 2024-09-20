from pathlib import Path
from typing import Iterable
''' Esta libreria proporciona clases para
trabajar con sistemas de archivos y rutas de archivos de una
manera mas intuitiva'''

import scrapy

class QuotesSpider(scrapy.Spider):
# nuestra subclase Spider "scrapy.Spider"
# y definen algunos atributos y metodos:

    name="quotes"
    #Identificar al Spider (unico dentro de un proyecto)



    def start_requests(self):
        # debe devolver un iterable de solicitudes 
        # desde la que el Spider comenzara a rastrear.
        # Las solicitudes posteriores se generaran sucesivamente
        # a partir de estas solicitudes iniciales
        urls=[
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",

        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self,response):
       # Un metodo que se llamará para gestionar la respuesta descargada
       # para cada una de las solicitudes realizadas.
       # El parametro de respuesta es una instancia de "TextResponse"
       # que contiene el contenido de la pagina y tiene otros metodos utiles para gestionarlo
        page=response.url.split("/")[-2]
        filename=f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")







