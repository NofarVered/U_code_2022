from fastapi import APIRouter, HTTPException, status
import requests
from ..db.consts.consts import *
from ..db.db_manager import db_manager
from ..utils.helpers import *

# connector = DB_Manager(HOST, USER, PWD, DB_NAME)

router = APIRouter()


# get tickets by user's input - category and tags.
# we will return all the tickets by the parameters above.
@router.get("/tickets/", status_code=200)
def get_tickets_by_input(category: str = "", tags: str = ""):
    try:
        tag_list = parse_str_tags_to_list(tags)
        validate_category(category)
        tickets = db_manager.get_tickets_by(category, tag_list)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exeception occured:{}".format(e)
        )
