#  HTTP POST "/" with JSON body {"num": 100} to 127.0.0.1:5000

import requests
import json

url = 'http://mp2-t1-1568464906.us-east-2.elb.amazonaws.com:80/'
data = {"num": 100}
headers = {'content-type': 'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.text)
