import requests
import pandas as pd
import yaml

# test de selenium
# from selenium import webdriver

# on ouvre le ficier headers.yml et on met en en-tête les headers Chrome
with open("headers.yml") as f_headers:
    browser_headers = yaml.safe_load(f_headers)
browser_headers["Chrome"]

# le temps max que la connexion se fasse
TIMEOUT_IN_SECONDS = 0.2

# une liste de nos proxies
proxy_list = {
    'http' : "http://77.86.32.251:8080",
}

# on prend une liste de proxies qui fonctionnent et gratuit 
response = requests.get("https://free-proxy-list.net/")
proxy_list = pd.read_html(response.text)[0]

# on split les urls 
proxy_list['url'] = "http://" + proxy_list["IP Address"] + ":" + proxy_list["Port"].astype(str)

# on prend les 5 premiers proxies du site
proxy_list.head()

# on ne prendra que les proxies pouvant supporter le HTTPS
https_proxies = proxy_list[proxy_list["Https"] == "yes"]
# on les comptes 
https_proxies.count()
print(https_proxies.count())



url = "https://httpbin.org/ip"
good_proxies = set()
headers = browser_headers["Firefox"]
for proxy_url in https_proxies["url"]:
    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }
    
    try:
        response = requests.get(url, headers=headers, proxies=proxies, timeout=2)
        good_proxies.add(proxy_url)
        # print(f"Proxy {proxy_url} OK, added to good_proxy list")
    except Exception:
        pass
    
    if len(good_proxies) >= 3:
        break


# test avec Selenium
# for proxy_url in good_proxies:
#     proxy = proxy_url.replace("http://", "")

#     firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
#     firefox_capabilities['marionette'] = True

#     firefox_capabilities['proxy'] = {
#         "proxyType": "MANUAL",
#         "httpProxy": proxy,
#         "sslProxy": proxy
#     }

#     driver = webdriver.Firefox(capabilities=firefox_capabilities)
#     try:
#         driver.get("https://httpbin.org/ip")
#     except Exception:
#         pass