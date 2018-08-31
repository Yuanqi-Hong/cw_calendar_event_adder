# fix: Reordered elements for better UX
# added wait feature to make sure event edit it saved

event_url = input('Paste event URL here: ')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get('https://courseworks2.columbia.edu')

uni = driver.find_element_by_xpath('//*[@id="username"]')
uni.send_keys('yourUNI')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('yourPassword')

login = driver.find_element_by_xpath('//*[@id="fm1"]/div[3]/input[4]')
login.click()

calendar = driver.find_element_by_xpath('//*[@id="global_nav_calendar_link"]')
calendar.click()

driver1 = webdriver.Chrome()
driver1.get(event_url)

title = driver1.find_element_by_class_name('eventTitle').text
title

when = driver1.find_element_by_class_name('eventWhen')
when_str = when.text
when_str

where = driver1.find_element_by_class_name('eventWhere').text
where

when1 = datetime.strptime(when_str.split(' - ')[0], '%A, %B %d, %Y %I:%M %p')
when2 = datetime.strptime(when_str.split(' - ')[1], '%I:%M %p')
date = when1.strftime('%Y-%m-%d')
from_ = when1.strftime('%H:%M')
_to = when2.strftime('%H:%M')

create_btn = driver.find_element_by_xpath('//*[@id="create_new_event_link"]')
create_btn.click()

Title = driver.find_element_by_xpath('//*[@id="calendar_event_title"]')
Title.send_keys(title)

Date = driver.find_element_by_xpath('//*[@id="calendar_event_date"]')
Date.clear()
Date.send_keys(date)

From = driver.find_element_by_xpath('//*[@id="calendar_event_start_time"]')
From.clear()
From.send_keys(from_)

To = driver.find_element_by_xpath('//*[@id="calendar_event_end_time"]')
To.clear()
To.send_keys(_to)

Location = driver.find_element_by_xpath('//*[@id="calendar_event_location_name"]')
Location.send_keys(where.split('\n')[0] + '  ' + where.split('\n')[1])
Location.send_keys('\n')

delay = 3
try:
    WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="create_new_event_link"]')));
except TimeoutException:
	pass

driver.quit()
driver1.quit()

raise SystemExit()