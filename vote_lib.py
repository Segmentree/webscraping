from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import choice
from string import ascii_lowercase
import time
import names
import os

URL = 'https://www.korea.net/TalkTalkKorea/English/winners/WIN0000000468'
OPTIONS = ['--ignore-certificate-errors', '--incognito',
           '--disable-dev-shm-usage', '--no-sandbox', '--headless']
# OPTIONS = ['--ignore-certificate-errors', '--incognito']
count = 0


def name_generator():
    return names.get_full_name()


def word_generator(n):
    return ''.join(choice(ascii_lowercase) for i in range(n))


def email_generator():
    return word_generator(12) + '@' + word_generator(12) + '.com'


def add_vote(url=URL):
    NAME = name_generator()
    EMAIL = email_generator()
    global count
    try:
        options = webdriver.ChromeOptions()
        # options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        for opt in OPTIONS:
            options.add_argument(opt)
        # driver = webdriver.Chrome(executable_path=os.environ.get(
        #     "CHROMEDRIVER_PATH"), options=options)
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


def engine(iteration_size, url=URL):
    global count
    count = 0
    for i in range(0, iteration_size):
        add_vote(url)
    return iteration_size, count
