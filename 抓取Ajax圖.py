import requests
from bs4 import BeautifulSoup
import os

path = './運動相簿/'
if not os.path.exists(path):
    os.mkdir(path)

url='https://running.biji.co/index.php?pop=ajax&func=album&fename=load_more_photos_in_listing_computer'


fdata={'type': 'album',
       'rows': '0',
       'need_rows': '120',
       'cid': '10298',
       'album_id': '49026',
       'start':'',
       'end':'',
       'subtitle':''}

resp = requests.post(url,data=fdata)

with open('test.html','w',encoding='utf-8') as fobj:
    fobj.write(resp.text)
    
soup = BeautifulSoup(resp.text,'html.parser')
imglist = soup.find_all('img','photo_img photo-img')

count = 0
for i in imglist:
    count += 1
    url = i['src'].replace('/600','/2048')
    resp = requests.get(url)
    with open(path+str(count)+'.jpg','wb') as fobj:
        fobj.write(resp.content)        
    print(count,url)

    