# coding:utf-8

from selenium import webdriver
import time
import requests
from yundama.dama import indetify


driver = webdriver.Chrome()
driver.get("https://www.douban.com")

driver.find_element_by_id("form_email").send_keys("1973488043@qq.com")
driver.find_element_by_id("form_password").send_keys("18838972980kl")

# 识别验证码
captcha_image_url = driver.find_element_by_id("captcha_image").get_attribute("src")
captcha_content = requests.get(captcha_image_url).content
captcha_code = indetify(captcha_content)
print("验证码的识别结果为:",captcha_code)

# 输入验证码
driver.find_element_by_id("captcha_field").send_keys(captcha_code)

driver.find_element_by_class_name("bn-submit").click()

cookies = {i["name"]:i["value"] for i in driver.get_cookies()}
print(cookies)
time.sleep(3)
driver.quit()