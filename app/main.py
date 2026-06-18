# Entry point
# Making the connections
from fastapi import FastAPI
from app.database import engine
from app.models.link import Base
from app.routes import links

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="URL Shortner")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["https://chiragintech.com", "https://www.chiragintech.com"],
    # allow_origin_regex = "https://.*\.chiragintech\.com", # type: ignore 
    # allow_credentials = True, # Only True when you are handling auth
    allow_methods = ['GET', 'POST'],
    allow_headers = ['Content-Type'],
)

@app.get("/")
def root():
    return {"message": "URL Shortener is running", "docs": "/docs"}


Base.metadata.create_all(bind=engine)  # looks at each subclass of Base
# Creates a table for each class if it doesn't exits already
# In prodn, this is replaced by proper migration tools like Alembic

# Registers all 3 routes from links to app
app.include_router(links.router)
# if theres a user feature in  future
# app.include_router(users.router)
