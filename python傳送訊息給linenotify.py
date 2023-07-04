import requests
import random
url = 'https://notify-api.line.me/api/notify'
token='SyzZUq7bQzjcDp9CPsplSiESIM7vYegFTFF1p8xvSgr'

ha= {'Authorization':'Bearer ' + token}
msg ={'message':'測試訊息'}


with open('pic.png','rb') as fobj:
    img = fobj.read()
imgfile={'imageFile':img}

resp = requests.post(url, headers=ha, params=msg,files=imgfile)

'''
while True:
    num = random.randint(1,101)
    print(f'亂數出數字 {num}')
    
    if num % 10 == 7:
        msg ={'message': '亂數出數字 ' + str(num)}
        resp = requests.post( url, headers = ha, params=msg)
    if num == 100:
        break
'''