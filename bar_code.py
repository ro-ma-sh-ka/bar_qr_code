def print_barcode(items, barcode_type='ean13', folder_to_save=None):
    import barcode
    for item in items:
        file_to_save = str(folder_to_save) + '/' + item['article']
        text = f"Art: {item['article']}\\n adress: {item['country']}, {item['adress']}, warranty: {item['warranty']}"
        barcode.generate(barcode_type, item['barcode'], None, file_to_save, None, text)