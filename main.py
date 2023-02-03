# ensure you have Python (3  or latest)
# ensure you have pip installer
import requests 
from bs4 import BeautifulSoup 
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


#fonction qui permet de "crawler" sur mon site et recuperer tous les liens sur la page visée
def getEndpoints(soup):
    div = soup.find('div', { "class": "widgets__container"})
    section_div = div.find('div', { "class": "section"})
    articles = section_div.findAll('article')
    links = []
    for article in articles:
        a = article.find('a')
        try: 
            links.append(a['href'])
        except:
            print(article)
            print('ERROR: No link')
    return links

def swoup(url, process):
    #Instanciation de mon proxy
    response = requests.get(url)
    #si mon site renvoie un code HTTP 200 (OK)
    if response.ok:
        #je passe le contenue html de ma page dans un "parser"
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            #Je retourne l'execution de ma fonction process prenan ma SWOUP SWOUP en paramètre
            return process(soup)
        except Exception:
            print("ERROR: Impossible to process ! " )
    else:
        print("ERROR: Failed Connect")
        # print(response)
    return 

#concatene mes liens a l'url
def addBaseUrl(baseUrl, urls):
    res = []
    for url in urls:
        res.append(url)
    return res


#Execution
urls = []
for link in getLinks(baseUrl + uri, 1):
    print("Checking " + link)
    urls.extend(addBaseUrl(baseUrl, swoup(link, getEndpoints)))
    for url_link in urls:    
        print("Voici les liens des stages :",url_link)

def get_info(url_link)
    