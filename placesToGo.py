import requests
import json

lon=139
lat=35
units = 'auto'

url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
  client_id='[redacted]',
  client_secret='[redacted]',
  v='20180323',
  ll='36.116089,-96.697670',
  section='food',
  limit=3,
  radius = 1000
)
response = requests.get(url=url, params=params)
data = json.loads(response.text)

name = [0, 0, 0,];
hereNow = [0, 0, 0];
address = [0, 0, 0];
#to get top 3 restaurants
if(response.ok):
    jData = json.loads(response.content)
    #print("Places to eat")
    for i in range(0,3):
      name[i] = (jData['response']['groups'][0]['items'][i]['venue']['name'])
      hereNow[i] = (jData['response']['groups'][0]['items'][i]['venue']['hereNow']['summary'])
      address[i] = (jData['response']['groups'][0]['items'][i]['venue']['location']['formattedAddress'][0])
      print(name[i])

else:
     response.raise_for_status()


url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
  client_id='[redacted]',
  client_secret='[redacted]',
  v='20180323',
  ll='36.116089,-96.697670',
  section='sights',
  limit=3
)
response = requests.get(url=url, params=params)
data = json.loads(response.text)
#to get top 3 sights in the area
if(response.ok):
    jData = json.loads(response.content)
    #print("Places to checkout")
    for i in range(0,3):
      name[i] = (jData['response']['groups'][0]['items'][i]['venue']['name'])
      hereNow[i] = (jData['response']['groups'][0]['items'][i]['venue']['hereNow']['summary'])
      address[i] = (jData['response']['groups'][0]['items'][i]['venue']['location']['formattedAddress'][0])
      print(name[i])

else:
     response.raise_for_status()
