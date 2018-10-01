# coding:utf-8

import requests

response = requests.get('https://ss0.baidu.com/7Po3dSag_xI4khGko9WTAnF6hhy/image/h%3D300/sign=45e1c8e71ddfa9ece22e501752d1f754/342ac65c103853434cc02dda9f13b07eca80883a.jpg')

with open('1.jpg','wb') as f:
    f.write(response.content)
