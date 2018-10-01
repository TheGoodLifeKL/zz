from django.contrib import admin
from booktest.models import AreaInfo
# Register your models here.

class AreaInfoAdmin(admin.ModelAdmin):
    list_per_page = 10 # 指定每页显示10条数据
    list_display = ['id','atitle','title','parent']
    actions_on_bottom = True
    actions_on_top = False
    list_filter = ['atitle'] # 列表页右侧过滤栏
    search_fields = ['atitle'] # 搜索框

    fields = ['aparent','atitle']

admin.site.register(AreaInfo,AreaInfoAdmin)