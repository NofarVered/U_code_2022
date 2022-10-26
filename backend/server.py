from asyncio import events
from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from routers import tickets_router, users_router, events_router
from db.services.db_manager import db_manager
from db.load_data import load_all_data

app = FastAPI()

# load_all_data(db_manager)
app.include_router(events_router.router)
app.include_router(tickets_router.router)
app.include_router(users_router.router)


@app.get("/sanity")
def root():
    return {"message": "Server is running"}


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
