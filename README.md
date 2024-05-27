
# Flask Character API

Esta es una API construida con Flask y SQLAlchemy para gestionar personajes (Character). La API permite agregar, obtener, listar y eliminar personajes, así como inicializar y eliminar la base de datos.

## Requisitos

- Python 3.8
- Flask
- Flask-RESTful
- SQLAlchemy
- Docker (para la configuración de Docker)

## Configuración del Proyecto

### Instalación de Dependencias

1. Clona el repositorio.

   ```sh
   git clone github.com:kamicase24/character_api.git
   cd character_api
   ```

2. Crea un entorno virtual y activa.

   ```sh
   python -m venv venv
   . venv/bin/activate
   ```

3. Instala las dependencias.

   ```sh
   pip3 install -r requirements.txt
   ```

### Estructura del Proyecto

```sh
.
├── app.py
├── db.py
├── models
│   └── character.py
├── views
│   ├── character_views.py
│   └── db_views.py
├── compose
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── templates
    └── docs.html

```

### Uso de Docker

1. Construye la imagen de Docker.

   ```sh
   docker-compose up -build
   ```

2. Inicia el contenedor.

   ```sh
   docker-compose up
   ```

3. Alternativa de inicialización.

    ```sh
   docker-compose start
   ```

4. Inicia el contenedor demonizado.

   ```sh
   docker-compose up -d
   ```

5. Detener el servicio.

   ```sh
   docker-compose stop
   ```

6. Acceder al shell de flask.

   ```sh
   docker-compose exec api flask shell
   ```

### Endpoints

#### Base de Datos

- **Inicializar la base de datos**

  ```sh
  GET /db/init
  ```

- **Eliminar tablas de la base de datos**

  ```sh
  GET /db/drop
  ```

#### Personajes

- **Agregar un personaje**

  ```sh
  POST /character/add
  POST /character/new
  POST /character
  ```

  **Body:**

  ```json
  {
    "character_id": 0,
    "name": "string",
    "height": 00.0,
    "mass": 00.0,
    "hair_color": "string",
    "skin_color": "string",
    "eye_color": "string",
    "birth_year": 0
  }
  ```

- **Obtener un personaje por ID**

  ```sh
  GET /character/get/<int:character_id>
  GET /character/<int:character_id>
  ```

- **Obtener todos los personajes**

  ```sh
  GET /character/getAll
  GET /character
  ```

- **Eliminar un personaje por ID**

  ```sh
  DELETE /character/delete/<int:character_id>
  ```

### Descripción de Archivos

- `app.py`: Configuración principal de Flask y definición de los recursos API.
- `db.py`: Configuración de SQLAlchemy y funciones para inicializar y eliminar la base de datos.
- `models/character.py`: Definición del modelo `Character`.
- `views/character_views.py`: Vistas y lógica de los endpoints relacionados con `Character`.
- `views/db_views.py`: Vistas y lógica de los endpoints relacionados con la base de datos.
- `compose/Dockerfile`: Dockerfile para construir la imagen de la aplicación.
- `docker-compose.yml`: Configuración de Docker Compose para orquestar los contenedores de la aplicación.

