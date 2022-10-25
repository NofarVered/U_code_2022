from fastapi import FastAPI
import uvicorn
from routers import tickets_router, users_router
from db import load_data
from db.db_manager import db_manager

load_data.load_all_data(db_manager)
 
app = FastAPI()


# create table call
# load data call

app.include_router(tickets_router.router)
app.include_router(users_router.router)


@app.get("/")
def root():
    return "server is up and running"


if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)
