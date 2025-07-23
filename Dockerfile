# Imagen base
FROM python:3.10-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . /app

# Instalar dependencias
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Ejecutar el scraping antes de iniciar la API
RUN python -m app.scraper

# Exponer el puerto de FastAPI
EXPOSE 8000

# Comando para iniciar la API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
