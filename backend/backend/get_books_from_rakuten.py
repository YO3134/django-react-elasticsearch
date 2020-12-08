import requests
import json
import time

URL = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?[parameter]=[value]…
"

payload = {
    'fornmat' : 'json',
    'applicationID' : 'XXXXXXXXXXX',
    'bookGenreID' : '000',
    'keyword' : 'Django',
    'page' : '1',
}

books = []

