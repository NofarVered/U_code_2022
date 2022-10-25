from fastapi import APIRouter, HTTPException, status
import requests
from ..utils.connect_details import connect_details as cd
# to do import to DB_Manager

connector = DB_Manager(cd.host, cd.user, cd.pwd, cd.db)

router = APIRouter()


# get notifications for user.
@router.get("/users/notifications", status_code=200)
def get_notification_for_user():
    try:
        pass
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exeception occured:{}".format(e)
        )
