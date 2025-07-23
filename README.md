# RPA Quotes Scraper & REST API

Este proyecto realiza scraping del sitio [quotes.toscrape.com](https://quotes.toscrape.com), almacena la información en una base de datos relacional y expone una API REST con filtros de búsqueda. Fue desarrollado como parte de una prueba técnica para un rol de Desarrollador/a RPA.

---

## Objetivo

- Automatizar la recolección de citas desde la web.
- Almacenar las citas en una base de datos relacional (SQLite).
- Exponer los datos a través de una API REST desarrollada con FastAPI.
- Permitir búsquedas por autor, etiqueta o contenido.

---

## Tecnologías Usadas

- **Python 3.10+**
- **FastAPI** – API REST.
- **SQLAlchemy** – ORM y modelo de persistencia.
- **SQLite** – Base de datos relacional local.
- **BeautifulSoup4** – Scraping web.
- **Uvicorn** – Servidor ASGI para FastAPI.

---

## Instalación y Ejecución

### 1. Clonar el repositorio 

```bash
git clone 
cd rpa_quotes_project

2. Crear y activar entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate

### 3. Instalar dependencias
```bash
pip install -r requirements.txt

### 4. Ejecutar el scraper
```bash
python -m app.scraper

### 5. Ejecutar la API
```bash
uvicorn app.main:app --reload

### 6. Probar la API en Swagger UI
Abrir en el navegador: http://127.0.0.1:8000/docs

## Endpoints
GET /quotes
Obtiene todas las citas almacenadas.

Filtros opcionales combinables:

?author=Einstein – Filtra por autor.
?tag=change – Filtra por etiqueta.
?search=world – Búsqueda libre por contenido.

## Docker
El proyecto puede ejecutarse fácilmente con Docker.

### Construir la imagen
```bash
docker build -t rpa-quotes-app .

### Ejecutar el contenedor
```bash
docker run -p 8000:8000 rpa-quotes-app

### Probar la API en Swagger UI
Abrir en el navegador: http://127.0.0.1:8000/docs
