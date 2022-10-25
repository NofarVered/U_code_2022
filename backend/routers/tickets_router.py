from fastapi import APIRouter, HTTPException, status
import requests
from ..utils.connect_details import connect_details as cd
# to do import to DB_Manager

connector = DB_Manager(cd.host, cd.user, cd.pwd, cd.db)

router = APIRouter()


# get tickets by user's input - category and tags.
# we will return all the tickets by the parameters above.
@router.get("/tickets/", status_code=200)
def get_tickets_by_input(category: str = "", tags: str = ""):
    try:
        pass
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exeception occured:{}".format(e)
        )
