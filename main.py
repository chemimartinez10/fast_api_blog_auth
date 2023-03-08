from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from blog import crud, models, schemas
from blog.database import SessionLocal, engine

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/blogs')
def index(skip:int = 0, limit:int = 20, db:Session = Depends(get_db)):
    blogs = crud.get_blogs(db,skip,limit)
    return blogs

@app.get('/blogs/{blog_id}')
def show(blog_id:int,db:Session = Depends(get_db)):
    db_blog = crud.get_blog(db,blog_id)
    if db_blog:
        return db_blog
    raise HTTPException(status_code=404, detail="This blog doesn't exists")

@app.post('/blogs/create', status_code=status.HTTP_201_CREATED)
def create(blog:schemas.Blog, db:Session = Depends(get_db)):
    db_blog = crud.get_blog_by_title(db,blog_title=blog.title)
    if db_blog:
        raise HTTPException(status_code=404, detail="Blog title already exists")
    return crud.create_blog(db,blog)

@app.put('/blogs/update/{blog_id}')
def update(blog_id:int, blog:schemas.BlogUpdate, db:Session = Depends(get_db)):
    try:
        return crud.update_blog(db,blog,blog_id)
    except:
        raise HTTPException(status_code=404, detail="This blog doesn't exists")

@app.delete('/blogs/delete/{blog_id}')
def delete(blog_id:int, db:Session = Depends(get_db)):
    try:
        crud.delete_blog(db, blog_id)
        return {"detail":"Blog erased successfully"}
    except:
        raise HTTPException(status_code=404, detail="This blog doesn't exists")
    
    