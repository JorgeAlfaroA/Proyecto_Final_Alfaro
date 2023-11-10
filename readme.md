# Proyecto_Recetario
***
+ La idea es poder generar ese recetario que todas las familias tienen, de una forma digital. Si pudieramos hacer que todas las familias completen su recetario, con diferentes inredientes, cantidades, historias, podriamos generar un recetario global con las recetas de todas las familias del mundo, tradiciones diferentes, historias, y todo al hacer un par de clicks.

## Instrucciones para instalar el proyecto en local

+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Clona este proyecto en la carpeta madre
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```
+ Si es necesario, corre dentro de la carpeta madre:

```
python manage.py makemigrations
python manage.py migrate
```
+ En ese orden

+ Prende el servidor dentro de la carpeta Blog:
```
python manage.py runserver
```
## Instrucciones para entrar al panel aministrativo de Django
+ En consola, crear un superuser:
```
python manage.py createsuperuser
```
+ Acceder con user y password via:
```
127.0.0.1:8000/admin
```
# Usuarios normales
+ Usar los botones en la vista del proyecto, son bastante intuitivos y se pueden crear los usuarios deseados.