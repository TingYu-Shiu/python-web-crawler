import requests
import pandas as pd
import sqlite3
import time

conn = sqlite3.connect('臺銀.db')

d1 = pd.date_range('20220801','20230430')

for dtemp in d1:
    d = str(dtemp)[0:10]

    sql = 'Select * From 匯率 Where 日期 ="'+d+'"'

    try: #移到前面優化
        dfcheck = pd.read_sql(sql, conn)
    except:
        dfcheck = pd.DataFrame()
    
    if len(dfcheck) == 0:

        url="https://rate.bot.com.tw/xrt/all/"+d
        time.sleep(2)
        print(d)
        print(url)
        print('----------------')
        list1 = pd.read_html(url)
        df =list1[0]
        if len(df)>1: #假日沒營業沒資料
            df = df.iloc[:,:5]
            df.columns=['幣別','現金買入','現金賣出','即期買入','即期賣出']
            df['幣別代號'] = df['幣別'].str.split(' ').str[1].str.replace('(','').str.replace(')','')
            df['幣別'] = df['幣別'].str.split(' ').str[0] 
            #str[0] = list串列中字串的第0欄
            
            for i in range(1,5):
                df.iloc[:,i] = pd.to_numeric(df.iloc[:,i], errors='coerce')
            
            df = df.set_index('幣別代號')
            #set_index 只能針對DataFrame內有的欄位設定
            
            df['日期'] = d
            df.to_sql('匯率', conn, if_exists='append')