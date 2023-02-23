import Studyrama
import Scrapper
import requests 
import csv 
from bs4 import BeautifulSoup

# L'url du site que je souhaite Scraper
baseUrl = 'https://www.stage.fr/'
uri = "jobs/?q=stage%20Cybersecurité&p="

# instanciation des classes 
studyrama = Studyrama(baseUrl, uri, 1)
scrapper = Scrapper(studyrama, "linksList.csv", "infos.csv")

