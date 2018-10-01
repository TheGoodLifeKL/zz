# coding:utf-8
import requests,re

class NeihanSpider:
    def __init__(self):
        self.url = "https://www.neihan8.com/article/list_5_{}.html"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
        self.first_regex_encode = re.compile(r'<div class="f18 mb20">.*?</div>',re.S)
        self.second_regex_encode = re.compile(r'<.*?>|&(.*?);|\s|　　')


    def parse_url(self,url):
        response = requests.get(url,headers = self.headers)
        return response.content.decode("gbk")

    def analysis_data(self,data):
        data_list = self.first_regex_encode.findall(data)

        return data_list

    def save_data(self,data,num):
        with open("1.csv","a") as f:
            for content in data:
                second_data =self.second_regex_encode.sub("",content)
                f.write("第{}页\t".format(num))
                f.write(second_data)
                f.write("\n")

    def run(self):
        # 获取url路径
        num =1
        while num < 507:
            url = self.url.format(num)
            # 发送请求,获取响应
            json_str = self.parse_url(url)
            print(type(json_str))
            # 数据解析
            first_data = self.analysis_data(json_str)
            print(first_data)
            # 保存数据
            self.save_data(first_data,num)
            print("开始下载第{}页".format(num))
            num += 1


if __name__ == '__main__':
    tool = NeihanSpider()
    tool.run()
