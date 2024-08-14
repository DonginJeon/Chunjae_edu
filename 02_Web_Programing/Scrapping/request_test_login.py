import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/catalog/books"

session = requests.Session()

# session을 가져옵니다
with requests.Session() as session:
    form = {
        "username": "admin",
        "password": "12",
        "csrfmiddlewaretoken" : "vXwQnuCU9FczAtEXN6CAFzwslH233c90rcJiQtfhVkEm580hjWSuonT3izgZkKpa"
    }
    cookies = {
        "csrftoken":"6pnCD9NxWPCXFPwuG0q4TYxL72o6rIqk"
    }

    # 로그인
    response = session.post("http://127.0.0.1:8000/accounts/login/", data=form,cookies=cookies)
    # 페이지를 가져옴
    response = session.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    page = soup.select_one(".page-current > p")

    # page 1 of 2.을 가져옴
    # string을 잘라야함
    total_page = int(page.text.split("of")[1].strip()[0])

    print(total_page)
    # total 페이지 만큼 반복
    # D.D에 저장 [{name:"",author:""}]
    result = []
    for i in range(1, total_page + 1):
        # "http://127.0.0.1:8000/catalog/books/?page=1"
        books_res = session.get(URL, params={"page": i})
        books_html = BeautifulSoup(books_res.text, "html.parser")
        li_list = books_html.select("div.col-sm-10 > ul > li")
        for li in li_list:
       
       
            # str 자르고... 나누고...
            books = li.text.strip().split("\n")
            result.append({"name": books[0].strip(),"author": books[1].strip()})

    print(result)



# response = requests.get(URL)

# soup = BeautifulSoup(response.text, 'html.parser')
# # class이름: row > class: col-sm-10 > ul 태그
# # 데이터가 안나올땐 한칸씩 위로
# ul = soup.select(".row > .col-sm-10 > ul")[0]

# # ul > li 찾기
# li = ul.select("li")
# for tag in li:
#     print(tag.text.strip())
    