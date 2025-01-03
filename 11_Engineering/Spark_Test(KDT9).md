## Pyspark Dataset API 실습 과제

### 0. 사전 고지
- Dataset은 아래 다섯개 활용합니다. (dataset/data-02/ 폴더 아래에 있는 데이터 활용)
  - **member_dup.parquet**
  - **member.parquet**
    - idx : 학생 고유번호(중복X)
    - sex : 성별
    - status : 회원 상태
    - grade : 학년
  - **point_his.parquet**
    - idx : 학생 고유번호(중복X)
    - proc_ym : 이력 발생 년월
    - proc_ymd : 이력 발생 년월일
    - point : 획득 점수
    
  - **item_his.parquet**
    - idx : 학생 고유번호(중복X)
    - lv : 학생 레벨
    - proc_ym : 이력 발생 년월
    - proc_ymd : 이력 발생 년월일
    - codename : 아이템명
    - mascodename : 아이템 구분
    - price : 아이템 가격
  - **study_his.parquet**
    - idx : 학생 고유번호(중복X)
    - proc_ym : 이력 발생 년월
    - proc_ymd : 이력 발생 년월일
    - pointnm : 획득 포인트 이름
  - **regdate_his.parquet**
    - idx : 학생 고유번호(중복X)
    - regdate : 학생 등록일자
	

- 문제 중 `slicing 사용 X`은 문자열을 단순히 index로 끊어 추출하는 방식(slice, substring 등 다양한 함수가 존재할 수 있음)이 아닌 다른 방식을 사용해주시라는 뜻입니다.

### 1. 실습 문제

1. member 테이블에서 회원 상태별 인원수를 내림차순으로 보여주세요. (6)

2. study_his 테이블의 pointnm 컬럼에 대해 공백을 모두 없애주세요 (6)

3. point_his의 proc_ymd 컬럼의 날짜 표현 형식을 yyyy-mm-dd 형식이 되도록 바꿔주세요. (6)(UDF, slicing 사용 X)

4. member 회원상태(status)가 학습만료 회원들이 공부한 과목 리스트를 TOP3를 뽑아주세요 (8)

5. member_dup 테이블에 학년이 여러개인 idx가 있습니다. 해당 idx의 학년 중 가장 높은 학년만 남겨서 idx와 grade가 1:1 대응이 되도록 만들어주세요 (8)

6. regdate_his 등록일(reg_date)이 2023.03.15일인 유료회원들이 가장 많이 착용한 아이템(codename) TOP3를 뽑아주세요 (8)

7. member 테이블의 grade 컬럼에서 숫자만 뽑아 grade라는 컬럼을 재구성해주세요. (초3학년 -> 3) (8)  (UDF, slicing 사용 X)

8. study_his 월별로 pointnm 컬럼에 대한 point 발생 수(count)를 오름차순으로 순번 매겨주세요 (10)

9.  레벨이 151~160 에 있는 유저들 중 딱 한 명씩만 등록한 날짜들을 구해주세요. 
   레벨은 idx가 가진 레벨중 가장 높은 레벨로 사용(10) -> 중복처리에 유의

10. item_his 테이블에서 레벨이 null인 유저가 가장 많은 날짜를 구해주세요 (10)


11. pointnm 별로 획득한 point의 종류가 언더바(_)로 이어져서 보이도록 테이블을 만들어 주세요 (10)

    |pointnm|point종류|
    |---|---|
    |point_A|1_2_3_4_5|
    |point_B|1_4_5|


12. member의 status 컬럼에서 '회원'단어가 있으면 띄어쓰기하고 없으면 띄어쓰기 후 회원 단어 추가해주세요 (유료회원 -> 유효 회원  /  신규 -> 신규 회원) (10)
