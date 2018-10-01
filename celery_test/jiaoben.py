# coding:utf-8
import time
from tasks import add,test_status
import sys

# result = add.delay(11,11)
#
# while not result.ready():
#     time.sleep(1)
# print("task done:{}".format(result.get()))

def pm(body):
    res = body.get("result")
    if body.get("status") == "PROGRESS":
        sys.stdout.write('\r任务进度:{}%'.format(res.get("p")))
        sys.stdout.flush()
    else:
        print("\r")
        print(res,"*"*10)
r = test_status.delay()
print(r.get(on_message=pm,propagate=False))