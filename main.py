from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
# options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get(
    "https://www.korea.net/TalkTalkKorea/English/winners/WIN0000000468")
accept = driver.find_element_by_class_name('co-btn--danger')
driver.execute_script("arguments[0].click();", accept)
time.sleep(1)
page_source = driver.page_source
