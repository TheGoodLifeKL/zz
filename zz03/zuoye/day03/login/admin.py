from django.contrib import admin
from login.models import UserInfo
# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['usename','password']
    def __str__(self):
        return
admin.site.register(UserInfo)