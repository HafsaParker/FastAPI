#Import fastAPI
from fastapi import FastAPI
from typing import Optional
#instance of FASTAPI
app = FastAPI()
#this function handles the path
# Pydantic --> it looks for data validation

## /blog?limit=10&published=true
@app.get('/blog')
def index(limit,published: bool, sort:Optional[str]):
    # because of this query will get only 10 published blogs
    if published:
        return {'data':f'{limit} blogs from the db'}
    else:
        return "No published blogs"


#@app.get('/about')
#def about():
#    return {'data':{'aboutPage'}}
#



@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs '}



# Dynamic routing
@app.get('/blog/{id}')
def show(id :int):
    # fetch id = id
    return {'data': id}



@app.get('/blog/{id}/comment')
def comment(id):
    # fetch comments of blog with id = id
    return {'data':{'1','2'}}
