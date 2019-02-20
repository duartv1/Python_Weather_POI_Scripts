import requests
import json

lon=139
lat=35
units = 'auto'

token='[redacted]'
url='https://api.darksky.net/forecast/'+token+'/'+str(lat)+','+str(lon)

#https://api.darksky.net/forecast/[key]/[latitude],[longitude]
#https://dev-sandbox-api.airhob.com/sandboxapi/flights/v1.3/search
response=requests.get(url, units)

if(response.ok):
    jData = json.loads(response.content)
    print(jData['daily']['data'][0]['summary'])

else:
     response.raise_for_status()
