# coding
import requests

headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}

cookie = "anonymid=jjcjs4ov-qzxc3y; depovince=GW; _r01_=1; jebe_key=77a4afaf-a6d5-455d-b355-454d5596a910%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1531038001934%7C1%7C1531038005818; JSESSIONID=abcVXlxysuvmN6599i5rw; jebecookies=316339fc-2ba4-4316-8831-376ccad7d110|||||; ick_login=86154777-0a21-4d54-bca2-ca45ade262e3; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=f94858e0e7f1f128f24913c0eab540509; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn121/20180614/1515/main_yJK9_18cb000005581986.jpg; t=d68b4002a080ebe25e10c8daabf88cdb9; societyguester=d68b4002a080ebe25e10c8daabf88cdb9; id=327550029; xnsid=86db75d9; loginfrom=syshome; wp_fold=0"

cookie = {i.split("=")[0]:i.split("=")[1] for i in cookie.split(";")}
print(cookie)
response = requests.get("http://www.renren.com/327550029/profile", headers=headers, cookies=cookie)

# 保存文件
with open("renren3.html","wb") as f:
    f.write(response.content)