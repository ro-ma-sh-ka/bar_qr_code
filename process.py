import csv
import barcode
from typing import NoReturn


def get_csv(filename='ean13_1.csv') -> list:
    """recieves CSV filename and return list of dictionaries with items and their attributes"""
    with open(filename, newline='', encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        items = []
        for row in reader:
            items.append(row)
    return items


def print_barcode(items, barcode_type='ean13', folder_to_save=None) -> NoReturn:
    """recieves list of items from get_csv function, type of barcode and destination folder to save images"""
    for item in items:
        file_to_save = str(folder_to_save) + '/' + item['article']
        text = f"Art: {item['article']}, Info: {item['information']}"
        barcode.generate(barcode_type, item['barcode'], None, file_to_save, None, text)
