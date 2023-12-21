import json
import urllib.parse
import urllib.request

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter location: ')

parms = dict()
parms['address'], parms['key'] = address, api_key

url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)

data = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters')
js = json.loads(data)
print(js['results'][0]['place_id'])
