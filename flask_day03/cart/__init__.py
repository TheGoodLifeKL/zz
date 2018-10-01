# coding:utf-8

from flask import Blueprint

app_cart = Blueprint('app_cart',__name__,template_folder='templates')

# 在init文件被执行时,把视图加载进来,让程序知道视图的存在
from .views import get_cart