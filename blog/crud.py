from sqlalchemy.orm import Session
from . import schemas, models, utils

def get_blog(db:Session, blog_id:int):
    return db.query(models.Blog).filter(models.Blog.id==blog_id).first()
def get_blog_by_title(db:Session, blog_title:str):
    return db.query(models.Blog).filter(models.Blog.title==blog_title).first()
def get_blogs(db:Session, skip:int=0, limit:int = 20):
    return db.query(models.Blog).offset(skip).limit(limit).all()

def create_blog(db:Session, blog:schemas.Blog):
    db_blog = models.Blog(**blog.dict())
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def update_blog(db:Session, blog:schemas.BlogUpdate, blog_id:int):
    db_blog = db.get(models.Blog, blog_id)
    if db_blog:
        db_blog.title = blog.title if blog.title else db_blog.title
        db_blog.content = blog.content if blog.content else db_blog.content
        db_blog.published = blog.published if blog.published else db_blog.published
        db.commit()
        db.refresh(db_blog)
        return db_blog
    else:
        raise Exception("blog not found")

def delete_blog(db:Session, blog_id:int):
    db_blog = db.get(models.Blog,blog_id)
    if db_blog:
        db.delete(db_blog)
        db.commit()
    else:
        raise Exception("blog not found")
    

##########
###USER###
##########


def create_user(db:Session, user:schemas.User):
    db_user = models.User(name=user.name, email=user.email, password=utils.Hash.bcrypt(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db:Session, user_email:str):
    return db.query(models.User).filter(models.User.email==user_email).first()
def get_user_by_id(db:Session, user_id:int):
    return db.query(models.User).filter(models.User.id==user_id).first()
