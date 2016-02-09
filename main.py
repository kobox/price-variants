#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# __author__ = 'ko'
#from __future__ import unicode_literals
import itertools
from operator import itemgetter, attrgetter, methodcaller

quantity = (1, 10, 20, 50, 75, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000)
line = []
properties = [[[('CMYK tryck 4/0', 199), ('CMYK tryck 4/4', 201)], [('Gotäld folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)], [('STR16', -0.15), ('STR23', -0.10), ('STR30', 0), ('STR38', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK tryck 4/0', 49), ('CMYK tryck 4/4', 51)], [('Gotäld folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16', -0.15), ('STR23', -0.15), ('STR30', 0), ('STR38', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]],
              [[('CMYK tryck 4/0', 30), ('CMYK tryck 4/4', 32)], [('Gotäld folie', 0), ('Matt folie', 0.20), ('Repsäker matt folie', 2), ('Folie med linstruktur', 3)],
              [('STR16', -0.15), ('STR23', -0.15), ('STR30', 0), ('STR38', 0.35)], [('Ja', 0.2), ('Nej', 0)],
              [('Ja', 0.35), ('Nej', 0)], [('Icke', 0), ('Ficka för visitkort', 0.4), ('Trekantig ficka', 0.5), ('Ryggficka', 0.4)]]]

for v in range(len(properties)):
    for lista in itertools.product(*properties[v]):
        x2, y2 = zip(*lista)
        line.append((x2, quantity[v], quantity[v+1]-1, sum(j for i, j in lista)))

line = sorted(line, key=lambda x: x[0])
for i in range(len(line)):
    print line[i]
