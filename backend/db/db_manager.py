import pymysql
import os
from consts.consts import *
from db_utils import *
from consts.consts import *


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

    def get_tickets_by(category, tags):
        if category and tags:
            pass

        
    # def get_heaviest_pokemon(self):
    #     with self.connection.cursor() as cursor:
    #         cursor.execute(SELECT_HEAVIEST_POKEMON)
    #         return cursor.fetchall()


db_manager = DB_Manager(HOST, USER, PWD, DB_NAME)
