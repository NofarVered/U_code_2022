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

    def create_tables(self):
        with open('backend\db\create_tables_queries.sql', 'r') as f:
            sqlFile = f.read()
        sqlCommands = sqlFile.split(';')
        with self.connection.cursor() as cursor:
            for command in sqlCommands:
                try:
                    cursor.execute(command)
                except Exception as e:
                    pass

    def get_tickets_by_event(self, event_id):
        return self.execute_select(SELECT_TICKET_BY_EVENT.format(event_id=event_id))

    def get_events_by(self, category, tags):
        if category and tags:
            return self.execute_select(SELECT_EVENTS_BY_CATEGORY_AND_TAG)
        elif category:
            return self.execute_select(SELECT_EVENTS_BY_CATEGORY.format(category_name=category))
        elif tags:
            return self.execute_select(SELECT_EVENTS_BY_TAG)
        else:
            return self.execute_select(SELECT_ALL_EVENTS)


db_manager = DB_Manager(HOST, USER, PWD, DB_NAME)
