import urllib.request
import json

url = input('Enter location: ')
print('Retrieving', url)
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')
tree = json.loads(data)
counts = tree['comments']
sums = 0
for num in counts:
    sums += int(num['count'])
print(sums)
