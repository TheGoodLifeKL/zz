# -*- coding: utf-8 -*-
import scrapy
import re


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/966840529/profile']


    def start_requests(self):
        cookies = "anonymid=jjcjgwl5-tsdem5; _r01_=1; depovince=GW; _de=CC6BB63D520808F7ADC07AF1BE8330E8; ln_uact=17549219730; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=7d78f7e7-69ce-46a5-b891-e45a5e08d580%7C80a5b5330e5a963e2203047a306ce0b9%7C1532525239158%7C1%7C1532525241563; jebecookies=9b1b79de-d8ab-4ca3-97ee-ac58e1cbba99|||||; JSESSIONID=abcp2ux0dODX4diq8vwtw; ick_login=27195dfc-da0c-409b-9c67-cc8bbe3f246f; p=d62852f7636ba5c5e24dd9150496405f9; first_login_flag=1; t=b0eea4f2a825a859c100b8e74f9ee5e59; societyguester=b0eea4f2a825a859c100b8e74f9ee5e59; id=966840529; xnsid=29a8276e; loginfrom=syshome; wp_fold=0"
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(re.findall("新用户",response.body.decode()))
