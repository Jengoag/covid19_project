
## How to deploy to Heroku for dummies:

# Backend

`$` -> comando en consola
`H` -> en heroku

- `H` crearse una nueva cuenta en heroku gratuita

- `$ heroku login`
- `$ heroku create`
  - Este comando crea un nuevo proyecto en heroku con un nombre asignado por la plataforma

Opcional al comando `$ heroku create`:

- `H` crear un servicio nuevo en heroku, aqui podremos elegir el nombre/dominio que queramos
- `git remote add heroku <<RUTA NUEVO SERVICIO>>`
  - Con este comando ya podemos subir nuestros cambios a heroku

Seguimos:

- `$ pip install pipreqs`
- `$ pipreqs.pipreqs ./api`

  - En caso de que no funcione usar el comando `python3 -m`
    - `$ python3 -m pipreqs.pipreqs ./api`

- Gracias a ese comando se crea un archivo `requirements.txt` en nuestra carpeta api
- A este archivo hay que añadir

```
uvicorn==0.12.3
aiofiles==0.6.0
```

- Crear archivo runtime.txt y añadir version de python:

```
python-3.8.6
```

- Crear archivo Procfile

```
web: uvicorn api.main:router --host=0.0.0.0 --port=${PORT:-5000}
```

- Este comando es el mismo que usamos para iniciar fastapi con el puerto que designe Heroku o en su defecto el 5000

- `$ git push heroku master`

- Si todo va bien, al final del comando aparece que se ha desplegado el servicio y la ruta para acceder desde el navegador

- `$ heroku logs --tail`
- Este comando sirve para ver los logs de nuestra web en heroku

Credits: https://towardsdatascience.com/how-to-deploy-your-fastapi-app-on-heroku-for-free-8d4271a4ab9

## Base de Datos en Heroku

#### Configurar la conexion

Primero hay que añadir el addon de postgres a nuestro proyecto de Heroku:

- `H`
  - Resources
  - Add-ons
  - Buscar e instalar, `Heroku postgres`

Al hacer esto se creara una nueva variable de entorno llamada `DATABASE_URL` que sera la ruta a nuestra variable.

- Eliminar las variables:

```
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
postgres_url = f'postgresql+psycopg2://{user}:{password}@127.0.0.1:5432'
```

y sustituirlas por

```
postgres_url = os.getenv("DATABASE_URL")
```

Hay un bug en este addon y es que hay que cambiar la ruta de `postgres://` por `postgresql://` con este codigo cuando creamos la `engine`

```
postgres_url = os.getenv("DATABASE_URL")  # or other relevant config var
if postgres_url and postgres_url.startswith("postgres://"):
    postgres_url = postgres_url.replace("postgres://", "postgresql://", 1)
```

- Eliminar las variables del archivo `.env` y sustituirlas por `DATABASE_URL=postgresql+psycopg2://admin:admin@127.0.0.1:5432`

- Instalar
  - `pip install pipenv`
  - `pipenv install psycopg2`

#### Crear las tablas en la base de datos en Heroku

- `H`
  - More
  - Run console
  - Comando para ejecutar el archivo que crea las tablas:
    - `python api/database/database_creation.py`
  - Comprobar si aparece un error en el output
  - Si no aparece es que se ha creado la base de datos satisfactoriamente

# Frontend

- `$ pipreqs.pipreqs ./streamlit`
- Procfile

  - `web: sh setup.sh && streamlit run dashboard/main.py`

- crear archivo `setup.sh`

```
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

- `$ git push heroku master`
