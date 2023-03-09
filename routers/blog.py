from fastapi import APIRouter, HTTPException, Depends, status
from blog import schemas, crud, oauth2
from sqlalchemy.orm import Session
from blog.database import get_db

router = APIRouter(prefix='/blogs', tags=['blogs'], dependencies=[Depends(oauth2.get_current_user)])

@router.get('/', response_model=list[schemas.ShowBlog])
def index(skip:int = 0, limit:int = 20, db:Session = Depends(get_db)):
    blogs = crud.get_blogs(db,skip,limit)
    return blogs

@router.get('/{blog_id}')
def show(blog_id:int,db:Session = Depends(get_db)):
    db_blog = crud.get_blog(db,blog_id)
    if db_blog:
        return db_blog
    raise HTTPException(status_code=404, detail="This blog doesn't exists")

@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def create(blog:schemas.Blog, db:Session = Depends(get_db)):
    db_blog = crud.get_blog_by_title(db,blog_title=blog.title)
    if db_blog:
        raise HTTPException(status_code=404, detail="Blog title already exists")
    return crud.create_blog(db,blog)

@router.put('/update/{blog_id}')
def update(blog_id:int, blog:schemas.BlogUpdate, db:Session = Depends(get_db)):
    try:
        return crud.update_blog(db,blog,blog_id)
    except:
        raise HTTPException(status_code=404, detail="This blog doesn't exists")

@router.delete('/delete/{blog_id}')
def delete(blog_id:int, db:Session = Depends(get_db)):
    try:
        crud.delete_blog(db, blog_id)
        return {"detail":"Blog erased successfully"}
    except:
        raise HTTPException(status_code=404, detail="This blog doesn't exists")