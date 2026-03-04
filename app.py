from fastapi import FastAPI,Response,Depends
from typing import Optional,List
from pydantic import BaseModel,Field
from pathlib import Path
import json

class NewTask(BaseModel):
    name: str

file = Path("db.json")
# create file to store tasks
def checkFile(): #check if file exists and create if not
    
    if not file.exists(): #if file doesnt exist
        file.touch() #create file
        file.write_text(json.dumps([])) # place an empty array in file
checkFile()

def write_to_file(tasks):
    print(tasks)
    file.write_text(json.dumps(tasks))

def readTask():
    list = json.loads(file.read_text()) # read content from file into list
    return list

def check_id(id,tasks):
    found = any(task.get("id") == id for task in tasks)
    return found

server = FastAPI()



@server.get("/")
def get_task(tasks:List = Depends(readTask)):
    return tasks

@server.get("/{id}")
def get_task_by_id(id:int,response: Response,tasks = Depends(readTask)):
    found = check_id(id,tasks)
    if not found:
        response.status_code = 404
        return "task not found"
    return tasks[id - 1]

@server.post("/add")
def add_task(new_task: NewTask,tasks:List = Depends(readTask)):
    last = tasks[len(tasks) - 1]["id"] if len(tasks) >= 1 else 0
    tasks.append(dict(new_task,id= last + 1 ))
    write_to_file(tasks)
    return tasks
    

@server.put("/update/{id}")
def update_task(id:int,response: Response,new_task: NewTask,tasks:List = Depends(readTask)):
    found = check_id(id,tasks)
    if not found:
        response.status_code = 404
        return "task not found"
    tasks[id - 1] = dict(new_task,id = id)
    write_to_file(tasks)
    return tasks

@server.delete("/delete/{id}")
def delete_task(id:int,response: Response,tasks:List = Depends(readTask)):
    found = check_id(id,tasks)
    if not found:
        response.status_code = 404
        return "task not found"
    
    for i,task in enumerate(tasks):
        if task["id"] == id:
            tasks.pop(i)
    write_to_file(tasks) 
    return tasks


# users =[
#     {"id": 1, "name": "joseph"},
#     {"id": 2, "name": "jose"},
#     {"id": 3, "name": "joe"},
#     {"id": 4, "name": "josephine"},
#     {"id": 5, "name": "josephina"},
#     {"id": 6, "name": "josef"}
# ]

# class Userresponse(BaseModel):
#     name: str

# class User(BaseModel):
#     id: int = Field(..., gt=len(users) )
#     name:str = Field(...,min_length=2)



# @server.get("/health")
# def health_Check(response: Response):
#     response.status_code = 203
#     return {"name":"Joseph Benin Man"}

# @server.get("/users",response_model=List[Userresponse])
# def get_users(minId: Optional[int] = None):
#     found = [user for user in users if user['id'] >= minId] if minId and minId >= 0 else users  
#     return found


# @server.get("/users/{id}",response_model=List[Userresponse])
# def get_user(id: int):
#     found = [user for user in users if user["id"] == id ]
#     return found


# @server.post("/users/add",response_model=List[Userresponse])
# def add_user(data: User):
#     # print(len(users))
#     # if( data.id <= len(users)):
#     #     return f"id must be greater than {len(users)}"
    
#     users.append(dict(data))
    
#     return users
    



# @server.post("/health")
# def health_Checker():
#    return {"name":"Joseph Benin Man from post"}