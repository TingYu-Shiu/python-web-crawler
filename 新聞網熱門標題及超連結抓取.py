from bs4 import BeautifulSoup
import requests

url='https://api.hakkatv.org.tw/api/news/index?'
fdata ={'per': '4','sort[created_at]': 'desc',
'type': 'hakka'
,'keywords':''}

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}


resp = requests.post(url,data=fdata, headers=header)


soup = BeautifulSoup(resp.text,'html.parser')

print(soup.beautiffy)