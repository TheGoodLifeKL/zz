# coding:utf-8

from multiprocessing import Process
import os 
import time 

def run_proc():
    """子进程要运行的代码"""
    print("子进程运行中,pid=%d..." % os.getpid())
    print("子进程将要结束...")

if __name__ == "__main__":
    print("父进程pid:%d..." % os.getpid())
    p = Process(target=run_proc)
    p.start()


