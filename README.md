## Caritas Felices

Caritas Felices

## Instalación (primera vez)

1. Clona este repositorio:
    git clone https:https://github.com/gabrieldiaz8/caritas-felices.git
2. Crea y activa un entorno virtual:
    python3 -m venv venv
3. Ejecuta el entorno virtual:
    source venv/bin/activate  # En Windows: venv\Scripts\activate
4. Instala las dependencias:
    pip install -r requirements.txt
5. Ejecuta el servidor de desarrollo:
    python manage.py runserver

## Luego de instalación

1. Recorda siempre ejecutar el entorno virtual:
    source venv/bin/activate  # En Windows: venv\Scripts\activate
2. Ejecuta el servidor de desarrollo:
    python manage.py runserver

## Para utilizar el panel administrativo

1. Crea las migraciones de la base de datos:
    python manage.py makemigrations
2. Ejecuta las migraciones de la base de datos:
    python manage.py migrate
3. Crea un superusuario para acceder al panel administrativo:
    python manage.py createsuperuser





