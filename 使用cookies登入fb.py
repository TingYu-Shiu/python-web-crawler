from selenium import webdriver
from time import sleep
import json
import time

if __name__ == '__main__':
    with open('cookies_jar.json') as f:
        cookies = json.load(f)
    driver = webdriver.Chrome()
    driver.implicitly_wait(100)

    driver.get('https://www.facebook.com/?ref=tn_tnmn')

    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    
    time.sleep(10)
    
    print(driver.page_source)
    
    
    
with open('fb.html', 'w', encoding='utf-8',) as file:
    file.write(driver.page_source)

driver.quit()
