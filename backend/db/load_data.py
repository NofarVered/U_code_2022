import imp
from .services.db_manager import DB_Manager
from .queries.insert_queries import *
from .mock_data.users_data import user_data
from .mock_data.event_data import event_data
from .mock_data.categories_data import categories_data
from .mock_data.event_tag_data import event_tag_data
from .mock_data.tickets_data import tickets_data




def load_all_data(db_manager: DB_Manager):
    for record in categories_data:
        db_manager.execute_insert(INSERT_INTO_CATEGORY, [record])
    for record in user_data:
        db_manager.execute_insert(INSERT_INTO_USER, list(record.values()))
    for record in event_data:
        db_manager.execute_insert(INSERT_INTO_EVENT, list(record.values()))
    for record in tickets_data:
        db_manager.execute_insert(INSERT_INTO_TICKET, list(record.values()))
    for record in event_tag_data:
        db_manager.execute_insert(INSERT_INTO_EVENT_TAG, list(record.values()))
    pass
