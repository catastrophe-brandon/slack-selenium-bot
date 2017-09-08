from selenium import webdriver
import os
import time
from faker import Faker
from selenium.webdriver.common.by import By

fake = Faker()

slack_domain = os.getenv('SLACK_DOMAIN', 'default')

url = 'https://{}.slack.com'.format(slack_domain)


webdriver = webdriver.Firefox()
webdriver.get(url)
# At this point you'll need to sign in to Slack to allow the bot to do its thing.
# You have 60 seconds.
time.sleep(60)
textbox = webdriver.find_element_by_css_selector('#msg_input > div:nth-child(1)')
time.sleep(5)

while True:
    textbox.send_keys(fake.text() + '\n')
    time.sleep(60)


