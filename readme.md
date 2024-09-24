# **0924**

- matplotlib에서 한글 지원하는 방법 : pip install koreanize_matplotlib
- [수업필기]
- [인사이트](https://www.analyticsinsight.net/)
- 파이썬 pdf 불러오기
- [정규표현식](./06_NLP/02_Regular_Expression/attempt.ipynb) - import re
- 요즘은 자연어 처리나 수학적 통계적 수식을 바로 옮길 수 있는 코딩 기술
- [파이썬 추가공부 사이트](https://www.w3schools.com/python/python_regex.asp)

# **0911**

ffmpeg를 호출하는 문제가 있는데 파이썬 3.8의 가상환경을 만들어서 해보자

# **0910**

[수업필기](./05_Deep_Learning/Note/0910.md)

- vit
  - 이미지 분류모델을 만들때 만들던게 아쉬우면 vit를 선택해보자
- 함수를 통해 영수증 합계 구현 시도(지피티없이 성공!!)

  ```
  def total_pay():
    price = 0
    product = input("상품이름을 입력하세요, 여러개일 경우 ,로 구분해주세요")
    product = product.split(",")

    for pro in product:
        question = f"what is price of {pro}?"
        answer = pipe(image=document, question=question)
        a = answer[0].get("answer")
        a = float(a)
        price += a
  ```


    return price

```

> 데코레이터를 활용하는 것으로 개선해보자
- *arg, **kwargs


# **0906**

- ## Resnet
- [마크다운 표만들기](https://www.tablesgenerator.com/markdown_tables)

# **0905**

- [수업필기](./05_Deep_Learning/Note/0905.md)
- attention : 앞뒤 데이터의 관계를 추론하여 대답을 할때 고려
- [get_dumies](https://hongl.tistory.com/89)

# **0904**

- [수업필기](./05_Deep_Learning/Note/0904.md)
- mkdir : 파이썬에서 폴더생성하는 방법
- np.random.permutation(X) : 무작위로 X를 섞는 함수
- pd.cut
- scatter_matrix

# **0903**

- [수업필기](./05_Deep_Learning/Note/0903.md)
- 딥러닝 기초
- 실생활에서 딥러닝이 어떻게 쓰이는가

# **0902**

- 실루엣점수
- 실루엣 점수는 구분을 얼마나 명확하게 하는지에 대한 지표

# **0826**

- 표준화

- 로그변환 : 큰 쪽은 y값이 작아지고 작은 쪽은 커짐(왼쪽 치중이면 사용/오른쪽 꼬리가 길때)
- 지수변환 : 작은 값들 차이가 적게나고 큰값들 차이는 크게남(그래프의 길이를 조절해서 사용)
- standard scaler

- 데이터의 스케일에 따라 결과가 달라질 수 있음
- 범위 0~1 : -20~100 이면 min-max scaler를 사용하면 좋음

# **0823**

- [실습피드백](./Project/Mini_project_machinelearning_0822/Feedback.md)
- [보고서피드백](./Project/Mini_project_machinelearning_0822/REPORT_feedback.md)
- 피드백 해주신 부분 수정, 피어슨 상관계수를 통해 랜덤포레스트에서 유의미한 영향이 있다고 판단한 부분에 대하여

# **0822**

- 실습(만료및탈퇴회원)

- 특성확인/전처리/x,y데이터 선정/ 무엇을 분석할지
- 분석테마

  - 회원이 언제쯤 탈퇴할까?(오래있을 회원, 빨리 그만둘회원을 나누어 서비스를 다르게 제공가능)
  - 50일까지의 유저가 90일에 어떨지 예측하는 모델
  - 어떤 지표가 변경되었을때 만료가 되지 않는가(survival analysis)

* 컬럼
- 유저id : 회원의 개인정보가 노출되지 않게 문자로 바꾸어 제시(개인식별이 불가능한)
- gender : 성별
- 멤버타입\_코드네임 :
- grade_codename
- memberstatus : 44- 만료
- ./codename
- ./change

# **0821**

## 수업

- [수업필기](./03_Machine_learning/NOTE/0821.md)
- 분석을 하며 feature_importance를 확인한뒤 인사이트를 얻어보자
- 보고서 작성팁
- 구성
  - 요약
  - R&R
  - WBS
  - 서론 : 문제정의, 프로젝트 기획 의도, 기술현황 등을 제시
  - 개발 환경 : 사용된 라이브러리의 라이선스 정보 포함(파이썬 버젼, 운영체제 버젼, 라이선스 정보 등)
  - 기능 구현 : 구현된 기능의 시연 및 벤치마크 결과를 포함해 설명할 것(사실에 대한 정보만 적는 곳/의견X)
  - 산출물 : 입력에 따른 산출물 전반에 대한 설명을 포함할 것(앞선 사실에 이어 의견을 제시)
  - 개선점 : 현 시점에서의 프로그램 개선 가능성에 대해 서술
  - 소스코드 : 깃허브 레퍼지토리 첨부
  - 참고문헌 : 적절한 인용 양식에 따름

## 공부

- 각 모델별 나누는 방식에 대해 추가 공부를 해보고 유의미한 컬럼만 넣었을때 실제 성능차이가 나는지 확인해보자

# **0820**

## 수업

- [수업필기](./03_Machine_learning/NOTE/0820.md)
- ### 의사결정나무
- 반복문을 돌릴 때 전체를 zip()으로 묶어서 사용도 가능
- ### 당뇨병 실습
- 트레인이 1.0인데 테스트가 훨씬 낮으면 과적합의 확률이 높다
- y=y>a 라고 하면 y>a에서 나온 불린형이 y에 들어감. 즉 0,1로 바꾸지 않아도 됨

## 공부

- ### 0819 수업 복습
- randomforestclassifier
  - [Feature Selection](https://velog.io/@ssom_d/ML-Feature-Selection) : 필요없는 데이터를 줄이기 위한 방법/가지고 있는 특성 중에서 훈련에 가장 유용한 특성을 선택하는 것
  - 랜덤포레스트 파일 내의 추가 예제 [풀이](./03_Machine_learning/01_Random_forest/RNA.ipynb)
    - 콤마를 끊고 싶으면 split을 이용
    - list(set(리스트))를 하면 중복을 없앤 리스트로 만들어줌
    - 그냥 리스트에서 .index(원소이름)을 호출하면 원소의 번호를 출력해줌

# **0819**

## 수업

- ### 머신러닝 시작

- [수업필기](./03_Machine_learning/NOTE/0819.md)
- .T를 통해 행렬을 뒤집을 수 있음
- 넘파이 어레이로 바꾸면 더 빠름
- 클래스 초기화

```

class A:
**init**(self):

a = A()

```

- 데이터사이언스 추가 공부 [링크](https://datascienceschool.net/02%20mathematics/02.01%20%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%99%80%20%ED%96%89%EB%A0%AC.html)
- 표집에 대한 추가 공부

# **0818**

## 복습

- ### [데코레이터](https://kevinitcoding.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-%EC%89%AC%EC%9A%B4-%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0-%EC%9B%90%EB%A6%AC) 이해
- ### 할일
- 교육PC 내 데이터베이스 보고 오기

# **0815**

## 복습

- ### 숫자 맞추기 게임
- 그대로 입력하고 원리 이해
- ### 날씨 맞추기 프로그램

# **0814**

## 수업

- ### 장고 마무리

```

장고 정리
HTML(파일명까지 장고에서 제시하는대로 해야함), 요청, DB => 웹개발을 위한 필요한 모든 것을 가지고 있는 프레임워크, 유연하지 못하다는 것이 최대 단점
프레임워크 수업에서 배웠던 것, 장고, 플라스크에 대한 공부 뿐만 아니라 프레임워크 사용 전반에 대한 맛을 봄. 시키는 대로 해야함

```

```

장고 API
불러오기

```

```

웹 스크레이핑 -> 만들어둔 사이트를 활용
로그인이 필요한 사이트에서 로그인을 하고 스크레이핑 시도
특별한 보안으로 막힌 곳: 쿠키 같은 것. 주소를 정확히 치고 새로고침하거나 다시 들어가면 달라지니 잘 넣기

```

```

- 시험 정리

# HTML(뼈대) CSS() JS(기능)

    JS에서 fetch를 통해 데이터를 가져올 수 있음

```

# 웹 : 네트워크가 거미줄처럼 연결

  서버(컴퓨터)와 클라이언트(브라우저)의 관계가 중요함.
    클라이언트 -> 서버 : request
      1. method : GET POST UPDATE DELETE...
        GET과 POST의 차이 알기: GET은 URL로 다 해결, POST는 안에 body 데이터가 들어감
      2. param(url안에 들어간 식별자 값, ?)
      3. API
    서버 -> 클라이언트 : response
      1. status : 성공(200), 실패 - 유저(400), 서버(500)
      2. data, body: JSON,HTML,text

  * 프레임워크와 라이브러리 차이 알기
      프레임워크는 개발순서, 방법을 정해줌

# 프레임워크

  플라스크
    @(데코레이터)에 따라 움직임: 함수에 대한 라벨, 함수의 시작과 끝에 무언가 처리를 할 수 있음 => 함수를 제어하는 함수
    @app.route("/") -> url을 받아서 원하는 함수 실행

    -특징
    1. 경량
    2. 확장성
    => 처음 시작, 스타트업, 신기능에 많이 사용, 사수를 잘 만나야함

  장고
    -MVT - model: 비즈니스 로직을 가지는 세상에 있는 것을 추상화한 것,
          view: 모델과 템플릿을 연결하여 원하는 화면을 구성하는 것,
          template: UI

    -ORM => 객체(모델) 관계(DB) 맵핑(

    -명령어
      startproject
      createapp
      runserver
      migrate(makemigration, migrate)

    - 파일
      settings.py
      urls.py
      views.py
      admin.py
      template/HTML(템플릿 문법 들어감)

    - 특징
    1. 기업용
    2. all-in-one
    3. 크고 무겁다
    )

```

`

## 연휴 계획

```

- 0815
  웹 배웠던 거 복습

- 0816
  웹 복습 + 파이썬 예제 및 테스트 정리
- 0817
  유데미
- 0818

```

# **0813**

## 수업

- ### 장고 개발

```

- 아래의 터미널 명령어는 기억할 것.
  python manage.py runserver
  python .\manage.py makemigrations
  python .\manage.py migrate

```

[참고 사이트](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page)

# **0812**

## 수업

- ### ORM 설명 및 실습

```

1. SQL을 사용할 필요가 없어짐, 파이썬 코드로 데이터베이스를 간접적으로 핸들링
2. 쿼리에 대한 공부는 필요함

```

- ### 장고

```

1. 웹 앱을 만들기 위한 기업용 프레임워크
2. MVT라는 개념이 필요 => 면접 단골질문
3. manage.py가 반겨줌(장고를 핸들링할 수 있게 무언가를 주는 역할) => 앱도 만듬
4. admin 지원 - 모델을 선언하고 화면에 미치는 영향을 정의하고 그 모델로 admin환경을 만듦.

```

```

- 터미널에서 빠져나올땐 exit()
- 터미널 폴더로 들어가기 cd .\\
- 뒤로 가기 cd ../

```

```

conda install django

python - django --version => 장고 설치 확인

PS C:\Users\user\Desktop\Chunjae_edu> django-admin startproject mytestsite

PS C:\Users\user\Desktop\Chunjae_edu\02_Web_Programing\FRAMEWORKS\DJANGO\mytestsite>

PS C:\Users\user\Desktop\Chunjae_edu\02_Web_Programing\FRAMEWORKS\DJANGO\mytestsite> python manage.py runserver

cd ../

PS C:\Users\user\Desktop\Chunjae_edu\02_Web_Programing\FRAMEWORKS\DJANGO> django-admin startproject locallibrary

PS C:\Users\user\Desktop\Chunjae_edu\02_Web_Programing\FRAMEWORKS\DJANGO> cd .\locallibrary\

PS C:\Users\user\Desktop\Chunjae_edu\02_Web_Programing\FRAMEWORKS\DJANGO\locallibrary> python manage.py startapp catalog

PS C:\Users\user\Desktop\Chunjae_edu\02_Web_Programing\FRAMEWORKS\DJANGO\locallibrary> PS C:\Users\user\Desktop\Chunjae_edu> django-admin startproject mytestsite

```

```

로컬라이브러리의 세팅에서 데이터베이스 부분 마리아 디비로 바꾸기
models.py
urls.py

PS C:\Users\user\Desktop\Chunjae_edu\02_Web_Programing\FRAMEWORKS\DJANGO\locallibrary> python manage.py makemigrations => 이걸하면 적용이 됨

PS C:\Users\user\Desktop\Chunjae_edu\02_Web_Programing\FRAMEWORKS\DJANGO\locallibrary> python manage.py migrate = > 이거까지 해야 데이터베이스에 적용

```

```

admin에 정리

```

# **0809**

## 수업

- 데이터베이스에 있던 정보로 사이트 만들기

```

- 스테틱과 템플릿, 두개의 폴더 생성
  templates(끝에 s를 붙이는 것이 중요)
  static

```

- 정리

```

1. 만들땐 목록 먼저 만들자 - SQL을 활용해서
2. 게시판 목록(boards)을 만듦
   url_for - 함수 이름과 매개변수(kwarg)를 가지고 라우터 함수를 찾아서 라우터로 간다

```

# **0808**

## 할일

```

파이썬 필수템설치
unibeautify
장고
settings.json-> 사용자설정-> 슬랙 내용 붙여넣기
라이브 서버
마리아 디비
디비버
플라스크 설치

```

## 수업

- SQL 예제 정리
- 라이브러리 프레임워크 차이
- \*args, \*\*kwargs
- 데코레이터
- 플라스크
  - 기본적인 사용법(간단한 사이트 만들기)
  - 동적 라우팅
  - 깃에 올리기 전 사전 작업. => 다른 파일로 만들어서 사용하기
  - 예제 만들어보기(아이디 비번 입력.)

# **0807**

## 복습

- JS

  - 변수선언

    - var : 잘 안씀
    - let : 변수
    - const : 상수

  - IF문
  - For문
  - function
    function [이름]()

    const [이름] = function

                 = () =>

    변수 안에 들어갈 수 있음

  - [배열] -> list
    { } -> 데이터 딕셔너리

  - 웹에 주는 영향
    웹에는 다큐먼트(html 요소(dom)를 가지고 있음- 돔에 대한 접근을 할 수 있게 해줌)가 있음. -> 요즘은 queryselector로 대체됨

    요소 + contents

    - css

    - eventlisener

- API
  - 서버 -> 클라이언트
  - fetch("URL").then()

* SQL
  - DB를 관리하고 싶으면 DBMS(오라클, mysql)를 사용
  - 여러가지 문법
  - 조인
  - 외래키
  - 파이썬과 연결하여 사용
  - 오토인크리먼트 늘리기
  - 파이썬에서 수정하고 연동하기

# **0806**

## 수업

- API

  [postman](https://www.postman.com/)

  [insomnia](https://insomnia.rest/download)

  rest client 설치

  get을 통한 url 확인

  - 실습
    - 고양이 사이트 핸들링
    - 날씨어플 만들기

- 데이터베이스

  - 마리아 DB 설치 -> 집에서도 설치하기
  - 간단한 테이블 만들어보기

# **0805**

## 수업

- CSS
  개발(디자인)
- JS
  문법(연산)

  구구단

  변수 선언하는 방법
  let var const
  차이 비교

  IF문

  Switch ~ case문

  for문

  함수
  만드는법
  foreach
  map
  filter
  find, findindex
  join

  [array를 다루는 함수](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array)

  - 웹 개발
    사용자=>행동(마우스, 키보드)
    [event]
    이벤트가 일어났을때 어떤 일을 해야한다고 정해주는 것-listener,handler

  - 자바 실습(숫자맞추기)

# **0802**

## 수업

- 깃에 대한 첫 이해
- vscode에서 하던 것과는 다르게 깃배쉬를 통해 첫 실습
- 소스트리
- 깃 브렌치변경(생성)
- 깃 플로우
- 깃 허브 플로우
- 웹
  - 라이브 서버 설치
  - vscode에서 웹페이지 구성
  - HTML에 대한 이해
    - head, body
    - h1~h6
    - p
    - 하이퍼링크
    - [참고사이트](https://developer.mozilla.org/ko/docs/Learn/HTML)

# **0730~0801**

데이터분석 팀 프로젝트

- 새롭게 습득한 기술
  데이터맵핑
  반복문을 통한 딕셔너리 생성
  마크다운 문법

# **0725**

plotly

- 사용법
- scatter
- 특이그래프 - 3d scatter - sunburst - treemap - density
  fulium
- 지도 그리는법
- 마커찍는법
- 아이콘 바꾸는 법

부족한 부분

- 어떤 요소가 영향을 주는지 어떻게 그래프를 그려야하는지에 대한 경험 부족
- 판다스
  groupby
  sort value 등 함수에 대한 인식 부족
  filter에 대한 추가 학습 필요
  개선사항
- 판다스 테스트 와인 자료에 대한 분석 진행--> 결측치를 근거있게 대체해보자

- **0724**
  배운 내용(seaborn)
  - 히스토그램
  - KDE
  - rug
  - bar
  - count
  - box
  - violin
  - heatmap
  - pair
  - pie
  - seaborn 데이터를 활용한 시각화 실습

부족한 부분

- 옵션에 대한 숙지 미숙
  개선사항
- 각 차트가 언제 쓰이고 해석하는 경험 많이 쌓기

```

```

```

```
