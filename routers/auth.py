from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from blog import crud, token
from blog.database import get_db
from blog.utils import Hash

router = APIRouter(prefix='/auth', tags=['Authentication'])

@router.post('/login')
def login(req:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db,req.username)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    if not Hash.verify(req.password, db_user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    
    access_token = token.create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}