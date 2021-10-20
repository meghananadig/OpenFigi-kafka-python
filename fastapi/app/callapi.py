import requests
import json
from time import sleep
from json import dumps



headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response_API = requests.post('https://api.openfigi.com/v3/search', json={"query": "ibm", "exchCode": "US"}, headers=headers);
response_json = response_API.json()
print((response_json));
#response_json = response_json.values()
response_result_set = ((response_json['data']));







