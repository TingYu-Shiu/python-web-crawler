import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

url ='https://docs.google.com/spreadsheets/d/15X5bupyQzlu3xYh5McW2Wk9BRtN-F1SqjscN-IWFkIY/export?format=csv'

df = pd.read_csv(url)



plt.figure(figsize=(5,5),dpi=300)
plt.rcParams['font.sans-serif']='Microsoft JhengHei'
#plt.rcParams['font.size'] = 16 #改整張圖的字體大小

'''
thisyear = datetime.now().year
df['年齡'] = thisyear - df['出生年月日'].str[:4].astype('int')

print('平均年齡:{:.2f}'.format(df['年齡'].mean()))
df['年齡10量化'] = df['年齡']//10 *10

s = df['年齡10量化'].value_counts()

plt.bar(s.index, s.values,width=3)
plt.grid()
'''
'''
df = df.rename(columns={'你對課程的滿意度': '滿意度'})
print('平均滿意度:{:.2f}'.format(df['滿意度'].mean()))
s2 = df['滿意度'].value_counts()
plt.bar(s2.index,s2.values)
plt.xticks((1,2,4,3,5))
plt.grid()
'''
'''
這題很重要很難

df = pd.read_csv( url )
df1 = df.iloc[:, 4:10]
df1.columns = ['Excel', 'PowerPoint', 'Word',
               'Google試算表','Google簡報','Google文件']
familiar = ['完全不熟', '不是很熟', '普通', '還算可以', '相當熟練']

plt.figure( figsize=(15,5), dpi=300)
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'

for i in range(5):
    count = []
    for j in range(6):
        count.append( df1[ df1.iloc[:,j]==familiar[i] ].count()[0] )
    plt.bar(np.arange(6)-0.3+i*0.15, count, label=familiar[i], width=0.15)
    
    
plt.xticks(np.arange(6), df1.columns)
plt.legend()
plt.grid()
plt.savefig('4-5軟體熟悉度長條圖.png')
'''


pandas.melt( DataFrame,
id_vars=[固定不動的欄位],
value_vars=[取消樞紐的欄位],
var_name='取消樞紐的欄位名的欄位名',
value_name='取消樞紐的值的欄位名',
ignore_index=True )


s1 = df['你的興趣(複選)'].str.replace(' ','')
df1 = s1.str.split(',',expand=True)
df2 = pd.melt(df1,value_name='興趣', ignore_index=False)
df2 = df2[df2['興趣'].notna()]
s = df2['興趣'].value_counts()


