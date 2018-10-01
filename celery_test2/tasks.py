# coding:utf-8
# from celery import Celery
#
# app = Celery("tasks",backend=backend,
#              broker=broker
#              )
from celery1 import app
import datetime
@app.task
def add(x,y):
    return x + y
@app.task
def pop(x,y):
    return x - y

@app.task
def now_time(x,y):
    return x * y
