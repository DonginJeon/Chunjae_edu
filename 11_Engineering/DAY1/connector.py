import psycopg2

class DBConnector:
    def __init__(self, host, database, user, password, port):
        print("Start DBConnector!")
        self.conn_params = dict(
            host = host,
            dbname = database,
            user = user,
            password = password,
            port = port
        )
        self.connect = self.postgres_connect()

    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()
        print("Exit")

    def postgres_connect(self):
        self.conn = psycopg2.connect(**self.conn_params)
        return self