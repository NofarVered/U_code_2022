from fastapi import APIRouter, HTTPException, status
import requests
from utils import *
from db import db_manager

router = APIRouter()

# get tickets by user's input - category and tags.
# we will return all the tickets by the parameters above.


@router.get("/tickets/", status_code=200)
def get_tickets_by_event(event_id: str):
    try:
        event_id = int(event_id)
        raw_tickets = db_manager.get_tickets_by_event(event_id)
        tickets = {"tickets": [Ticket(ticket) for ticket in raw_tickets]}
        return tickets

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exeception occured:{}".format(e)
        )
