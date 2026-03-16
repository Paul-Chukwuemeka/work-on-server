from fastapi import APIRouter,Response,Depends,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Optional,List
from pydantic import BaseModel,Field
from pathlib import Path
import json
from lib.database import engine,get_db
from models.userModel import Base, User
from utils.crypto import hash_password



router = APIRouter()


class UserItem(BaseModel):
    username: str
    password: str
    email: str
    
class signUpItem(BaseModel):
    name: str
    country: str
    username: str
    password: str
    email: str
    

@router.post("/login", status_code=201)
def login(user: UserItem, db: Session=Depends(get_db)):
    try:
        newLogin=User(
            username = user.username,
            password= user.password,
            email = user.email
        )
        db.add(newLogin)
        db.commit()
        db.refresh(newLogin)
        return newLogin
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to add info")
    
@router.post("/signup")
def signup(user: signUpItem, db: Session=Depends(get_db)):
    newUser = json.dumps(user)
    return newUser
    try:
        newLogin= User(
            name = user.name,
            country = user.country,
            username = user.username,
            password= hash_password(user.password),
            email = user.email
        )
        db.add(newLogin)
        db.commit()
        db.refresh(newLogin)
        return newLogin
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=e)
 