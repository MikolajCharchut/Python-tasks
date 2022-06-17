import requests
import sys

#page_url = 'https://api.discogs.com/artists/359282' #Budka Suflera
#page_url = 'https://api.discogs.com/artists/56168' #Queens Of The Stone Age

try:
    id = int(input('Podaj id zespołu: '))
except:
    print('Złe id zespołu')

page_url = 'https://api.discogs.com/artists/' + str(id)

page = requests.get(page_url)

if page.status_code != 200:
    print("Bad server status")
    sys.exit(1)

membersList = page.json()['members']

names = {}

for i in membersList:
    bands = []
    getBand = requests.get(i['resource_url'])
    try:
        for j in getBand.json()['groups']:
            bands.append(j['name'])
        names[i['name']] = bands
    except: pass

result = {}
bands = []

for i in names:
    for j in names[i]:
        bands.append(j)

bands = set(bands)
bands = list(bands)

for i in bands:
    result[i] = []

for i in names:
    for j in names[i]:
        if j in bands:
            result[j].append(i)

for i in sorted(result):
    if len(result[i]) >= 2:
        print('Zespół:', i, '|| Członkowie:', result[i])

sys.exit(0)
