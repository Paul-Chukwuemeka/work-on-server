

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# class UserItem(BaseModel):
#     username: str
#     password: str
#     email: str
    
# class signUpItem(BaseModel):
#     name: str
#     country: str
#     username: str
#     password: str
#     email: str
    
# class UpdateItem(BaseModel):
#     username: str
#     password: str
#     email: str
    
# @app.get("/login")
# def check_login(db: Session=Depends(get_db)):
#     try:
#         users = db.query(Task).all()
#         return users
#     except Exception:
#         raise HTTPException(500, detail="Failed to get users")
    
# @app.get("/login/{id}")
# def get_user(id:int, db: Session=Depends(get_db)):
#     try:
#         user = db.query(Task).filter(Task.id == id).first()
#         if not user:
#             raise HTTPException(status_code=404, detail="user not found")
#         return user
#     except Exception:
#         raise HTTPException(status_code=500, detail="Failed to get user")


# @app.post("/addLogin", status_code=201)
# def add_login(user: UserItem, db: Session=Depends(get_db)):
#     try:
#         newLogin=Task(
#             username = user.username,
#             password= user.password,
#             email = user.email
#         )
#         db.add(newLogin)
#         db.commit()
#         db.refresh(newLogin)
#         return newLogin
#     except Exception:
#         raise HTTPException(status_code=500, detail="Failed to add info")
    
# @app.post("/addSignup", status_code=201)
# def add_Signup(user: signUpItem, db: Session=Depends(get_db)):
#     try:
#         newLogin=Task(
#             name = user.name,
#             country = user.country,
#             username = user.username,
#             password= user.password,
#             email = user.email
#         )
#         db.add(newLogin)
#         db.commit()
#         db.refresh(newLogin)
#         return newLogin
#     except Exception as e:
#         print(e)
#         raise HTTPException(status_code=500, detail="Failed to add info")
    
    
# @app.delete("/delete/{id}")
# def delete_login(id: int, user: UserItem, db: Session=Depends(get_db)):
#     try:
#         user = db.query(Task).filter(Task.id == id).first()
#         if not user:
#             raise HTTPException(status_code=404, detail="user not found")
#         db.delete(user)
#         db.commit()
#         return {"message": "user deleted"}
#     except Exception:
#         db.rollback()
#         raise HTTPException(status_code=500, detail="Failed to get user")
    
    
# @app.patch("/update/{id}")
# def update_login(id:int, update: UpdateItem, db:Session=Depends(get_db)):
#     try:
#         user = db.query(Task).filter(Task.id == id).first()
#         if not user:
#             raise HTTPException(404, detail="user not found")
#         for key, value in update.model_dump(exclude_unset=True).items():
#             setattr(user,key,value)
#         db.commit()
#         db.refresh(user)
#         return user
#     except Exception:
#         raise HTTPException(status_code=500, detail="Failed to update user")
    

