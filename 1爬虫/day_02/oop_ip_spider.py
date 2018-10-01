# coding:utf-8
import requests,re

class IpSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
        self.url_temp = "http://www.xicidaili.com/wt/{}"
        self.ip_threading = []

    def get_url_list(self):
        return [self.url_temp.format(i+1) for i in range(10)]

    def request_parse_url(self,url):
        response = requests.get(url,headers=self.headers)
        return response.content

    def save_file(self,file,page_num):
        with open("page-{}.html".format(page_num),"wb") as f:
            f.write(file)
            print("第{}页下载完成".format(page_num))
            return "page-{}.html".format(page_num)
    def re_ip(self,file_name):
        f =  open(file_name)
        content = f.read()
        # print(content)
        li = []
        ip = re.findall(r"((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))",content)
        li.append(ip)
        print(li)
        #port =
    def run(self):
        # 获取url列表
        url_list= self.get_url_list()
        # 遍历列表,发送请求,获取应答
        for url in url_list:
            file = self.request_parse_url(url)
        # 保存
            file_name = self.save_file(file,page_num = (url_list.index(url)+1))
        # 正则提取ip地址,建立ip池,{"ip":ip,"times":num}
            self.re_ip(file_name)

if __name__ == '__main__':
    ipspider = IpSpider()
    ipspider.run()
