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

books = []


class ReadRakutenAPI:
    def api_connect():
        while True:
            response = requests.get(URL, params=payload)
            data = json.loads(response.text)
            books.extend(data["Items"])
            if data["pageCount"] == data["page"]:
                break
            payload["page"] = data["page"] + 1
            time.sleep(1)

            with open("rakuten_book_json", "w") as f:
                json.dump(books, f)
