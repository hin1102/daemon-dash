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
#url = 'http://api.reimaginebanking.com/customers?key=defaf675f4be378719748dbe11ecc902'
#url = 'http://api.reimaginebanking.com/merchants?key=defaf675f4be378719748dbe11ecc902'
url = 'http://api.reimaginebanking.com/branches?key=defaf675f4be378719748dbe11ecc902'

result = urllib.request.urlopen(url)
#result = requests.get(url)
data = result.read().decode("UTF-8")

#data = result.content
temp = json.loads(data)
print(temp[0])


text_file = open("branches.txt", "w")
for i in range(0, len(temp)):
    #line = '' + str(temp[i]["first_name"]) + ' ' + str(temp[i]["last_name"]) + ' ' + str(temp[i]["_id"]) + ' ' + str(temp[i]["state"]) + ' ' + str(temp[i]["zip"])
    text_file.write('"{}" "{}"\n'.format(temp[i]["geocode"]["lat"], temp[i]["geocode"]["lng"]))

text_file.close()
