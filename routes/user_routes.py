from fastapi import APIRouter,Response,Depends,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Optional,List
from pydantic import BaseModel,Field
from pathlib import Path
import json
from lib.database import engine,get_db
from models.userModel import Base, User



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
    
class UpdateItem(BaseModel):
    username: str
    password: str
    email: str
    
@router.get("/users")
def get_users(db: Session=Depends(get_db)):
    try:
        users = db.query(User).all()
        return users
    except Exception:
        raise HTTPException(500, detail="Failed to get users")

    
@router.get("/users/{id}")
def get_user(id:int, db: Session=Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        return user
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to get user")
    
       
    
@router.delete("/users/delete/{id}")
def delete_login(id: int, user: UserItem, db: Session=Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        db.delete(user)
        db.commit()
        return {"message": "user deleted"}
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to get user")
    
    
@router.patch("/users/update/{id}")
def update_login(id:int, update: UpdateItem, db:Session=Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(404, detail="user not found")
        for key, value in update.model_dump(exclude_unset=True).items():
            setattr(user,key,value)
        db.commit()
        db.refresh(user)
        return user
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to update user")