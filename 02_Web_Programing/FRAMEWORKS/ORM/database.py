import pymysql
from sqlalchemy import create_engine,select
from sqlalchemy.orm import Session
from db_config import PORT, HOST, USER, PASSWORD
from model import User

pymysql.install_as_MySQLdb()
engine = create_engine(f"mariadb+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/test_db?charset=utf8mb4")
session = Session(engine)


# 실제 ORM 작성법입니다.
# 이 문장은 Database statement를 반환합니다. > 쿼리정보
stmt = select(User).where(User.login_id=="user2")

# fetchall과 같은 함수
users = session.scalars(stmt)
for user in users:
    print(user.id,user.login_id,user.login_password)










