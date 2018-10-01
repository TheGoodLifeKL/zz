from django.contrib import admin
from bookapp.models import BookInfo
# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','book_name','bpub_date']


admin.site.register(BookInfo,BookInfoAdmin)