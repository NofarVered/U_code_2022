import pymysql
import sys
from consts.consts import *

connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )

def create_db(db_name):
    try:
        global connection
        with connection.cursor() as cursor:
            query = 'CREATE DATABASE ' + db_name
            cursor.execute(query)
            connection.commit()
    except pymysql.Error as e:
        print(e.args[1], file=sys.stderr)

# create_db(DB_NAME)