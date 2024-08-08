import pymysql
from insert_test import db_connect


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
def get_user_by_id(id: int):
    SQL = """
        SELECT 
            `user`.id, `user`.login_id, `user`.name,
            board.title, board.content
        FROM
            tb_user `user`
            INNER JOIN tb_board board ON `user`.id = board.user_id
        WHERE 1 = 1
            AND `user`.id = %s 
        """

    with db_connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(SQL, id)
            results = cursor.fetchall()
            print(results)


get_user_by_id(3)


## 4
def insert_board(title: str, content: str, user_id: int):
    SQL = """
        insert into tb_board(
            title,content,user_id
        ) values (
            %s, %s, %s
        )
"""
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(SQL, [title, content, user_id])
            conn.commit()


insert_board("파이썬-데이터베이스", "파이썬과 데이터베이스를 연동", 2)


## 5
def update_board(title: str, content: str, id: int):
    SQL = """
        update tb_board set
            title = %s,
            content = %s
        where 1=1
            and id = %s
    """
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(SQL, (title, content, id))
            conn.commit()


## 6
def delete_board(id: int):
    SQL = """
        delete from tb_board where id = %s
"""
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute(SQL, id)
            conn.commit()
