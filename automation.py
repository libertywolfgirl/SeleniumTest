from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome_browser = webdriver.Chrome(options=options)
chrome_browser.get("https://www.selenium.dev/selenium/web/web-form.html")

user_message = chrome_browser.find_element(By.ID, 'my-text-id')
submit_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-outline-primary')

time.sleep(1)
user_message.send_keys('I AM EXTRA COOOOL')
time.sleep(1)
current_text = user_message.get_attribute('value')
print(current_text)
assert 'I AM EXTRA COOOOL' in current_text
submit_button.click()
time.sleep(1)
chrome_browser.back()
time.sleep(1)
user_message.clear()
time.sleep(1)
chrome_browser.quit()
