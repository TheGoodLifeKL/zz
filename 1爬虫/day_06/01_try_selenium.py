# coding:utf-8
import time
from selenium import webdriver


driver = webdriver.Chrome()
# driver = webdriver.PhantomJS()
# driver.set_window_size(1920,1080)
driver.maximize_window()

# 发送请求
driver.get("http://www.baidu.com")

# 进行页面截屏
driver.save_screenshot("./baidu.png")

driver.find_element_by_id("kw").send_keys("huya")
driver.find_element_by_id("su").click()
print(driver.current_url)

# driver获取html文件
# print(driver.page_source)

# driver获取cookies
# cookies = driver.get_cookies()
# print(cookies)
# print("*"*30)
# cookies = {i["name"]:i["value"] for i in cookies}
# print(cookies)

time.sleep(5)
driver.quit()