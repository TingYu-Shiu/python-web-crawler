import requests

url = "https://irs.thsrc.com.tw/IMINT/?locale=tw&_ga=2.104041351.608170395.1683701198-968809144.1683701196"

ua = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

resp = requests.get(url, headers = ua)

if resp.status_code == 200:
    with open ('高鐵.html','w',encoding='utf-8') as fobj:
        fobj.write ( resp.text )

print(resp.text)        



