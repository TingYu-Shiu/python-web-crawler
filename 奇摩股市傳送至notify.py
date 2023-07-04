import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime


stockID = ['2330','2302','2303']
stockName = ['台積電','麗正','聯電']

count =[0,0,0]
while True:
    #time.sleep(10)
    for i in range(len(stockID)):
            
        url='https://tw.stock.yahoo.com/quote/'+ stockID[i]
        lineurl = 'https://notify-api.line.me/api/notify'
        token='WG4HCQCpagGeHft60WFY1xBd1gPJYB7URODWecenRoA'
        
        ha= {'Authorization':'Bearer ' + token}

  
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text,'html.parser')
        
        
        ul = soup.find('ul',class_='D(f) Fld(c) Flw(w) H(192px) Mx(-16px)')
        
        lilist = ul.find_all('li')
        
        成交 = float(lilist[0].find_all('span')[1].text.replace(',',''))
        
        昨收 = float(lilist[6].find_all('span')[1].text.replace(',',''))
        
        漲跌幅 = (成交-昨收)/昨收
        print(f'{stockName[i]}{漲跌幅:.4f}', time.strftime('%H:%M:%S',time.localtime()))
        #print(漲跌幅,(str(datetime.today())[11:19]))
        
        if 漲跌幅 < -0.03:
            count[i] += 1
            print(stockName[i]+'跌幅超過3%，建議賣出')
            msg ={'message':stockName[i]+'跌幅超過3%，建議賣出'}
            if count[i] <6:
                resp = requests.post(lineurl,headers=ha,params=msg)
        elif 漲跌幅 > 0.03:
            count[i] += 1
            print(stockName[i]+'漲幅超過3%，建議買入')
            msg ={'message':stockName[i]+'漲幅超過3%，建議買入'}
            if count[i] <6:
                resp= requests.post(lineurl,headers=ha,params=msg)
        else:
            count[i] = 0
    
            