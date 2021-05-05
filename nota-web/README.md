
# crear start app
py manage.py startapp nombreModulo
 crea una carpeta models, test, views, 

#nota
agregar el modulo en el archivo settings.py array NSTALLED_APPS[ ... ]
esto se ace para seguir el siguete paso que es ORM
se debe cambiar la ruta de modulo apps.py

 # ORM


 py manage.py migrate

 1. py manage.py makemigrations nombre_modulo

 2. py manage.py sqlmigrate polls 0001

 3. py manage.py migrate

 # SHELL
 py manage.py shell
 from apps.dashboard.model import Menu
 q = Menu(icon='home', rutaName='/home',nombre='Home')
 q.save()

#Django Admin

py manage.py createsuperuser
nombre de usuario: admin
pass by123456
1. cajero01 => by123456 Jose Rivera jose@gmail.com

## agregar model al admin del Django 

admin del modulo archivo admin.py 

## importamos el modelo
from .models import Menu
# y agregamos el model que deseamos mostrar en el admin de Django
admin.site.register(Menu)
### se puede agregar datos de un manera rapida


# Templates global
la linea de abajo debe estar en opcion arreglo TEMPLATES
opcion 'DIR :[]' dentro de ese arreglo para poder extender 
la plantilla de base en otra plantillas
os.path.join(BASE_DIR, 'templates'),
eJ.
DIR: [
    os.path.join(BASE_DIR, 'templates'),
]

## Formulario View
para poder verlo html agregar la palabra {{ form }}

