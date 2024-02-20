from mysql.connector import connect
from os import environ

db_connection = connect(
    host=environ.get("MYSQL_HOST", "mysql"),
    user=environ.get("MYSQL_USERNAME", "robi"),
    password=environ.get("MYSQL_PASSWORD", "test"),
    database=environ.get("MYSQL_DATABASE", "pancake"),
    port=int(environ.get("MYSQL_PORT", "3306"))
)

