import imp
from .services.db_manager import DB_Manager
from .queries.insert_queries import *
from .mock_data.users_data import user_data
from .mock_data.tickets_data import tickets_data
from .mock_data.categories_data import categories_data
from .mock_data.ticket_tag_data import ticket_tag_data



def load_all_data(db_manager: DB_Manager):
    for record in categories_data:
        db_manager.execute_insert(INSERT_INTO_CATEGORY, [record])
    for record in user_data:
        db_manager.execute_insert(INSERT_INTO_USER, list(record.values()))
    for record in tickets_data:
        db_manager.execute_insert(INSERT_INTO_TICKET, list(record.values()))
    for record in ticket_tag_data:
        db_manager.execute_insert(INSERT_INTO_TICKET_TAG, list(record.values()))
