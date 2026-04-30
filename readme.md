# Adoratio

Adoratio es una aplicación pensada para músicos, bandas y grupos de alabanza que necesitan organizar canciones, acordes y playlists de forma simple y colaborativa.

El objetivo del proyecto es evitar depender de capturas de pantalla, páginas con anuncios o letras mal estructuradas.

---

# Objetivo del proyecto

Crear una plataforma donde cualquier usuario pueda:

* Guardar canciones con letra y acordes
* Organizar playlists
* Compartir repertorios con otros músicos
* Transponer tonalidades
* Tener acceso rápido desde celular o web
* Crear una biblioteca musical propia

---

# Tecnologías utilizadas

## Backend

* Python
* FastAPI
* Uvicorn
* Pydantic

## Próximamente

* PostgreSQL
* SQLAlchemy
* Autenticación de usuarios
* Frontend web
* Aplicación móvil

---

# Estructura del proyecto

```text
adoratio/
│
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   ├── schemas/
│   │   ├── main.py
│   │   └── __init__.py
│   │
│   └── requirements.txt
│
├── frontend/
├── docs/
├── README.md
└── .gitignore
```

---

# Estado actual

Actualmente el proyecto cuenta con:

* API inicial funcionando
* Endpoint principal (`/`)
* Router de canciones
* Endpoint GET `/songs`
* Endpoint POST `/songs`
* Validación de datos mediante schemas
* Almacenamiento temporal en memoria
* Documentación automática con Swagger

---

# Cómo ejecutar el proyecto

## 1. Clonar repositorio

```bash
git clone https://github.com/TU-USUARIO/adoratio.git
```

---

## 2. Entrar al proyecto

```bash
cd adoratio
```

---

## 3. Crear entorno virtual

```bash
python -m venv venv
```

---

## 4. Activar entorno virtual

### Windows

```bash
venv\Scripts\Activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 5. Instalar dependencias

```bash
pip install -r backend/requirements.txt
```

---

## 6. Ejecutar backend

Entrar a:

```bash
cd backend
```

Y luego ejecutar:

```bash
uvicorn app.main:app --reload
```

---

# Documentación API

Una vez iniciado el servidor:

```text
http://127.0.0.1:8000/docs
```

---

# Roadmap

## Backend

* [x] FastAPI inicial
* [x] Router de canciones
* [x] Schemas
* [x] Validación de datos
* [ ] Base de datos PostgreSQL
* [ ] SQLAlchemy
* [ ] Autenticación
* [ ] Roles de usuario
* [ ] Compartir playlists

## Frontend

* [ ] Interfaz web
* [ ] Login
* [ ] Biblioteca de canciones
* [ ] Crear playlists
* [ ] Buscador
* [ ] Responsive mobile

---

# Aprendizaje

Este proyecto también funciona como roadmap de aprendizaje.

El objetivo no es solo terminar una aplicación, sino aprender:

* Arquitectura backend
* APIs REST
* Bases de datos
* Modelado de datos
* Buenas prácticas
* Git y GitHub
* Estructuración profesional de software

---

# Estado del proyecto

Proyecto en desarrollo activo.

Actualmente se está construyendo la arquitectura backend paso a paso.
