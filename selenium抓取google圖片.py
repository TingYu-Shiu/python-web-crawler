from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless') #不會彈出視窗
options.add_argument('--no-sandbox') #在沙盒模式下運行Chrome瀏覽器
driver = webdriver.Chrome('chromedriver',options=options)
driver.implicitly_wait(10)


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

driver.get("https://www.google.com.tw/imghp?hl=zh-TW&authuser=0&ogbl")
# 最大化窗口，因為每一次爬取只能看到視窗内的圖片  
driver.maximize_window()
# 紀錄下載過的圖片網址，避免重複下載  
img_url_dic = {}

from selenium.webdriver.common.by import By
q = driver.find_element(By.NAME, 'q')
keyword='鴨'
q.send_keys(keyword)
q.submit()

from urllib import request
import time

# 模擬滾動視窗瀏覽更多圖片
pos = 0  
count = 0 # 圖片編號 
for i in range(30):  
    pos += 500 
    js = "document.documentElement.scrollTop=%d" % pos
    #document.documentElement.scrollTop 是用於獲取或設置文檔的根元素（即 <html> 元素）的滾動位置的属性。
    driver.execute_script(js)  
    time.sleep(1)
    
    '''
frame可见并切换到该frame上
EC.frame_to_be_available_and_switch_to_it
元素可以点击，常用于按键
EC.element_to_be_clickable
元素出现，只要一个符合条件的元素加载出来就通过
EC.presence_of_element_located
元素出现，须所有符合条件的元素都加载出来，这个基本上就是你爬取的最主要内容了
EC.presence_of_all_elements_located
判断某段文本是否出现在某元素中，常用于判断输入页数与实际高亮页数是否一致
EC.text_to_be_present_in_element
    '''

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'Q4LuWd'))
    )
    
    
    imgs = driver.find_elements(By.CLASS_NAME,'Q4LuWd') #全部記得+s


    path = '.\鴨'
# 檢查目錄是否存在，如果不存在則創建目錄
if not os.path.exists(path):
    os.mkdir(path)

for img in imgs:
    # 獲取圖片的URL(get_attribute是web element的用法,只有在webdriver還在執行時才能使用)
    img_url = img.get_attribute("src")
    
    # 檢查URL是否有效且未被處理過
    if img_url is not None and img_url not in img_url_dic:
        img_url_dic[img_url] = ''
        count += 1
        
        # 設定圖片的保存路徑(os.path.join 串聯路徑)
        save_img = os.path.join(path, keyword + str(count) + '.jpg')
        
        # 打開圖片URL並將其保存到文件中(fdata ，requests打不開，要用urllib.request)
        with request.urlopen(img_url) as response:
          data = response.read()
        with open(save_img, "wb") as f:
          f.write(data)
            
driver.close() 

