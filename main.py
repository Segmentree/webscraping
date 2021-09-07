from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get(
    "https://www.korea.net/TalkTalkKorea/English/winners/WIN0000000468")
accept = driver.find_element_by_class_name('co-btn--danger')
accept.click()
time.sleep(1)
name = driver.find_element_by_id('voteName')
email = driver.find_element_by_id('voteEmail')
check = driver.find_element_by_id('countryOth')
name.send_keys('Myname')
email.send_keys('a@b.com')
check.click()
page_source = driver.page_source
