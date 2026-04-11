# Why are there 2 link.py ?
# The one in models/link.py -> is for Db to see
# this one will be exposed to API client 

# DB model may have an hashed PW field. 
# So we control what goes in and what comes out.

from pydantic import HttpUrl, BaseModel
from datetime import datetime

#Validation Models:

class LinkCreate(BaseModel):
    """
    Defines what a request must send
    """
    original_url : HttpUrl

class LinkResponse(BaseModel):
    """ Defines what gets send back to the request """
    id: int
    original_url: str
    short_code: str
    created_at: datetime
    click_count: int

    #Normal pydantic expects dict, 
    class Config:
        from_attributes = True # This allows it to accept objects (ORM models)
    