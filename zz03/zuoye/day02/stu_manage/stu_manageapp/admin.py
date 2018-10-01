from django.contrib import admin
from stu_manageapp.models import ClassInfo,StudentInfo
# Register your models here.
class ClassInfoAdmin(admin.ModelAdmin):

    list_display = ['class_name','student_count','class_num']


class StudentInfoAdmin(admin.ModelAdmin):

    list_display = ['stu_name','stu_gender','stu_age','stu_class']

admin.site.register(ClassInfo)
admin.site.register(StudentInfo)
