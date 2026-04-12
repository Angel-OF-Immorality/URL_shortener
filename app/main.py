# Entry point
# Making the connections
from fastapi import FastAPI
from app.database import engine
from app.models.link import Base
from app.routes import links

app = FastAPI(
    title= "URL Shortner"
)

Base.metadata.create_all(bind=engine) #looks at each subclass of Base
# Creates a table for each class if it doesn't exits already
# In prodn, this is replaced by proper migration tools like Alembic

# Registers all 3 routes from links to app
app.include_router(links.router)
# if theres a user feature in  future
# app.include_router(users.router)