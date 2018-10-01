from django.db import models
# 设计和表对应的类,模型类
# Create your models here.

# 一类
# 图书类
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    def __str__(self):
        return self.btitle
# 英雄人物类
# 英雄名
# 性别
# 年龄
# 备注
# 关系属性
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    # BooleanField
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=128)
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        return self.hname

