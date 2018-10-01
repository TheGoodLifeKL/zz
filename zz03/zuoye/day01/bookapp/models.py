from django.db import models

# Create your models here.
class BookInfo(models.Model):
    book_name = models.CharField(max_length=20)
    bpub_date = models.DateField()

    def __str__(self):
        return self.book_name
