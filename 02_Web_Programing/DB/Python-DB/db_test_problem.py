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


## 1
SQL = "select name from tb_user"

with db_connect() as conn:
    with conn.cursor() as cursor:
        cursor.execute(SQL)
        results = cursor.fetchall()
        print(results)

## 2
SQL = "select title,content from tb_board"

with db_connect() as conn:
    with conn.cursor() as cursor:
        cursor.execute(SQL)
        results = cursor.fetchall()
        print(results)

## 3
SQL = """select 'user'.id, 'user'.name, board.title, board.content 
from tb_user as 'user' inner join tb_board as board on 'user'.id=board.user_id 
where 'user'.id = 3 """

with db_connect() as conn:
    with conn.cursor() as cursor:
        cursor.execute(SQL)
        results = cursor.fetchall()
        print(results)
