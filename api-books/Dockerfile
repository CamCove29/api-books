FROM python:3-slim

# Establecer el directorio de trabajo en /programas/api-books
WORKDIR /programas/api-books

# Instalar dependencias necesarias
RUN pip3 install "fastapi[standard]"
RUN pip3 install pydantic
RUN pip3 install mysql-connector-python

# Copiar todos los archivos al contenedor
COPY . .
CMD ["fastapi", "run", "./main.py", "--port", "8000"]
