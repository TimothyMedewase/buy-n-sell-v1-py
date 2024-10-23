import psycopg2
import os

conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user = "postgres",
        password= os.getenv('PGpassword'),
        port = "5432")