from fastapi import FastAPI, status, Form, HTTPException, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Optional, Annotated
from fastapi.responses import JSONResponse
from enum import Enum
from pydantic import BaseModel

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

@app.get("/product")
async def product():
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "user": True
    })


@app.get('/blogs/unpublished')
async def unpublished_blog():
    return { "Data" : "Unpublished blog"}


@app.get("/blogs/{blog_id}")
async def blog_wise_comments(blog_id:int):
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "Blog": f"This is blog with Id {blog_id}"
    })



@app.get("/blogs/{blog_id}/comments")
async def blog_wise_comments(blog_id:int):
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "Blog": f"This is comments with Id {blog_id}"
    })

# Query parameters
@app.get('/posts')
async def posts(limit: int = 10, published: bool = True, sort: Optional[str] = 'asc', mp: str | None = "masud"):
    if published:

        return {"Post": f"Published Posts {limit} and { published } and {sort} and {mp}"}
    else:
       return {"Post": f"All Posts {limit} and { published }"}
    
@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(user_id: int, item_id: int, q: str | None = None, short: bool = False):
    item = { "item_id" : item_id, "owner_id" : user_id}

    if q:
        item.update({"q" : q})
    
    if not short:
        item.update({
            "description" : "This is an amazing item that has a short description"
        })
    else:
        item.update({
            "description" : "This is an amazing item that has a long description"
        })
    
    return item

class Product(BaseModel):
    title: str
    description: str | None = None
    price: float
    tax: float | None = None
    published_at: Optional[bool] = False

# Request Body
@app.post("/products")
async def create_product(request:Product):
    return {"data" : {
        "title" : request.title,
        "description" : request.description,
        "price" : request.price,
        "tax" : request.tax,
        'published_at' : request.published_at
    }}


# Pydantic Models for Forms
class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"} #allow, ignore, forbid


@app.post("/login")
async def login(data: Annotated[FormData, Form()]):
    return data



# Use HTTPException
students = {"foo": "The Foo Wrestlers"}
@app.get("/students/{student_id}")
async def read_item(student_id: str):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"item": students[student_id]}

# Import File
@app.post("/file/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/uploadfile")
async def upload_file(mp: UploadFile):
    return { "file name" : mp.file}

@app.post("/files/")
async def create_files(files: Annotated[list[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}

@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}

@app.get("/showfile")
async def main():
    content = """
        <body>
        <form action="/files/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        </body>
            """

    return HTMLResponse(content=content)