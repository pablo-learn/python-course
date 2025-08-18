import csv

field_names = ['name', 'price', 'quantity', 'total_value']

#Leer un archivo
with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    with open('products_updated.csv', mode='w') as file:
        csv_writer = csv.DictWriter(file, fieldnames=field_names)
        csv_writer.writeheader()
        for row in csv_reader:
            csv_writer.writerow(
                {
                    'name': row['name'],
                    'price': row['price'],
                    'quantity': row['quantity'],
                    'total_value': float(row['price']) * float(row['quantity'])
                }
            )
