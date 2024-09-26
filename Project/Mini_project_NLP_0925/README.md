# FILES

- main.py : 문제 생성 파일입니다. 실행을 하시면 문제가 생성됩니다.
- data.py : 문제에 사용될 텍스트가 모여있는 파일입니다.
- manage.py : 관리자가 텍스트를 추가하는 파일입니다. 직접 입력, 폴더에 넣은 채로 추가하는 2가지 방식으로 구성하였습니다.
- question_model.py : 모델 코드입니다.
- quiz_brain.py : 생성에 필요한 함수가 구현되어 있는 파일입니다.
- README.md : 설명 파일입니다.
- test.ipynb : 저장된 DB를 조회할 수 있는 코드입니다. 실행하면 DB 내용을 볼 수 있습니다.

# Introduction

- konlpy가 설치되어 있어야 원활하게 코드가 작동합니다.

  - [설치링크](https://konlpy.org/ko/latest/install/)

- 실행 시 터미널 경로를 해당 파일들이 들어있는 폴더로 해주세요

- main.py을 실행하면 이름, 학년을 입력하고 난이도를 지정하면 문제가 제시됩니다. 총 10문제가 출제되고 다 풀면 프로그램이 종료됩니다. 문제를 푼 기록은 DB에 저장됩니다. 관리자는 manage.py를 통해 데이터를 직접 입력할 수도 있고 대량의 데이터를 텍스트 파일에 저장하여 추가할 수 있습니다.(텍스트 파일로 저장시 온점 단위로 한 문장씩 인식하여 저장됩니다.)

- 정답은 품사를 포함해서 명사입니다. 명사요 등으로 작성해도 가능합니다. 품사는 오타가 나면 오답으로 처리됩니다.

- 문제를 다 해결하면 틀렸던 품사에 대한 설명이 나옵니다.

# quiz_logs Table Schema

| Column Name    | Python Data Type | Description                              |
| -------------- | ---------------- | ---------------------------------------- |
| id             | `int`            | Primary key, auto-incrementing           |
| user_id        | `str`            | 학생이름 - 학년 (e.g., "전동인 - 3학년") |
| question_text  | `str`            | 문제 텍스트                              |
| user_answer    | `str`            | 학생이 선택한 답                         |
| correct_answer | `str`            | 실제 정답                                |
| is_correct     | `bool`           | 정오답여부 (정답 - 1, 오답 - 0)          |
| time_taken     | `float`          | 소요된 시간 (초단위)                     |
| solved_at      | `datetime`       | 응답이 완료된 시간                       |
