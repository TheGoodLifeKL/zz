from django.db import models

# Create your models here.
class ClassInfo(models.Model):
    class_name = models.CharField(max_length=20)
    stu_num = models.IntegerField()
    class_num = models.IntegerField()

    def __str__(self):
        return self.class_name

    class Meta:
        db_table = 'classinfo'

class StudentInfo(models.Model):
    stu_name = models.CharField(max_length=20)
    stu_gender = models.BooleanField(default=False)
    stu_age = models.IntegerField()
    stu_class = models.ForeignKey('ClassInfo')
    def __str__(self):
        return self.stu_name
    class Meta:
        db_table = 'studentinfo'