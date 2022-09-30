import qrcode, PIL, barcode

img = qrcode.make('https://gelta.ru/')
img.save('gelta.png')

ean = barcode.get_barcode_class('ean13')
ean2 = ean('123456789123')
ean2.save('ean_test2')

