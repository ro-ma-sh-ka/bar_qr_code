
import csv


with open('ean13_1.csv', newline='', encoding='UTF-8') as csvfile:
    reader = list(csv.reader(csvfile, delimiter=';'))

    for row in reader:
        print(row)

if __name__ == "__main__":
    print('hello')