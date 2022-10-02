import get_csv

items = get_csv.get_csv()
def print_barcode():
    import barcode
    for item in items:
        barcode.generate('ean13', item['barcode'], None, item['article'], None, item['country'])