# coding:utf-8
# 4.将 [{1:'a'},{2:'b'}]转换为 [{'value':'a','key':1},{'value':'b','key':2}]

d = [{1:'a'},{2:'b'}]
d2 = []
for i in d:
    for key in i:
        dict = {'value':i[key],'key':key}
        print(dict)
        d2.append(dict)
print(d2)
