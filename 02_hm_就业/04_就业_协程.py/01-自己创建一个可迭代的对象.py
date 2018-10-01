from collections import Iterable
class Classmate():
    def __init__(self):
        self.names = list()
    def add(self, name):
        self.names.append(name)
    def __iter__(self):
        '''如果要让一个对象为可以迭代的对象(for),那么必须实现__iter__方法'''
        pass
classmate = Classmate()

classmate.add("xiaoli")
classmate.add("xiaowang")
classmate.add("xiaozhao")
for s in classmate:
    print(names)
    
