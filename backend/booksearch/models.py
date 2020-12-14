from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=180, help_text="本のジャンルを入力してください(SF,時代小説,古典,ファッション等)"
    )

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=200, help_text="本の言語を決定します。(日本語、英語等)")

    def __str__(self):
        return self.name


class Book(models.Model):
    # 暫定DB
    class Meta:
        # テーブル名
        db_table = "book"
        # テーブル項目
        ordering = ["title", "author"]

    title = models.CharField(max_length=225)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(null=True, blank=True)
    publisher_name = models.CharField(max_length=120)
    isbn = models.CharField("ISBN", max_length=13, unique=True)
    genre = models.ManyToManyField(Genre, help_text="この本のジャンルを選択してください")
    description = models.TextField()
    stock_status = models.IntegerField()
    out_of_stock_flag = models.IntegerField()

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField("died", null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    book_id = models.ForeignKey(
        to=Book, related_name="comments", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.text
