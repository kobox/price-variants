import requests

a = raw_input('Enter currency to convert from?')
a = a.upper()

b = raw_input('Enter currency to convert to?')
b = b.upper()

c = float(raw_input('Enter value to convert?'))

url = ('https://currency-api.appspot.com/api/%s/%s.json') % (a, b)
print(url)

r = requests.get(url)
print(r.json()['rate'])

print(c*float(r.json()['rate']))

urlalt = ('http://themoneyconverter.com/%s/%s.aspx') % (a, b)
print(urlalt)

#split and strip
split1 = ('>%s/%s =') % (b, a)
strip1 = ('</textarea>')

ralt = requests.get(urlalt)
d = float(ralt.text.split(split1)[1].split(strip1)[0].strip())
print(d)

print(c * d)