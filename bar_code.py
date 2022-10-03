import get_csv


def print_barcode(items):
    import barcode
    for item in items:
        barcode.generate('ean13', item['barcode'], None, item['article'], None, item['country'])