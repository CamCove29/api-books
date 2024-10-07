from fastapi import FastAPI, HTTPException
import mysql.connector
from pydantic import BaseModel

app = FastAPI()

# Detalles de conexión a la base de datos
host_name = "100.27.62.167"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "bd_api_books"

# Esquema Pydantic para validar el modelo de libro
class Book(BaseModel):
    title: str
    author: str
    genre: str
    year: int
    isbn: str
    estado: str

# Ruta de prueba de conexión para comprobar si el servicio está funcionando
@app.get("/")
def get_echo_test():
    return {"message": "Echo Test OK"}

# Obtener todos los libros
@app.get("/books")
def get_books():
    # Conexión a la base de datos
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM api_books")  # Consulta SQL para obtener todos los libros
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    
    # Verificar si se encontraron resultados
    if not result:
        raise HTTPException(status_code=404, detail="No se encontraron libros")
    return {"books": result}

# Obtener un libro por su ID
@app.get("/books/{id}")
def get_book(id: int):
    # Conexión a la base de datos
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM api_books WHERE id = %s", (id,))  # Consulta SQL para obtener un libro por ID
    result = cursor.fetchone()
    cursor.close()
    mydb.close()
    
    # Verificar si el libro existe
    if result is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"book": result}

# Añadir un nuevo libro
@app.post("/books")
def add_book(book: Book):
    # Conexión a la base de datos
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    
    # Consulta SQL para insertar un nuevo libro
    sql = "INSERT INTO api_books (title, author, genre, year, isbn, estado) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (book.title, book.author, book.genre, book.year, book.isbn, book.estado)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    
    return {"message": "Libro añadido exitosamente"}

# Actualizar un libro por su ID
@app.put("/books/{id}")
def update_book(id: int, book: Book):
    # Conexión a la base de datos
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    
    # Consulta SQL para actualizar un libro
    sql = "UPDATE api_books SET title=%s, author=%s, genre=%s, year=%s, isbn=%s, estado=%s WHERE id=%s"
    val = (book.title, book.author, book.genre, book.year, book.isbn, book.estado, id)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    
    return {"message": "Libro actualizado exitosamente"}

# Eliminar un libro por su ID
@app.delete("/books/{id}")
def delete_book(id: int):
    # Conexión a la base de datos
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = mydb.cursor()
    
    # Consulta SQL para eliminar un libro
    cursor.execute("DELETE FROM api_books WHERE id = %s", (id,))
    mydb.commit()
    cursor.close()
    mydb.close()
    
    return {"message": "Libro eliminado exitosamente"}

