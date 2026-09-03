import os
from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def inicio():
    db_host = os.getenv("DB_HOST", "db")

    conexion = psycopg2.connect(
        host=db_host,
        database="postgres",
        user="postgres",
        password="secreto"
    )

    cursor = conexion.cursor()
    cursor.execute("SELECT 1;")
    cursor.close()
    conexion.close()

    return "MiniBlog funcionando y conectado a PostgreSQL"

app.run(host="0.0.0.0", port=5000)