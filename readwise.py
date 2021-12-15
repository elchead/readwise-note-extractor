import requests
from decouple import config

token = config("TOKEN")

base_url = "https://readwise.io/api/v2/"


def create_book_highlights(notes, title, author, date):
    obj = lambda txt: {
        "text": txt,
        "title": title,
        "author": author,
        "highlighted_at": date,
        "source_type": "book",
    }
    return [obj(n) for n in notes]


def get_header():
    return {"Authorization": "Token " + token}


def can_auth():
    r = requests.get(base_url + "auth", headers=get_header())
    return r.status_code == 204


def save_highlights(obj_list):
    data = {"highlights": obj_list}
    r = requests.post(base_url + "highlights/", headers=get_header(), json=data)
    return r


def test_auth():
    assert can_auth()


def get_highlights():
    querystring = {}  # {"page_size": 1}
    response = requests.get(url=base_url + "highlights/", headers=get_header(), params=querystring)
    return response.json()
