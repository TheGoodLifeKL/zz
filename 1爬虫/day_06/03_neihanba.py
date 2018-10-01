# coding:utf-8

from selenium import webdriver

driver = webdriver.Chrome()
# driver.get("https://www.neihan8.com/wenzi/")
driver.get("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=python&rsv_pq=ec7935d8000017e2&rsv_t=c1537DnQVGythASY6RyAKkkp3YuryDRBiXIzy1oWLNU9b5GxzjplA6nCDHk&rqlang=cn&rsv_enter=1&rsv_sug3=6&rsv_sug1=6&rsv_sug7=101")

# ret = driver.find_elements_by_xpath("//div[@class='left']/div[@class='text-column-item box box-790']")
# ret = driver.find_elements_by_xpath("//div[@class='text-column-list mt10']//div[@class='text-column-item box box-790']")
# print("-----2----")
# print(ret)
# print("-----3----")
#
# for li in ret:
#     print("-----1------")
#     # print(li.find_element_by_xpath("./div[@class='desc']").text)
#     print(li.find_element_by_xpath("./h3/a").get_attribute("href"))
print(driver.find_element_by_link_text("下一页>").get_attribute("href"))
driver.quit()
