# blog_project made with FastAPI

written in Python, requires python 3.10 or later
## run with following commands:

### install dependencies
pip install -r requirements

### start alembic for database migrations
alembic init

### run migrations with every change on database's models
alembic revision --autogenerate

### commit changes to DB
alembic upgrade head

### serve the server app with uvicorn, ensure to have port 8000 free
uvicorn main:app --reload
