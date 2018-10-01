# coding=utf-8

import requests

session =requests.session()
post_url = "http://www.renren.com/PLogin.do"
post_data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}

# 使用session发送post请求,并保存cookie
session.post(post_url,data=post_data,headers=headers)

# 再次使用session进行请求登陆之后才能访问的地址
r = session.get("http://www.renren.com/327550029/profile",headers=headers)

# 保存页面
with open("renren1.html", "wb") as f:
    f.write(r.content)

