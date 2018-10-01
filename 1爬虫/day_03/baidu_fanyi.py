# coding:utf-8
import requests,json,sys

class BaiduFanyi:
    def __init__(self,trans_str):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
        self.trans_str = trans_str
        self.post_url = "http://fanyi.baidu.com/basetrans"
        self.judge_language_url = "http://fanyi.baidu.com/langdetect"

    def parse_url(self,url,data):
        response = requests.post(url,data=data,headers=self.headers)
        return json.loads(response.content.decode())

    def get_ret(self,dict_response):
        ret = dict_response["trans"][0]["dst"]
        print("Translate result is",ret)

    def run(self):
        # 获取用户输入的语言类型
        judge_lan_data = {"query":self.trans_str}
        lang = self.parse_url(self.judge_language_url,judge_lan_data)["lan"]
        # 准备post的数据
        trans_data = {"query":self.trans_str,"from":"zh","to":"en"} if lang == "zh" else {"query":self.trans_str,"from":"en","to":"zh"}
        # 发送请求,获取响应
        dict_repsonse = self.parse_url(self.post_url,trans_data)
        # 获取翻译的结果
        self.get_ret(dict_repsonse)

if __name__ == '__main__':
    trans_str = sys.argv[1]
    baidu_fanyi = BaiduFanyi(trans_str)
    baidu_fanyi.run()
