import os
import dotenv


env_path = dotenv.find_dotenv()
dotenv.load_dotenv(env_path)

TEMP_PATH = "c:\\Users\\user\\Desktop\\Memo\\1028\\천재교육\\DAY2\\temp_storage"

DB_SETTINGS = {
    "POSTGRES": {
        'engine' : os.getenv("POSTGRES_ENGINE"),
        'orm_engine' : os.getenv("POSTGRES_ENGINE"),
        'host': os.getenv("POSTGRES_HOST"),
        'database': os.getenv("POSTGRES_DB"),
        'user': os.getenv("POSTGRES_USER"),
        'password': os.getenv("POSTGRES_PASSWORD"),
        'port': os.getenv("POSTGRES_PORT")
    },
    ""
    "KDT9": {
        'engine' : os.getenv("POSTGRES_ENGINE"),
        'orm_engine' : os.getenv("POSTGRES_ENGINE"),
        'host': os.getenv("POSTGRES_HOST"),
        'database': os.getenv("POSTGRES_DB_2"),
        'user': os.getenv("POSTGRES_USER"),
        'password': os.getenv("POSTGRES_PASSWORD"),
        'port': os.getenv("POSTGRES_PORT")
    }
}