import requests
import json
import pandas

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.__dict__)

response_json = response.json()
print(response_json['iss_position']['latitude'])
