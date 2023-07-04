import requests
from bs4 import BeautifulSoup
import os

resource_path = './res2'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)

url ='https://www.ptt.cc/bbs/Gossiping/index.html'

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

ss = requests.session()
ss.cookies['over18']='1'
#ss.cookies.set('over18','1')

resp = ss.get(url, headers=header)

d = 39514
count = 0

while d >= 39510:

    url1 = 'https://www.ptt.cc/bbs/Gossiping/index'+str(d)+'.html'
    
    
    resp2 = ss.get(url, headers=header)
    
    soup = BeautifulSoup(resp2.text, 'html.parser')
    
    article_title = soup.select('div[class="title"]')
    
    for i in article_title:
        try:
            print(i.a.text)
            print('https://www.ptt.cc'+i.a['href'])
            
            article_url='https://www.ptt.cc'+i.a['href']
            article_title = i.a.text
            
            #對文章網址提出請求(爬取下來單一文章網址)
            article_res = ss.get(article_url, headers=header)
            article_soup =BeautifulSoup(article_res.text,'html.parser')
            #宣告一個變數裝文章的內容
            article_content = article_soup.select('div[id="main-content"]')[0].text
            
            try: #等同'{}/{}.txt'.format(resource_path,article_title)
                with open('{}/{}.txt'.format(resource_path,article_title+str(count)),'w',encoding='utf-8') as fobj:
                      fobj.write(article_content)
                count += 1
            except:
                print('error')
        except AttributeError as e:
            print(i)
            print(e.args)
    
    
        
    d -= 1