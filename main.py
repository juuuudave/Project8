import yaml
import time
import requests 
import csv 
from bs4 import BeautifulSoup 

# import proxies 

# L'url du site que je souhaite Scraper
baseUrl = 'https://www.stage.fr/'
uri = "jobs/?q=stage%20cybersécurité&p="


#Génère des liens avec l'argument "page" qui s'incrémente
def getLinks(url, nbPg=0):
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
            # impossible d'aller à la page demandée
            print("ERROR: Impossible to process ! ")
    
    else:
        print("ERROR: Failed Connect")
        pass
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


def getInformations(soup):
    # Fonction qui permet de "scrapper" sur le site et récupérer tous les information sur les pages visées
    # pour le titre du stage
    title_stages = soup.find('h1', {"class": "details-header__title"})
    title = title_stages.getText()
    # print(title)
    
    # on vérifie si les informations ne sont pas vide
    if title is not None:
        fiches = []
        ul = soup.find("ul", {"class": "clearfix"}) # ex du prof
        if ul is not None:
            name = ul.find("li", {"class": "listing-item__info--item-company"}).getText()
            if name is not None:
                address = ul.find("li", {"class": "listing-item__info--item-location"}).getText()
                if address is not None:
                    date = ul.find("li", {"class": "listing-item__info--item-date"}).getText()
                    
                    # création d'une list ayant toutes les informations de la page
                    fiche = { 
                        "title": title, 
                        "parution_date": date,
                        "address": address,
                        "name":name,
                        }
                    fiches.extend(fiche)
                    

    return fiche


# fonction pour lire un fichier
def fileReader(file):
    result = []
    with open(file, 'r', encoding="UTF8", newline="") as f:
        reader = csv.DictReader(f)
        for line in reader:
           result.append(line) 
    return result

# fonction pour écrire dans un fichier
def fileWriter(file, fieldnames, data):
    with open(file, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print("l'url à été écrite")
    

# fonction pour clean les infos erronés
def tryToCleanOrReturnBlank(str):
    try:
        result = str.getText().strip()
    except:
        result = ''
    return result


# On fait un tableau vide de toutes les urls
urls = []
for link in getLinks(baseUrl + uri, 1):
    print("Checking " + link)

    # on ajoute les urls dans le tableau
    urls.extend(addBaseUrl(baseUrl, swoup(link, getEndpoints)))

for url_link in urls:
    rows = []
    for i in range(len(urls)):
        rows.append({
            "id": i,
            "category":" liens ",
            "link": urls[i]
        })
        
    # catégorie du fichier 
    headers = ["id", "category", "link"]
    
    # On ouver le fichier et on écrit les endpoints dedans 
    with open('linkListStage.csv', "w", encoding='UTF8' ,newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    # On affiche les liens
    print("Voici les liens des stages :", url_link)

    # Récupération des informations
    # On vérifie si on peut se connecter à la page 
    swoup(url_link, getInformations)

    lignes = []
    
    for link in fileReader('linkListStage.csv'):
        lignes.extend(swoup(url_link, getInformations))

    # en-tête du fichier
    headers_infos = ["title", "name", "address", "date"]
    # on écrit dans le fichier .csv
    fileWriter('infoPages.csv', headers_infos, lignes)
