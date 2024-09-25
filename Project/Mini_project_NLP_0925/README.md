# Introduction

- main.py : 문제 생성 파일입니다. 실행을 하시면 문제가 생성됩니다.
- data.py : 문제에 사용될 텍스트가 모여있는 파일입니다.
- manage.py : 관리자가 텍스트를 추가하는 파일입니다. 직접 입력, 폴더에 넣은 채로 추가하는 2가지 방식으로 구성하였습니다.
- question_model.py : 모델 코드입니다.
- quiz_brain.py : 생성에 필요한 함수가 구현되어 있는 파일입니다.
- README.md : 설명 파일입니다.

# Guide

- main.py을 실행하면 이름, 학년을 입력하고 난이도를 지정하면 문제가 제시됩니다. 총 10문제가 출제되고 다 풀면 프로그램이 종료됩니다. 문제를 푼 기록은 DB에 저장됩니다. 관리자는 manage.py를 통해 데이터를 직접 입력할 수도 있고 대량의 데이터를 텍스트 파일에 저장하여 추가할 수 있습니다.

# quiz_logs Table Schema

| Column Name    | Python Data Type | Description                                                                        |
| -------------- | ---------------- | ---------------------------------------------------------------------------------- |
| id             | `int`            | Primary key, auto-incrementing                                                     |
| user_id        | `str`            | Identifier for the user (e.g., "전동인 - 3학년")                                   |
| question_text  | `str`            | The text of the question posed                                                     |
| user_answer    | `str`            | The answer provided by the user                                                    |
| correct_answer | `str`            | The correct answer for the question                                                |
| is_correct     | `bool`           | Indicates if the user's answer was correct (False for incorrect, True for correct) |
| time_taken     | `float`          | Time taken to answer the question (in seconds)                                     |
| solved_at      | `datetime`       | Timestamp of when the question was answered                                        |
