import time 
#from collections import Iterator
#from collections import Iterable
class Classmate():
    def __init__(self):
        self.names = list()
        self.current_num = 0
    def add(self, name):
        self.names.append(name)
    def __iter__(self):
        return self 
    def __next__(self):
        if self.current_num < len(self.names):
            result = self.names[self.current_num]
            self.current_num += 1
            return result
        else:
            raise StopIteration
classmate = Classmate()
classmate.add("老王")
classmate.add("老李")
classmate.add("老赵")
#print("判读classmate是否是可以迭代的对象:", isinstance(classmate, Iterable))
#classmate_iterator = iter(classmate)
#print("判读classmate_iterator是否是一个迭代器:", isinstance(classmate_iterator, Iterator))
#iter(classmate)
#print(next(classmate_iterator))
for s in classmate:
    print(s)
    time.sleep(1)
