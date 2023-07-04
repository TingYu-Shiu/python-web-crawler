import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd

resp = requests.get('https://www.brothers.tw/team_n1.php')
list1 = pd.read_html(resp.text)

df1t = list1[3]
df1 = df1t.iloc[3:-1,2]

team1 = list(df1.str.split(" ").str[0]) #中信兄弟

team2 = ['陳韻文','江辰晏','林子崴','潘威倫','古林睿煬','吳丞哲','李慶隆','劉軒荅','劉予辰','楊淳弼','李其峰','邱浩鈞','黃竣彥','王鏡銘','傅于剛','林威志','羅昂','施子謙','林航','布雷克','吳承諭','胡智為','林原裕','鄭鈞仁','方建德','柯瑞','張竣凱','姚杰宏','李承鴻',
'楊孟沅','劉志宏','江承峰','江國謙'] #統一獅

url = 'https://monkeys.rakuten.com.tw/players#first-team_pitcher'

resp = requests.get(url)

soup = BeautifulSoup(resp.text,'html.parser')

tempc = soup.find('div',id="pitcher")
tempcc = tempc.find_all('div',class_='name')

team3 =[] #樂天桃園
for i in tempcc:
    team3.append(str(i.text))
    
url2 ='https://www.fubonguardians.com/content/info/PlayersList?t=2'

resp1 = requests.get(url2)
soup1 = BeautifulSoup(resp1.text,'html.parser')
tempd = soup1.find('div',class_="fbg-member-list")
tepdd = tempd.find_all(class_="member-name")

team4 =[] #富邦悍將
for j in tepdd:
    team4.append(str(j.text.split('\r\n')[1].strip()))
    
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

url3 ='https://www.wdragons.com/team_cat/hero/hero-pitcher/'

resp3 = requests.get(url3,headers=header)

soup3 = BeautifulSoup(resp3.text,'html.parser')

tempe = soup3.find('div',class_="row customRow")

tempee = tempe.find_all(class_="name")[0].text.replace("*","")

tempee = tempe.find_all(class_="name")

team5 =[]#味全龍
for k in tempee:
    team5.append(k.text.replace("*",""))

teams =[team1,team2,team4,team4,team5]

#--------------------------    

todayM = datetime.date.today().month
todayD = datetime.date.today().day

url = 'https://www.ptt.cc/bbs/Baseball/index.html'
countList= [0,0,0,0,0]

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
                title = i.find('div',class_='title').a.text
                for l in range(len(teams)):
                    for m in teams[l]:
                        if m in title:
                            countList[l] +=1
                    
                print(f"標題:{title}")
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