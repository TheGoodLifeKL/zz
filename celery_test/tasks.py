# coding:utf-8

from celery import Celery,Task
import time
class MyTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print("task done:{}".format(retval))
        return super(MyTask,self).on_success(retval,task_id,args,kwargs)
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print("task fail,reason:{}".format(exc))
        return super(MyTask,self).on_success(exc,task_id,args,kwargs)

app = Celery("tasks",backend="redis://127.0.0.1:6379/0",broker="redis://127.0.0.1:6379/0")

app.config_from_object("celery_config")

@app.task(base=MyTask)
def add(x,y):
    return x*y

@app.task(bind=True)
def test_status(self):
    for i in range(1,11):
        time.sleep(0.1)
        self.update_state(state="PROGRESS",meta={"p":i*10})
    return "finish"

@app.task(bind=True)
def period_task(self):
    print("period task done:{}".format(self.request.id))
