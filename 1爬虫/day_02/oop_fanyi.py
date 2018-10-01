# coding:utf-8
import requests,json,sys

class Translate:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
        self.query_string = sys.argv[1]
        self.post_url = "http://fanyi.baidu.com/basetrans"
        self.judge_language_url = "http://fanyi.baidu.com/langdetect"

    def get_judge_language_data(self):
        judge_data = {"query":self.query_string}
        judge_response = requests.post(self.judge_language_url, data=judge_data, headers=self.headers)
        judge_ret_dict = json.loads(judge_response.content.decode())
        judge_ret = judge_ret_dict["lan"]
        return judge_ret


    def get_response_data(self,language_type):
        if language_type == 'en':
            response_data = {
                "query":self.query_string,
                "from":"en",
                "to":"zh"
            }
        else:
            response_data = {
                "query":self.query_string,
                "from":"zh",
                "to":"en",
            }
        return response_data

    def get_result(self,response):
        ret_dict = json.loads(response.content.decode())
        return ret_dict["trans"][0]["dst"]

    def run(self):
        # 获取用户输入语言类型
        language_type = self.get_judge_language_data()
        print("language_type is",language_type)
        # 根据语言类型,进行判断,获得请求数据data
        data= self.get_response_data(language_type)
        print(data)
        # 发送请求,获取响应
        response = requests.post(self.post_url, data=data, headers=self.headers)

        # 转换响应格式,获取最终结果
        ret = self.get_result(response)
        print("The translate result is:",ret)

if __name__ == '__main__':
    translate = Translate()
    translate.run()
