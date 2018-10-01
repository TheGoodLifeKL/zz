# coding:utf-8
from pymysql import connect
from datetime import datetime
from multiprocessing import Process,Queue,Manager
import os
import time

class Rt():
    def __init__(self):
        self.conn = connect(host='127.0.0.1', port=3306, user='root', password='mysql', database='ruantong',charset='utf8')
        self.cs = self.conn.cursor()
        self.q = Manager().Queue()
    def get_teacher_id(self):
        # self.cs = self.conn.cursor()
        self.cs.execute('select id,teacher_id from student')
        tup = self.cs.fetchall()
        self.conn.commit()
        self.cs.close()
        self.conn.close()
        print(list(tup))
        # 返回一个列表,每个元素为(id,teacher_id)
        return list(tup)
        # for i in tup:

    def insert_2_teacher_note(self,teacher_name,now_time):
        # self.cs = self.conn.cursor()
        print(now_time)
        values1 = {"teacher_name":teacher_name,"now_time":now_time}
        print(values1)
        self.cs.execute('insert into teacher values(0,%(teacher_name)s,%(now_time)s)',values1)
        self.cs.execute('select max(id) from teacher')
        t_id = self.cs.fetchone()[0]
        self.conn.commit()
        # self.cs.close()
        # self.conn.close()
        return t_id

    def update_teacher_id(self,tup,t_id):
        print("*"*20)
        print(os.getpid())
        # self.q.put(i)
        student_id,teacher_id = tup[0],tup[1]
        # student_id,teacher_id = student_id,teacher_id
        if teacher_id == 0:
            self.cs = self.conn.cursor()
            values2 = {"t_id":t_id,"student_id":student_id}
            self.cs.execute('update student set teacher_id=%(t_id)s where id=%(student_id)s',values2)
            conn.commit()
            # self.cs.close()
            # self.conn.close()

    def run(self):
        now_time = datetime.now()
        teacher_name = input("请输入老师名字:")
        t_id = self.insert_2_teacher_note(teacher_name,now_time)
        li = self.get_teacher_id()
        print("*"*20)
        q = Queue()
        for i in li:
            q.put(i)
        try:
            tup = q.get()
            p1 = Process(target=rt.update_teacher_id,args=(tup,t_id))
            p2 = Process(target=rt.update_teacher_id,args=(tup,t_id))
            p1.start()
            p2.start()
            # self.update_teacher_id(tup1,t_id)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    rt = Rt()
    rt.run()


