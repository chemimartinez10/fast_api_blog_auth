from fastapi import APIRouter, HTTPException, Depends, status
from blog import schemas, crud
from sqlalchemy.orm import Session
from blog.database import get_db

router = APIRouter(prefix='/users', tags=['users'])

@router.get('/{user_id}', response_model=schemas.ShowUser, tags=['users'])
def show_user(user_id:int,db:Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db,user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail='This user does not exists')
    return db_user

@router.post('/create', response_model=schemas.ShowUser, tags=['users'])
def create_user(user:schemas.User, db:Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=403, detail='This email has already taken')
    return crud.create_user(db,user)


