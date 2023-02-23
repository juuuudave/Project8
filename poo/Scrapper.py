import requests 
import csv 
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self, scrapInstance, linkFile, finalFile):
        self.setScrapInstance(scrapInstance)
        self.setLinkFile(linkFile)
        self.setFcrapInstance(finalFile)

    # mettre les setter 
