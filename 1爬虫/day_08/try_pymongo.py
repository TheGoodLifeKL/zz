# coding:utf-8

from pymongo import MongoClient


# 实例化client,建立连接
client = MongoClient(host="127.0.0.1",port=27017)
# collection = client["test"]["c1"]
collection = client["test"]["t3"]

# ret = collection.insert({"name":"xiaokou","age":23})
# print(ret)

# 插入多条数据
# data_list = [{"name":"py{}".format(i),"_id":"{}".format(i)} for i in range(0,1000)]
# collection.insert(data_list)

# 查询一条数据
t = collection.find()
data_list = list(t)
data_list = [i for i in data_list if int(i["_id"])%100==0 and i["_id"]!=0]
print(data_list)
# 查询多条数据
# t = collection.find({"name":"xiaokou"})
# print(t)
#
# for i in t:
#     print(i)
#
# for j in t:
#     print(j,"*"*20)

