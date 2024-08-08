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

* **0730~0801**
  데이터분석 팀 프로젝트

  - 새롭게 습득한 기술
    데이터맵핑
    반복문을 통한 딕셔너리 생성
    마크다운 문법

* **0725**

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
