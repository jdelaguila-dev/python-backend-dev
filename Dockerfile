# Definimos la imagen base
FROM python:3.13.4

# Variables de entorno para evitar la creación de archivos .pyc y habilitar el buffer de salida
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalamos las dependencias del sistema necesarias
RUN apt-get update \
    && apt-get install -y postgresql-client build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiamos los archivos de requerimientos al contenedor
COPY requirements.txt /app/
# Instalamos las dependencias de Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiamos el resto del código de la aplicación al contenedor
COPY . /app/

# Exponemos el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]