import requests
from bs4 import BeautifulSoup
import datetime

todayM = datetime.date.today().month
todayD = datetime.date.today().day

url = 'https://www.ptt.cc/bbs/Baseball/index.html'


def geturl( url ):
    urlheaders = 'https://www.ptt.cc'
    
    resp = requests.get(url)
    
    soup = BeautifulSoup(resp.text,'html.parser')
    
    divlist = soup.find_all('div',class_="r-ent")
    
    count = 0
    
    for i in divlist:
        podate = i.find('div','date').text
        poM, poD = podate.split('/')
        
        if int(poM) ==todayM and int(poD) == todayD:
        
            try:
                print(f"標題:{i.find('div',class_='title').a.text}")
                full = urlheaders + i.find('div','title').a['href']
                print(f"超連結:{full}")        
            except AttributeError as A:
                print(A.args)
        
                
            print(f"作者:{i.find('div','author').text}")
            print(f"按讚數:{i.find('div','nrec').text}")
            podate = i.find('div','date').text
            print(f"發布日期:{podate}")
            print('-'*20)
            count += 1
                
    page = soup.find('div','btn-group btn-group-paging')
    alist = page.find_all('a')
    prevpage = urlheaders + alist[1]['href']
    #print(f"上一頁連結:{prevpage}")
    if count > 0:
            geturl( prevpage )

geturl( url )