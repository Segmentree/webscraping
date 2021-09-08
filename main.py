from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import choice
from string import ascii_lowercase
import time
import names


for i in range(0, 1000):
    NAME = names.get_full_name()
    EMAIL = ''.join(choice(ascii_lowercase) for i in range(
        12)) + '@' + ''.join(choice(ascii_lowercase) for i in range(12)) + '.com'
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
    name.send_keys(NAME)
    email.send_keys(EMAIL)
    check.click()
    page_source = driver.page_source
    submit = driver.find_element_by_xpath(
        '//a[@href="'+'javascript:fn_egov_save();'+'"]')
    submit.click()
    time.sleep(5)
    driver.close()
    print(f'vote number { i }')

print('End proccess')
