
def set_func(func):
    def add_func(a, b):
        
        print("乘积为:%d" % (a * b))
        return func(a, b)
    return add_func

@set_func   # cal = set_func(cal)
def cal(a, b):
    return a + b
print("和为:%d" % cal(11,22))
