import requests
from bs4 import BeautifulSoup
import os

path = './屏東高速蜜鄉馬拉松/'
if not os.path.exists(path):
    os.mkdir(path)
    
count = 0

for p in range(3):

    url='https://www.sportag.net/web/event-photo.php?event_id=837&view=all&page='+str(p)
    
    
    resp = requests.get(url)
    with open('test1.html','w',encoding='utf-8') as fobj:
        fobj.write(resp.text)
    
    soup = BeautifulSoup(resp.text,'html.parser')
    imglist = soup.find_all('img',style='width:100%;height:auto;')
    
    
    for i in imglist:
        count += 1
        url = i['src']
        resp = requests.get(url)
        with open(path+str(count)+'.jpg','wb') as fobj:
            fobj.write(resp.content)