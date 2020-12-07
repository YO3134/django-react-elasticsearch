from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializers):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "price",
            "publisher_name",
            "description",
            "isbn",
            "stock_status",
            "out_of_stock_flag",
        )
