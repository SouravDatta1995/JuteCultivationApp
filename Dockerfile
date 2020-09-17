FROM python:3.8

RUN pip3 install fastapi uvicorn FastAPI-SQLAlchemy alembic psycopg2

EXPOSE 5000

COPY ./ /app

ENV PYTHONPATH "app/:app/Routes/:app/Database:app/Database/crud:app/alembic:"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]