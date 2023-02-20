import yaml
import time
import requests 
import csv 
from bs4 import BeautifulSoup 

# on ouvre le fichier contenant tous les headers
with open("headers.yml") as f_headers:
    browser_headers = yaml.safe_load(f_headers)
browser_headers["Firefox"]

# L'url du site que je souhaite Scraper
baseUrl = 'https://www.stage.fr/'
uri = "jobs/?q=stage%20Cybersecurité&p="


#Genere des liens avec l'argument "page" qui s'incrémente
def getLinks(url, nbPg):
    # initialisation du resultat (vide pour l'instant)
    urls = []
    # Pour chaque page
    for i in range(nbPg):
        # Ajoutes la concatenation de l'url avec l'index au tableau d'urls
        urls.append(url + str(i))
    return urls

def swoup(url, process):
    # Instanciation de mon proxy
    response = requests.get(url)
    # si mon site renvoie un code HTTP 200 (OK)
    if response.ok:
        # je parse le contenue html de ma page 
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            # Je retourne l'execution de ma fonction process prenant ma SWOUP SWOUP en paramètre
            return process(soup)
            
        except Exception:
            print("ERROR: Impossible to process ! " )
    
    else:
        print("ERROR: Failed Connect")
    return


# Fonction qui permet de "crawler" sur le site et recuperer tous les liens sur la page visée
def getEndpoints(soup):
    div = soup.find('div', { "class": "widgets__container"})
    section_div = div.find('div', { "class": "section"})
    articles = section_div.findAll('article')
    # on créer un tableau vide pour contenir tous nos liens du crawling
    links = []
    for article in articles:
        a = article.find('a')
        try: 
            links.append(a['href'])
        except:
            print(article)
            print('ERROR: No link')
    return links


# On concatène les liens à l'url
def addBaseUrl(baseUrl, urls):
    # on fait un tableau vide des résultats 
    res = []
    for url in urls or []:
        res.append(url)
    return res


# Fonction qui permet de "scrapper" sur le site et récuperer tous les information sur les pages visées
def getInformations(soup):
    div = soup.find('div', {"class": "container"})
    # pour le titre du stage
    title_stages = div.find('h1', {"class": "details-header__title"})
    if title_stages is not None:
        tabs = title_stages.findAll("li", {"class": "accordeon-item"}) # ex du prof
        if tabs is not None:
            for tab in tabs: 
                # print(tab)
                name = tab.find('div', {"class": "accordeon-header"})
                # print(name.getText)
                coord = tab.find('div', {"class": "accordeon-body"})
                adress = coord.find("p")

                try:
                    adress = adress.getText()
                    cleanAdress = []
                    for ele in str(adress).split("\n"):
                        if ele.strip() is not "":
                            cleanAdress = adress
                except: 
                    # mettre les variables vide comme ceci 'adress' : ""

                fiche = {
                    "title" : title.replace("mettre ce qu'il faut", ""),
                    "parution_date" : date_parution,
                    "adress" : adress,
                    "number" : number
                }
                fiche.append()
                return fiche
                
    print("VOICI LE TITRE DU STAGE",title_stages)
    exit()

def tryToCleanOrReturnBlank:


# On fait un tableau vide de toutes les urls
urls = []
for link in getLinks(baseUrl + uri, 1):
    print("Checking " + link)
    urls.extend(addBaseUrl(baseUrl, swoup(link, getEndpoints)))
    for url_link in urls:    
        # On affiche les liens 
        print("Voici les liens des stages :",url_link)
        # récupération des informations
        # On vérifie si on peut se connecter à la page 
        swoup(url_link, getInformations)




        # Les titres de nos informations
        # headers = ['id', "category", "link"]
        
        # rows = []
        # with open('linkList.csv', "w", newline='' ) as file: 
        #     writer = csv.DictWriter(file, fieldnames=headers)
        #     writer.writeheader()
        #     for row in rows: 
        #         writer.writerow(row)
        
        
        # for i in range(urls): 
        #     rows.append({
        #         "id" : i,
        #         "category" : "None",
        #         "link" : urls[i]
        #     })
