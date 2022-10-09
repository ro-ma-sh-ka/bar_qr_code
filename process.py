import csv
import barcode

def get_csv(filename='ean13_1.csv'):
    with open(filename, newline='', encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        items = []
        for row in reader:
            items.append(row)
    return items

def print_barcode(items, barcode_type='ean13', folder_to_save=None):
    for item in items:
        file_to_save = str(folder_to_save) + '/' + item['article']
        text = f"Art: {item['article']}\\n adress: {item['country']}, {item['adress']}, warranty: {item['warranty']}"
        barcode.generate(barcode_type, item['barcode'], None, file_to_save, None, text)