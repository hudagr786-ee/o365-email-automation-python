from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from exchange_service import ExchangeService


app = FastAPI(
    title="Exchange Email Monitor"
)


# Serve saved attachments
app.mount(
    "/attachments",
    StaticFiles(directory="attachments"),
    name="attachments"
)


# Serve frontend
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


exchange_service = ExchangeService()



@app.get("/")
def home():

    return FileResponse(
        "static/index.html"
    )



@app.get("/dashboard")
def dashboard():

    emails = exchange_service.read_emails(
        limit=10
    )

    return {
        "emails": emails
    }