import csv

with open('personnes.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["email"])

rows = []
for i in range(200):
    rows.append({
        "id" : i,
        "category" : "Generated",
        "link" : "https://to.the.past"
    })

headers = ['id', "category", "link"]

with open('linkList.csv', "w", newline='' ) as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)