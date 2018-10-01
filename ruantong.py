# coding:utf-8
import datetime
from multiprocessing import Pool,Process,Queue
from pymysql import connect
import os

q = Queue()
class Rt():
    def __init__(self):
        conn = connect(host='127.0.0.1', port=3306, user='root', password='mysql', database='ruantong',charset='utf8')

    def get_teacher_id():
        #获取Cursor对象
        cs1 = conn.cursor()
        # 插入记录
        values1 = {"teacher_name":teacher_name,"now_time":now_time}
        cs1.execute('insert into teacher values(0,%(teacher_name)s,%(now_time)s)',values1)
        cs1.execute('select max(id) from teacher')
        # print(cs1.fetchone()[0])
        t_id = cs1.fetchone()[0]
        print(t_id)
        return t_id


    def update_stu__teacher_id(teacher_name,now_time,student_name):
        # 创建数据库连接
            cs2 = conn.cursor()
            values2 = {"teacher_id":t_id,"student_name":student_name}
            cs2.execute('select teacher_id from student where name = %(student_name)s',values2)
            if cs2.fetchone():
                # teacher_id = cs2.fetchone()[0]
                teacher_id_list = cs2.fetchall()
            # print(teacher_id)
                for i in teacher_id_list:
                    if i == 0:
                        cs2.execute('update student set teacher_id=%(teacher_id)s where name = %(student_name)s',values2)
            conn.commit()
            cs1.close()
            conn.close()

if __name__ == '__main__':
    now_time = datetime.datetime.now()
    teacher_name = input("输入老师姓名:")
    student_name = input("请输入学生名:")
    p = Pool(3)
    while True:
        p.apply_async(proc,args=(teacher_name,now_time,student_name))
    # p1 = Process(target=proc,args=(teacher_name,now_time,student_name))
    # p1.start()
    # p2 = Process(target=proc,args=(teacher_name,now_time,student_name))
    # p2.start()


