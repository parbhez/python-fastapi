from fastapi import FastAPI

from schemas import Blog



app = FastAPI()

@app.get("/blogs")
async def get_blogs():
    return {"message": "Blogs fetched successfully"}

@app.post("/store")
async def store_blogs(blog: Blog):
    return {
        "data" : {
            "title" : blog.title,
            "body": blog.body
        }
    }


