import requests
import json

token = "ea5deff31be998431e8c6959b2979d14"
r = requests.post("http://challenge.code2040.org/api/reverse", json={"token":token})
print r.content
w = r.content[::-1]
a = requests.post("http://challenge.code2040.org/api/reverse/validate", json={"token":token,"string":w})
print a.content
