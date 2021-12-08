from typing import List
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from database import UserDatabase
from serializers import CreateUserSerializer, UserSerializer, UpdateUserSerializer


app = FastAPI()
user_database = UserDatabase() #VAriável que guarda
#essa conexão com a tabela user no BAnco de dados

@app.get('/status/')
def status_ok():
    return {"status":"okay"}


"""
CRUD = Create, Read, Update, Delete
"""

# CREATE USER

@app.post(
    '/users/', 
    status_code=status.HTTP_201_CREATED,
    response_model=UserSerializer
    )
def create_user(user: CreateUserSerializer): #essa variável user pode ser qualquer coisa
    new_user = user_database.add_user(user.dict())
    return new_user

# GET USER

@app.get('/user/', response_model=List[UserSerializer])
def get_users():
    return user_database.get_users()

# GET USER BY ID 

@app.get('/users/{user_id}', response_model=UserSerializer)
def get_user(user_id:str):
    #user = user_database.get_user(user_id)
    #tratamentos
    #return user
    user =  user_database.get_user(user_id)
    if user is None:
        return JSONResponse(
            content=dict(message="User not found"),
            #ou content={'message':'User not found'}
            status_code=status.HTTP_404_NOT_FOUND
            )
    return user

# UPDATE USER BY ID

@app.put('/users/{user_id}/')
def update_user(user_id: str, user_to_update: UpdateUserSerializer):
    updated_user = user_database.update_user(user_id, user_to_update.dict())
    if updated_user is None:
        return JSONResponse(
            content=dict(message="User not found"),
            #ou content={'message':'User not found'}
            status_code=status.HTTP_404_NOT_FOUND
            )
    return updated_user



# DELETE USER BY ID

@app.delete('/users/{user_id}/')
def delete_user(user_id: str, status_code=status.HTTP_204_NO_CONTENT):
    deleted=user_database.delete_user(user_id)
    if not deleted:
        return JSONResponse(
            content={'mesage': 'User not found'},
            status_code=status.HTTP_404_NOT_FOUND
        )