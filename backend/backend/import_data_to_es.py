from elasticsearch import Elasticsearch
import local_settings
import json

esPass = local_settings.ES_PASS

with open("rakuten_books.json", "r") as f:
    rakuten_books = json.load(f)

es = Elasticsearch(http_auth=("elastic", format(esPass)))

for rakuten_book in rakuten_books:
    rakuten_book_item = rakuten_book["Item"]
    try:
        es.create(index="book", id=rakuten_book_item["isbn"], body=rakuten_book_item)
    except:
        pass
    print("{} created".format(rakuten_book_item["title"]))
