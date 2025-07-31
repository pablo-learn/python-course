import csv

with open('products_updated.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
