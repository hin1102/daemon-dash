# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json
import urllib.request

apiKey = 'defaf675f4be378719748dbe11ecc902'

responseAction = {
	201 : lambda : print('It worked'),
	400 : lambda : print('Uh oh, something in your payload is wrong'),
}

#url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
url = 'http://api.reimaginebanking.com/customers?key=defaf675f4be378719748dbe11ecc902'

#payload = {
#  "type": "Savings",
#  "nickname": "test",
#  "rewards": 10000,
#  "balance": 10000,	
#}

#req = requests.post(
#	url, 
#	data=json.dumps(payload),
#	headers={'content-type':'application/json'},
#	)
#r = requests.get(url)
#data = r.read()
#data = json.load(data)
#print(data)

result = urllib.request.urlopen(url)
#result = requests.get(url)
data = result.read().decode("UTF-8")

#data = result.content
temp = json.loads(data)
print(temp[0]["first_name"])
print(temp[0]["_id"])

url2 = "http://api.reimaginebanking.com/merchants?key=defaf675f4be378719748dbe11ecc902"
results2 = urllib.request.urlopen(url2)
data2 = result.read().decode("UTF-8")
temp2 = json.loads(data2)
print(temp2)
