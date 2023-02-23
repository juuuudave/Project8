import csv

# Liste de données
liste = [
    ['1', 'John', 'Doe', 'john.doe@email.com'],
    ['2', 'Jane', 'Doe', 'jane.doe@email.com'],
    ['3', 'Bob', 'Smith', 'bob.smith@email.com']
]

# Header
header = ['ID', 'First Name', 'Last Name', 'Email']

# Ouverture du fichier en mode écriture
with open('fichier.csv', 'w', newline='') as f:
    # Création de l'objet writer
    writer = csv.writer(f)
    
    # Écriture du header
    writer.writerow(header)
    
    # Écriture des lignes de données
    writer.writerows(liste)