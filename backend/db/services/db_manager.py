import pymysql
from .consts import *
from ..queries.insert_queries import *
from ..queries.select_queries import *


class DB_Manager:
    def __init__(self, host, user, passward, db):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=passward,
            db=db,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )

    def execute_insert(self, query, params):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
        except Exception as e:
            print(e)

# to add params
    def execute_select(self, query):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)

    # def create_tables(self):
    #     with open('backend\db\create_tables_queries.sql', 'r') as f:
    #         sqlFile = f.read()
    #     sqlCommands = sqlFile.split(';')
    #     with self.connection.cursor() as cursor:
    #         for command in sqlCommands:
    #             try:
    #                 cursor.execute(command)
    #             except Exception as e:
    #                 pass

    def get_tickets_by(self, category, tags):
        if category and tags:
            with self.connection.cursor() as cursor:
                cursor.execute(SELECT_TICKETS_BY_CATEGORY_AND_TAGS)
                return cursor.fetchall()
        elif category:
            with self.connection.cursor() as cursor:
                cursor.execute(SELECT_TICKETS_BY_CATEGORY)
                return cursor.fetchall()
        elif tags:
            with self.connection.cursor() as cursor:
                cursor.execute(SELECT_TICKETS_BY_TAGS)
                return cursor.fetchall()
        else:
            with self.connection.cursor() as cursor:
                cursor.execute(SELECT_ALL_TICKETS)
                return cursor.fetchall()


db_manager = DB_Manager(HOST, USER, PWD, DB_NAME)
