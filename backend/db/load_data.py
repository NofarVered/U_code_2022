from .db_manager import DB_Manager
from .consts.insert_quries import *
from .mock_data.users_data import user_data
from .mock_data.tickets_data import tickets_data
from .mock_data.categories_data import categories_data

def load_all_data(connector: DB_Manager):
    connector.execute_insert(INSERT_INTO_CATEGORY,categories_data)
    connector.execute_insert(INSERT_INTO_USER,user_data)
    connector.execute_insert(INSERT_INTO_TICKET,tickets_data)
