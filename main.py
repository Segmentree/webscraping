from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import choice
from string import ascii_lowercase
import time
import names

URL = 'https://www.korea.net/TalkTalkKorea/English/winners/WIN0000000468'
OPTIONS = ['--ignore-certificate-errors', '--incognito', '--headless']
# OPTIONS = ['--ignore-certificate-errors', '--incognito']
count = 0


def name_generator():
    return names.get_full_name()


def word_generator(n):
    return ''.join(choice(ascii_lowercase) for i in range(n))


def email_generator():
    return word_generator(12) + '@' + word_generator(12) + '.com'


def add_vote(url=URL):
    global count
    NAME = name_generator()
    EMAIL = email_generator()
    try:
        options = webdriver.ChromeOptions()
        for opt in OPTIONS:
            options.add_argument(opt)
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        accept = driver.find_element_by_class_name('co-btn--danger')
        accept.click()
        time.sleep(1)
        name = driver.find_element_by_id('voteName')
        email = driver.find_element_by_id('voteEmail')
        check = driver.find_element_by_id('countryOth')
        name.send_keys(NAME)
        email.send_keys(EMAIL)
        check.click()
        submit = driver.find_element_by_xpath(
            '//a[@href="'+'javascript:fn_egov_save();'+'"]')
        submit.click()
        time.sleep(2)
        success = driver.find_element_by_xpath(
            "//*[contains(text(), 'Thank you for participating in the voting event!!')]")
        # confirm = driver.find_element_by_xpath("//*[contains(text(), 'Confirm')]")
        # confirm.click()
        if success.text != 'Thank you for participating in the voting event!!':
            raise ValueError("Doesn't match")
        print('Success : ', success.text)
        count += 1
        driver.close()
    except:
        print('Fail')


for i in range(1, 2000):
    add_vote()
    print(f'cycle : {i}')

print(f'End proccess { count }')
