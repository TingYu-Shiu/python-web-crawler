from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()
prefs = {'download.prompt_for_download': True}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome( options=options )
driver.get("https://www.google.com/")
driver.maximize_window()
element = driver.find_element(By.NAME,"q")
element.click()
element.send_keys('台灣證券交易所')
element.send_keys(Keys.ENTER)
time.sleep(2)
element = driver.find_element(By.PARTIAL_LINK_TEXT,'首頁- TWSE 臺灣證券交易所')
element.click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, "close").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "交易資訊").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "每日收盤行情").click()
time.sleep(1)
driver.find_element(By.NAME, "dd").click()
dropdown = driver.find_element(By.NAME, "dd")
dropdown.find_element(By.XPATH, "//*[@id='form']/div/div[1]/div[1]/span/select[3]/option[9]").click()
dropdown.find_element(By.XPATH, "//option[. = '全部(不含權證、牛熊證、可展延牛熊證)']").click()
driver.find_element(By.CLASS_NAME, "submit").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, "csv").click()


    



