#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import requests


class CurrencyConverter(object):

    url = ('https://currency-api.appspot.com/api/%s/%s.json') % ('PLN', 'SEK')

    def __init__(self, default=False):
        r = requests.get(self.url)
        if not default:
            self.rate = r.json()['rate']
        else:
            self.rate = 2.145
        print(self.rate)

    def convert(self, amount=1):
        return round(amount*float(self.rate), 2)


