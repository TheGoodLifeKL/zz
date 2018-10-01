from django.db import models

# Create your models here.

class AreaInfo(models.Model):
    # 地区名称
    atitle = models.CharField(verbose_name='标题',max_length=20)
    # 关系属性
    aparent = models.ForeignKey('self',null=True,blank=True)

    def __str__(self):
        return self.atitle

    def title(self):
        return self.atitle

    title.admin_order_field = 'atitle'
    title.short_description = '地区名称'

    def parent(self):
        if self.aparent is None:
            return ''
        return self.aparent.atitle
    parent.short_description = '父级地区'