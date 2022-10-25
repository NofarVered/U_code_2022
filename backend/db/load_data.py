
from backend.db.db_manager import DB_Manager

from .consts.insert_quries import *

def insert_data_to_table(connector: DB_Manager,query: str,data: dict):
    try:
        connector.execute_insert(query, data)
    except Exception as e:
        return e

