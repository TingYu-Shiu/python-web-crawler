import pandas as pd
import matplotlib.pyplot as plt

url = 'https://od.cdc.gov.tw/eic/NHI_EnteroviralInfection.csv'

df = pd.read_csv( url )

s1 = df.groupby('縣市')['腸病毒健保就診人次'].mean()
print( s1 )

city = ['基隆市','台北市','新北市','桃園市','新竹市','新竹縣',
        '苗栗縣','台中市','南投縣','彰化縣','雲林縣','嘉義市',
        '嘉義縣','台南市','高雄市','屏東縣','宜蘭縣','花蓮縣',
        '台東縣','澎湖縣','金門縣','連江縣']

plt.figure( figsize=(15,5), dpi=300)
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'
plt.plot(s1[city].index, s1[city].values)
plt.grid()
plt.title('各縣市每週平均腸病毒就診人次統計圖', fontsize=25)
plt.xticks( rotation=45)
plt.savefig('4-2腸病毒統計_依縣市.png')