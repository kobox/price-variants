#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv, io


def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

prices_file = io.open('tutorial.csv', 'w', encoding='utf-8')

mywriter = csv.writer(prices_file, delimiter=';',)

# create an object called data that holds the records.

data = [
('Name', 'Zadruk', 'Laminowanie', 'Mechanizm', 'Wielobig', 'Kółko grzbietowe', 'Kieszonki (wklejane)', 'Quantity', 'Product quantity limit', 'Price', 'Additional days')
]
#data = utf_8_encoder(data)
for item in data:
    mywriter.writerow(item)

#spamwriter = csv.writer(prices_file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
# always make sure that you close the file.
# to ensure the data is saved.

prices_file.close()
