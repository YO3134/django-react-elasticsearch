from django.db import models


class Book(models.Model):
    # 暫定DB　
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    price = models.IntegerField(null=True, blank=True)
    publisher_name = models.CharField(max_length=120)
    description = models.TextField()
    isbn =　models.TextField()
    stock_status = models.IntegerField()
    out_of_stock_flag = models.IntegerField()
    

    def _str_(self):
        return self.title
