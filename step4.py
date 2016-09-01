import requests
import json
import re

token = "ea5deff31be998431e8c6959b2979d14"
r = requests.post("http://challenge.code2040.org/api/prefix", json={"token":token})
d = r.json()
prefix = d.get('prefix')
print prefix
array = d.get('array')
print array
new_array = []
for word in array:
    if not re.match(prefix, word):
        print word
        new_array.append(word)
print new_array
a = requests.post("http://challenge.code2040.org/api/prefix/validate", json={"token":token,"array":new_array})
print a.content
