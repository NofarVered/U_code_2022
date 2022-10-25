import pymysql
import os
from backend.db.consts.consts import DB_NAME, HOST, PWD, USER
from db.consts.consts import *
from db.consts.queries import *
from db.db_utils import *


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

    # def get_heaviest_pokemon(self):
    #     with self.connection.cursor() as cursor:
    #         cursor.execute(SELECT_HEAVIEST_POKEMON)
    #         return cursor.fetchall()


db_manager = DB_Manager(HOST, USER, PWD, DB_NAME)
