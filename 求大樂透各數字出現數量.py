import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('中獎號碼.db')

sql = 'Select * From 大樂透;'
df = pd.read_sql(sql, conn)

slist = []

for i in range(5,12):
    s = df.iloc[:,i].value_counts()
    slist.append(s)
    
df1 = pd.DataFrame(slist)
df1 = df1.fillna(0) #將nah
df1 = df1.sort_index(axis=1) #欄index排序

s1 = df1.sum()

plt.figure(figsize=(15,5), dpi=300)
plt.bar(s1.index, s1.values)
plt.ylim(90,165)
for i in s1.index:
    plt.text(i, s1[i], int(s1[i]),ha='center',va='baseline',rotation=90)
    
plt.savefig('4-1大樂透號碼統計.png')