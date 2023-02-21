# import des librairies dont nous aurons besoin
import pandas as pd
import numpy as np
import re

# chargement et affichage des données
data = pd.read_csv('linklist.csv')
print(data.isnull().sum())

data['id'] = id
data['category'] = category
data['link'] = link