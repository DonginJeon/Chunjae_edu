import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/catalog/books"
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')
# class이름: row > class: col-sm-10 > ul 태그
# 데이터가 안나올땐 한칸씩 위로
ul = soup.select(".row > .col-sm-10 > ul")[0]

# ul > li 찾기
li = ul.select("li")
for tag in li:
    print(tag.text.strip())
    