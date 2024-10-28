import psycopg2
import psycopg2
import db.pgsql_query as postgresql_qurey
import db.mysql_query as mysql_query
import mysql.connector  # MySQL Connector 추가


from sqlalchemy import create_engine
from settings import DB_SETTINGS



class DBconnector:
    def __init__(self, engine, orm_engine, host, database, user, password, port):
        self.engine = engine
        self.orm_engine = orm_engine
        self.conn_params = dict(
            host = host,
            dbname = database,
            user = user,
            password = password,
            port = port

        )
        self.orm_conn_params = f"{orm_engine}://{user}:{password}@{host}:{port}/{database}"
        self.orm_connect()

        if self.engine == 'postgresql':
            self.connect = self.postgres_connect()
            self.queries = postgresql_qurey.queries

        elif self.engine == 'mysql':
            self.connect = self.mysql_connect()
            self.queries = mysql_query.queries

        # elif self.engine == 'mysql': ...

    def __enter__ (self):
        print("Enter")
        return self
    
    def __exit__(self, exe_type, exe_value, traceback):
        self.conn.close()
        print("Exit")


    def orm_connect(self):
        self.orm_conn = create_engine(self.orm_conn_params)

    def postgres_connect(self):
        self.conn = psycopg2.connect(**self.conn_params)
        return self
    
    def mysql_connect(self):
        self.conn = mysql.connector.connect(
            host=self.conn_params['host'],
            user=self.conn_params['user'],
            password=self.conn_params['password'],
            database=self.conn_params['dbname'],
            port=self.conn_params['port']
        )
        return self
    
    def get_query(self, table_name):
        try:
            _query = self.queries[table_name]
            return _query
        except KeyError:
            raise KeyError(f"'{table_name}' 키가 queries 에 존재하지 않습니다. 현재 있는 키 리스트 : {list(self.queries.keys)}")