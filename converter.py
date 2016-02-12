#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import requests


class CurrencyConverter(object):

    url = ('https://currency-api.appspot.com/api/%s/%s.json') % ('PLN', 'SEK')

    def __init__(self):
        r = requests.get(self.url)
        self.rate = r.json()['rate']
        print(self.rate)

    def convert(self, amount=1):
        return round(amount*float(self.rate), 2)


