from pydantic import BaseModel

# Esquema para los libros
class Book(BaseModel):
    title: str
    author: str
    genre: str
    year: int
    isbn: str
    estado: str
