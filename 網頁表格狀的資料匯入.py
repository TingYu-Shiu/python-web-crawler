import requests
import pandas as pd
import sqlite3 

conn = sqlite3.connect('中獎號碼.db')

d1 = pd.date_range('20210101','20210202', freq='M')

for i in d1:
    y = str(int(str(i)[0:4])-1911)
    m = str(int(str(i)[5:7]))
    print('抓取',y,'年',m,'月資料')

    url = 'https://www.taiwanlottery.com.tw/lotto/lotto649/history.aspx'
    
    payload = {'__EVENTTARGET': '', 
    '__EVENTARGUMENT': '', 
    '__LASTFOCUS': '', 
    '__VIEWSTATE': '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',
    '__VIEWSTATEGENERATOR': '11E838D2',
    '__EVENTVALIDATION': '71LRgFWBputVTVaJfZjKmx/H1dhm7XjXBQ83/T/YMfBwGbLcmMs/FZ+h6ZKE+wh80OXs0EewOomVv/IOUQfVI8r8Rulqf/IPIu/WanO2w3WxeFXzJcUwhxTifbdfDSKQRsVgoHUCuQc3xDKxZdRonjro6UJ6TxdPtH77KTFQEsO+7ItpGdBCgL2zACjpIrN44SSuEKRvf3U0j/xgbPToHCvrNvoRq6jTwIzPz3UOrSZg32KcMy9RZj7BIW0WXE6nU6O8hfhia18vFgazSU0Z/s25BUlkC4ZpfYlNox8IUz83R+RO+gTBd0re9ZPfgM6eNCcXHP6M/UCKh2l5p3R/88+3i7uB3lDSnoYFzFvZNzN5YM+80J2hf0VtUYIzlkoE9yvQUW90PShv5fne9X3HLXTSaViFfs0XU5q70t0Sr8+El3dhEwas4qkq1uX+RKtn1DK78DTNFsD1vRglUlVinfb23CNpNk3QjbgGituMgSVrzmEvXea768eIAFbCS1uCNFF6uWlIf9/PByxbc2Tgrx1ZygMH2P2/pYm042vB/IFUH2gIXzUXh5vUHD6PK7fBBneDR/jOi1xlXrj6S5z1VqHRjft2aN8QuCxLFngUqCuTrdnllJKj6gYkh7IzAfsmonm2Ra7Zd8FJ/vLSenRh1C+faQMGnNiXqmF3gEwCx51RHLMr',
    'forma': '請選擇遊戲',
    'Lotto649Control_history$chk': 'radYM',
    'Lotto649Control_history$dropYear': y,
    'Lotto649Control_history$dropMonth': m,
    'Lotto649Control_history$btnSubmit': '查詢'}
    
    resp = requests.post(url, data = payload)
    
    with open ('大樂透'+y+m+'.html','w',encoding='utf-8') as fobj:
        fobj.write( resp.text )
        
    list1 = pd.read_html( resp.text ) 
    
    colName = ['期別','開獎日','兌獎截止','銷售金額','獎金總額','獎號1','獎號2','獎號3','獎號4','獎號5','獎號6','特別號']
    
    
    for d in list1[2:-1]: #大樂透取內容
        data = []
        data.append(d.iloc[1,0])    #期別
        data.append(d.iloc[1,1])    #開獎日
        data.append(d.iloc[1,3])    #兌獎截止
        data.append(d.iloc[1,5])    #銷售金額
        data.append(d.iloc[1,7])    #獎金總額
        for i in range(2, 9):
            data.append( d.iloc[4, i] )  
        dftemp = pd.DataFrame([data],columns=colName)
        print( dftemp )
        sql = 'Select * from 大樂透 Where 期別 ="'+ data[0] +'"'
        try:
            dfcheck = pd.read_sql(sql,conn)
        except:
            dfcheck = pd.DataFrame(columns=colName)
        if len(dfcheck)==0:
            dftemp.to_sql('大樂透.html', conn,index=False, if_exists='append')
        
        
        print('----------------------------')
        