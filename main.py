from fastapi import FastAPI, Depends, HTTPException, status
from routers import blog, user, auth

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)

