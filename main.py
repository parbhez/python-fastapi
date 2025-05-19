from fastapi import FastAPI, status

from fastapi.responses import JSONResponse

from enum import Enum


app = FastAPI()


class Role(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"


@app.get('/user/{role}')
async def get_role(role: Role):
    if role == Role.ADMIN:
        return {
            "message": role.value  # বা "message": "ADMIN"
        }
    elif role == Role.USER:
        return {
            "message": role.value  # বা "message": "USER"
        }
    else:
        return {
            "message": "Not found"
        }
        

## 1st step
@app.get('/')
async def index():
    return {
        "message": "Hello World"
    }

# http://localhost:8000/users
@app.get('/users')
async def get_users():
    return {
        "message": "user fetch successfully!",
        "id": 1,
        "data" : ['masud', 'parbhez'],
        "email": 'a@gmail.com'
    }


# Path parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    print(item_id)
    return {
        "message": "Item Id fetch",
        "Item ID": item_id
    } 

@app.get("/products")
async def product():
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "user": True
    })
