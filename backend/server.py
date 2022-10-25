from fastapi import FastAPI
import uvicorn


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
