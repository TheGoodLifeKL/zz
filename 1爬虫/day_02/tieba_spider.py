# coding:utf-8
import requests

class TiebaSpider:
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw="+tieba_name+"&ie=utf-8&pn={}"
        self.headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}

    def get_url_list(self):
        # url_list = []
        # for i in range(1000):
        #     url_list.append(self.url_temp.format((i+1)*50))
        # return url_list
        return [self.url_temp.format(i*50) for i in range(1000)]

    def request_parse_url(self,url):
        response = requests.get(url,headers=self.headers)
        return response.content

    def save_file(self, file_name,page_num):
        with open("{}-page-{}.html".format(self.tieba_name,page_num), "wb") as f:
            f.write(file_name)
            print("第%s页下载完成" % page_num)


    def run(self): # 实现主要逻辑
        # 构造url列表
        url_list = self.get_url_list()
        # 遍历列表,发送请求,获取响应
        for url in url_list:
            file_name = self.request_parse_url(url)
            # 保存
            self.save_file(file_name, page_num=(url_list.index(url)+1))

if __name__ == '__main__':
    tieba_name = input("请输入要贴吧名字:")
    tieba_spider = TiebaSpider(tieba_name)
    tieba_spider.run()
