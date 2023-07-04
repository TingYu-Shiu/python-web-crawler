import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index.html'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

resp = requests.get(url,headers=header)

soup = BeautifulSoup(resp.text, 'html.parser')

#print(soup.prettify())-- 將結構顯現出來

article_title = soup.select('div[class="title"]')
#print(article_title)

for i in article_title:
    print(i.a.text)
    print('https://www.ptt.cc'+i.a['href'])
    print('_________')
    
#----------------(上面為首頁)---------------------

