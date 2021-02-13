class DBConfig:
    SECRET_KEY = 'secret_key'
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "Barr1993"
    MYSQL_HOST = "localhost"
    MYSQL_DB = "browardreseller"
    MYSQL_CURSORCLASS = "DictCursor"


cacheConfig = {
    "DEBUG": False,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300
}