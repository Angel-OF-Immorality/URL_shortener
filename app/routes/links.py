# API Layer - POST & GET routes
# Business logic
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.link import Link
from app.schemas.link import LinkCreate, LinkResponse
import random 
import string

router = APIRouter() # Used to structure routes 

def generate_short_code(length: int = 6) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length)) #random.choices allows duplicate choices

@router.post("/shorten", response_model = LinkResponse) 
def create_short_link(payload: LinkCreate, db: Session = Depends(get_db)): # Depends() injects FastAPI dependency
    # Not needed because of Depends() :
    # db = SessionLocal()
    # try:
    #     short_code = generate_short_code(), more code. ...
    # finally:
    #     db.close()

    short_code = generate_short_code()

    # Ensure uniqueness
    while db.query(Link).filter(Link.short_code == short_code).first():
        short_code = generate_short_code()

    link = Link(
        original_url = str(payload.original_url),
        short_code = short_code
    )

    db.add(link)
    db.commit()
    db.refresh(link)

    return link


@router.get("/{short_code}")
def redirect_to_original(short_code:str, db:Session = Depends(get_db)):
    link = db.query(Link).filter(Link.short_code == short_code).first()

    if not link:
        raise HTTPException(status_code = 404, detail = "Link Not Found")
        
    link.click_count += 1
    db.commit()        
    
    return RedirectResponse(url = link.original_url)

@router.get("/stats/{short_code}", response_model=LinkResponse)
def get_link_stats(short_code: str, db: Session = Depends(get_db)):
    link = db.query(Link).filter(Link.short_code == short_code).first()
    
    if not link:
        raise HTTPException(status_code=404, detail="Short link not found")
    
    return link