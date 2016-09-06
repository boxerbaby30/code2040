import requests
import json
from datetime import date, timedelta
import dateutil.parser

token = "ea5deff31be998431e8c6959b2979d14"
url1 = "http://challenge.code2040.org/api/dating"
url2 = "http://challenge.code2040.org/api/dating/validate"

r = requests.post(url1, json={"token":token})
d = r.json()

datestamp = d.get('datestamp')
interval = int(d.get('interval'))

date = dateutil.parser.parse(datestamp)
new_date = date + timedelta(seconds=interval)
new_datestamp = new_date.isoformat('T')[0:19]+'Z'

a = requests.post(url2, json={"token":token, "datestamp":new_datestamp})
print a.content
