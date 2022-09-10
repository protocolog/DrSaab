from django.test import TestCase
import json
import requests

request =requests.get("http://127.0.0.1:8000/disease/")
request_text = request.text
data = json.loads(request_text)
print(data)

# Create your tests here.
