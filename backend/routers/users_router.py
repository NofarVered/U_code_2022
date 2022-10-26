from fastapi import APIRouter, HTTPException, status
import requests
from db import db_manager

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
