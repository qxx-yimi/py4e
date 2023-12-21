import urllib.request
import xml.etree.ElementTree as ET

sums = 0
url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
counts = tree.findall('.//count')
for num in counts:
    sums += int(num.text)
print(sums)
