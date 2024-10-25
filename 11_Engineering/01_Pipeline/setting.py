DB_SETTING = {
    "POSTGRES": {
        "host": os.getenv("POSTGRES_HOST"),
        "database": os.getenv("POSTGRES_DB"),
        "user": os.getenv("POSTGRES_USER"),
        "port": os.getenv("POSTGRES_port"),
        "password": os.getenv("POSTGRES_PASSWORD"),
    },
    KDT_9 : {
        "host": os.getenv("POSTGRES_HOST"),
        "database": os.getenv("POSTGRES_DB_2"),
        "user": os.getenv("POSTGRES_USER"),
        "port": os.getenv("POSTGRES_port"),
        "password": os.getenv("POSTGRES_PASSWORD"),
    }
}