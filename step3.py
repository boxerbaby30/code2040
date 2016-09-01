import requests
import json

token = "ea5deff31be998431e8c6959b2979d14"
r = requests.post("http://challenge.code2040.org/api/haystack", json={"token":token})
d = r.json()
print d
search_string = d.get('needle')
array = d.get('haystack')
for word in array:
    if word == search_string:
        ind = array.index(word)
a = requests.post("http://challenge.code2040.org/api/haystack/validate", json={"token":token,"needle":ind})
print a.content
