import local_settings
import requests
import json
import time

URL = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?[parameter]=[value]…"
appID = local_settings.APPLICATION_ID


payload = {
    "fornmat": "json",
    "applicationID": format(appID),
    "bookGenreID": "000",
    "keyword": "Django",
    "page": "1",
}

print(payload)
