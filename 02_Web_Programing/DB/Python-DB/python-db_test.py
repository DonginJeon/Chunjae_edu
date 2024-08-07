import pymysql


# DB 연결


def db_connect():
    conn = pymysql.connect(
        host="127.0.0.1",
        user="user",
        password="1234",
        db="test_db",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )

    return conn


# SQL 실행
SQL = "select * from tb_board"

## with 문 ~ close() 즉 자원 반환하는 문법이 필요한 경우,
## with 문을 사용하면 자동으로 close를 해준다.

with db_connect() as conn:
    with conn.cursor() as cursor:
        cursor.execute(SQL)
        results = cursor.fetchall()
        print(results)
