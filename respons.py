from http.client import responses

import requests
from pprint import pprint
# API_URL='http://localhost:8000/predict?age=youth&income=medium&student=yes&credit_rating=fair'
API_URL='http://localhost:8000/condition?feature=age&value=youth'
response=requests.get(API_URL)
print(response)
print(response.status_code)
pprint(response.json())