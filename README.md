# 🐉 Pokémon API - Backend (Django REST Framework)

Este proyecto es el núcleo de datos para la Pokédex del **Taller de QA**. Proporciona una API robusta para la gestión de especímenes, incluyendo la sincronización automática con datos oficiales y operaciones CRUD completas para pruebas de calidad.

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.10+**
- **Django 5.x**
- **Django REST Framework**
- **PostgreSQL**
- **psycopg2**
- **django-cors-headers**
- **python-dotenv**
- **asgiref**
- **sqlparse**
- **tzdata**
- **Requests** (con `certifi`, `urllib3`, `charset-normalizer`, `idna`)
- **PyTest**

---

## 🚀 Instalación y Configuración

Sigue estos pasos para poner en marcha el servidor de desarrollo en tu máquina local:

### 1. Preparar el Entorno

Se recomienda el uso de un entorno virtual para aislar las dependencias:

```bash
python -m venv venv
```

#### En Windows:

```bash
.\venv\Scripts\activate
```

#### En Linux/Mac:

```bash
source venv/bin/activate
```

### 2. Crear la Base en postgres y crear y adecuar el .env

### 3. Realizar las migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Llenar la base

```bash
python manage.py import_pokemons
```

### 5. Correr el backend

```bash
python manage.py runserver
```
