import requests
import json
from datetime import datetime

url = 'https://www.nseindia.com/api/holiday-master?type=trading'

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'
headers['Accept'] = 'application/json'

r = requests.get(url=url,headers=headers)
resp = json.loads(r.text)

holidays = [x['tradingDate'] for x in resp['FO']]

with open('holidays.txt',mode='w') as f:
    f.write(str(holidays))
