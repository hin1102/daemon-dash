import requests
import json
import urllib.request

customerId = '55e94a6af8d8770528e60c22'
apiKey = '1a8c12195451ddcfbf6bade840550c9c'

responseAction = {
	201 : lambda : print('It worked'),
	400 : lambda : print('Uh oh, something in your payload is wrong'),
}

url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)

payload = {
  "type": "Savings",
  "nickname": "test",
  "rewards": 10000,
  "balance": 10000,	
}

req = requests.post(
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

responseAction[req.status_code]()

r = requests.get(url)
print (req)
