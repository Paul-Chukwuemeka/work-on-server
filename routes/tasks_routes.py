from fastapi import APIRouter,Response,Depends,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Optional,List
from pydantic import BaseModel,Field
from pathlib import Path
import json
from lib.database import engine,get_db
from models.tasksModel import Base, Task




router = APIRouter() 


class TaskItem(BaseModel):
    name: str
    
class UpdateItem(BaseModel):
    title:Optional[str] = None
    completed:Optional[bool] = None


@router.post("/tasks/add")
def add_task(task: TaskItem,response:Response,db:Session = Depends(get_db)):
    try:
        newTask = Task(
            title = task.name,
        )
        db.add(newTask)
        db.commit()
        db.refresh(newTask)
        response.status_code = 201
        return newTask
    except IntegrityError:
        db.rollback()
        return HTTPException(500, detail="Failed to add product")
    



@router.get("/tasks/")
def get_tasks(response: Response,db:Session = Depends(get_db)):
    try:
        tasks = db.query(Task).all()
        response.status_code = 202
        return tasks
    except:
        return HTTPException(500, detail="Failed to get products")
    

@router.get("/tasks/{id}")
def get_task(id:int,response: Response,db:Session = Depends(get_db)):
    try:
        task = db.query(Task).filter(Task.id == id).first()
        if not task:
            raise HTTPException(404,detail="task not found")
        response.status_code = 202
        return task
    except Exception as err:
        return HTTPException(500, detail= err or "Failed to get product")
        
    
@router.delete("/tasks/delete/{id}")
def delete_task(id:int,response: Response,db:Session = Depends(get_db)):
    try:
        task = db.query(Task).filter(Task.id == id).first()
        db.delete(task)
        db.commit()
        response.status_code = 203
        return "task deleted"
    except:
        db.rollback()
        return HTTPException(500, detail="Failed to get product")
        

@router.patch("/tasks/update/{id}")
def update_task(id:int,update: UpdateItem,response: Response,db:Session = Depends(get_db)):
        try:
            task = db.query(Task).filter(Task.id == id).first()
            if not task:
                raise HTTPException(404,detail="task not found")
            for key,value in update.model_dump(exclude_unset=True).items():
                setattr(task,key,value)
            db.commit()
            db.refresh(task)
            return task
        except Exception as err:
            db.rollback()
            return HTTPException(status_code=500, detail= err or "Failed to update product")
            
