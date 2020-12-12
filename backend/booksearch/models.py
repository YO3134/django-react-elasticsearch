from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=180, elp_text="本のジャンルを入力してください(SF,時代小説,古典,ファッション)"
    )


def _str_(self):
    return self.name


class Book(models.Model):
    # 暫定DB
    class Meta:
        db_table = "book"
        ordering = ["title", "author"]

    title = models.CharField(max_length=225)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(null=True, blank=True)
    publisher_name = models.CharField(max_length=120)
    isbn = models.CharField("ISBN", max_lenght=13, unique=True)
    genre = models.ManyToManyField(Genre, help_text="この本のジャンルを選択してください")
    description = models.TextField()
    stock_status = models.IntegerField()
    out_of_stock_flag = models.IntegerField()

    def _str_(self):
        return self.title
