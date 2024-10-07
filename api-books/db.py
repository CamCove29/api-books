import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("api-books.sqlite")

# Crear objeto cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Crear tabla 'api-books' con los atributos adicionales isbn y estado
sql_query = """ CREATE TABLE IF NOT EXISTS api-books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        genre TEXT NOT NULL,
                        year INTEGER NOT NULL,
                        isbn TEXT NOT NULL,  -- Añadido atributo ISBN
                        estado TEXT NOT NULL  -- Añadido atributo estado
                    )"""

# Ejecutar la creación de la tabla
cursor.execute(sql_query)
