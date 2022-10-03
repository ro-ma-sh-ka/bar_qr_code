def get_csv(filename='ean13_1.csv'):
    import csv

    with open(filename, newline='', encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        items = []
        for row in reader:
            items.append(row)
    return items
