import urllib.request
from bs4 import BeautifulSoup
import requests

u='https://www.google.com/finance/quote/CBDX:LON'
#u='https://www.google.com/'
#u='https://www.baidu.com'
req = requests.get(u)
#print('done')
soup = BeautifulSoup(req.text,'html.parser')
#print('dd')
for l in soup.find_all('div'):
    p=l.get('data-last-price')
    if not(p is None):
        print(p)