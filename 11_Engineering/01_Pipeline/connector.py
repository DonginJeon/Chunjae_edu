class DBConnector:
    def __init__(self, host, database, user, password, port):
        print("Start Class")
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connect = self.postgres_connect()

    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self,exc_type, exc_value, traceback):
        self.conn.close()
        print("Exit")

    def postgres_connect(self):
        self.conn = psycopg2.connect(
                                        host = self.host, \
                                        dbname = self.database, \
                                        user = self.user, \
                                        password = self.password, \
                                        port = self.port

                                    )
        
        return self