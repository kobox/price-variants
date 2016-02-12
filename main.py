#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# __author__ = 'ko'
#from __future__ import unicode_literals
import itertools
from operator import itemgetter, attrgetter, methodcaller
import csv, io
from converter import CurrencyConverter

data = ('Name', 'Zadruk', 'Laminowanie', 'Mechanizm', 'Wielobig', 'Kó?ko grzbietowe', 'Kieszonki (wklejane)', 'Quantity', 'Product quantity limit', 'Price', 'Additional days')
exclude = [(), ]
prices_file = io.open('tutorial.csv', 'w', encoding='utf-8')
mywriter = csv.writer(prices_file, delimiter=';',)
mywriter.writerow(data)
quantity = (1, 10, 20, 50, 75, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000, 10000)
line = []
properties = [[[('CMYK-tryck 4/0', 199), ('CMYK-tryck 4/4', 201)], [('Glättad folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)], [('STR16/04/152', -0.15), ('STR23/04/152', -0.10), ('STR30/04/152', 0), ('STR38/04/152', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK-tryck 4/0', 49), ('CMYK-tryck 4/4', 51)], [('Glättad folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16/04/152', -0.15), ('STR23/04/152', -0.15), ('STR30/04/152', 0), ('STR38/04/152', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK-tryck 4/0', 30), ('CMYK-tryck 4/4', 32)], [('Glättad folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16/04/152', -0.15), ('STR23/04/152', -0.15), ('STR30/04/152', 0), ('STR38/04/152', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK-tryck 4/0', 20), ('CMYK-tryck 4/4', 22)], [('Glättad folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16/04/152', -0.15), ('STR23/04/152', -0.15), ('STR30/04/152', 0), ('STR38/04/152', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK-tryck 4/0', 17), ('CMYK-tryck 4/4', 19)], [('Glättad folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16/04/152', -0.15), ('STR23/04/152', -0.15), ('STR30/04/152', 0), ('STR38/04/152', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK-tryck 4/0', 15), ('CMYK-tryck 4/4', 17)], [('Glättad folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16/04/152', -0.15), ('STR23/04/152', -0.15), ('STR30/04/152', 0), ('STR38/04/152', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK-tryck 4/0', 14), ('CMYK-tryck 4/4', 15)], [('Glättad folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16/04/152', -0.15), ('STR23/04/152', -0.15), ('STR30/04/152', 0), ('STR38/04/152', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK-tryck 4/0', 13.50), ('CMYK-tryck 4/4', 14.50)], [('Glättad folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16/04/152', -0.15), ('STR23/04/152', -0.15), ('STR30/04/152', 0), ('STR38/04/152', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK-tryck 4/0', 13), ('CMYK-tryck 4/4', 14)], [('Glättad folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16/04/152', -0.15), ('STR23/04/152', -0.15), ('STR30/04/152', 0), ('STR38/04/152', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK-tryck 4/0', 12), ('CMYK-tryck 4/4', 13)], [('Glättad folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16/04/152', -0.15), ('STR23/04/152', -0.15), ('STR30/04/152', 0), ('STR38/04/152', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK-tryck 4/0', 10.50), ('CMYK-tryck 4/4', 11.50)], [('Glättad folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16/04/152', -0.15), ('STR23/04/152', -0.15), ('STR30/04/152', 0), ('STR38/04/152', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK-tryck 4/0', 9.50), ('CMYK-tryck 4/4', 10.50)], [('Glättad folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16/04/152', -0.15), ('STR23/04/152', -0.15), ('STR30/04/152', 0), ('STR38/04/152', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK-tryck 4/0', 8.80), ('CMYK-tryck 4/4', 9.80)], [('Glättad folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16/04/152', -0.15), ('STR23/04/152', -0.15), ('STR30/04/152', 0), ('STR38/04/152', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK-tryck 4/0', 8.60), ('CMYK-tryck 4/4', 9.60)], [('Glättad folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16/04/152', -0.15), ('STR23/04/152', -0.15), ('STR30/04/152', 0), ('STR38/04/152', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK-tryck 4/0', 8.40), ('CMYK-tryck 4/4', 9.40)], [('Glättad folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16/04/152', -0.15), ('STR23/04/152', -0.15), ('STR30/04/152', 0), ('STR38/04/152', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK-tryck 4/0', 8.20), ('CMYK-tryck 4/4', 9.20)], [('Glättad folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16/04/152', -0.15), ('STR23/04/152', -0.15), ('STR30/04/152', 0), ('STR38/04/152', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK-tryck 4/0', 8), ('CMYK-tryck 4/4', 9)], [('Glättad folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16/04/152', -0.15), ('STR23/04/152', -0.15), ('STR30/04/152', 0), ('STR38/04/152', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]]]

converter = CurrencyConverter()

for v in range(len(properties)):
    for lista in itertools.product(*properties[v]):
        x2, y2 = zip(*lista)
        z1, z2, z3, z4, z5, z6 = x2
        line.append(('Reklampärmar', z1, z2, z3, z4, z5, z6, quantity[v], quantity[v+1]-1, converter.convert(round(sum(j for i, j in lista), 2)), 0))

line = sorted(line, key=itemgetter(1, 2, 3, 4, 5, 6, 7))
for i in range(len(line)):
    print(line[i])
    mywriter.writerow(line[i])

prices_file.close()
