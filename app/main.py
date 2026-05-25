from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "postgres")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")


@app.get("/")
def root():
    return {"message": "Infrastructure Challenge Running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/db-check")
def db_check():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )

    cur = conn.cursor()
    cur.execute("SELECT NOW();")

    result = cur.fetchone()

    cur.close()
    conn.close()

    return {
        "database": "connected",
        "time": str(result[0])
    }