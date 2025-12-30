# Repaso de contenidos

- Creacion de views y enlace con urls
- Manejo de panel admin con creacion de usuarios
    ``` python3 manage.py createsuperuser ```
    creacion de tareas dentro del panel de admin
- Jinja loops
    podemos usar bucles for dentro de ``` { % for element in list %} ``` para recorrer y añadir cualquier tipo de codigo  y acceder a atributos de objetos (ej html).


## Esquema de flujo 

``` bash 

Request
  ↓
project/urls.py
  ↓
app/urls.py
  ↓
view
  ↓
response (JSON / HTML / status)

```

Supongamos que creamos una app de tareas, podemos crearlas con los atributos: nombre, fecha, importancia y booleano de completado.
Usamos metodos HTTP para modificar los valores 
| Operación  | Método |
| ---------- | ------ |
| Ver tareas | GET    |
| Añadir     | POST   |
| Completar  | PATCH  |
| Borrar     | DELETE |


Para poder modificar una en concreto usamos el id en el path.

### Equema visual

```sql 
/tasks/
  ├─ GET     → listar
  ├─ POST    → crear
/tasks/3/
  ├─ GET     → ver una
  ├─ PATCH   → completar
  ├─ DELETE  → borrar

```


Aunque cambiemos de DB las url no se modifican ni las views.

## Herencia de templates

Usamos el comando de jinja : ``` {% extends 'nombre de archivo' %} ```



# Conceptos

## Models
Un Model de django es una clase que describe una tabla de la base de datos y como trabajar con ella.

Cada objeto es una fila en la DB.

En nuestro ejemplo de la lista de tares, cada tarea es una instancia de la clase.

### Migracion

Es como un "diff" versionado en tu DB.

#### Flujo mental: 

``` scss 
models.py (cambio)
   ↓
makemigrations   → crea el plan
   ↓
migrate          → ejecuta el plan en la BD

```

Si añadimos un nuevo campo `descripcion` a tareas, el HTML se recarga auto, pero la BD no, hay que hacer una migracion.

Si añado una nueva propiedad `importancia` al la BD, tendria que darle un valor por defecto y migrar.


## Flujo de datos para views + modelos

Cuando una view necesita datos de un modelo, Django devuelve una estructura propia. Se llama `Query set`, la view decide que tipo de dato quiere (HTML, JSON, lo que quieras).

### Que es QuerySet? 
Es como una lista,  como iterador, todavia no es JSON ni lista normal.

La view se encarga de convertir el QuerySet al tipo de dato que queremos.

# Django REST Framework (DRF)

Añade una capa entre mis modelos y el JSON, se llama serializer.

## FLujo mental: 

Un model = una tabla de la BD.

Un atributo = una columna de la BD

Cuando hacemos `priority = IntegerField(null = True)`
Decimos que cada tarea va a tener una columna llamada `priority` que puede ser null.

### Caso API
La view consulta: 
- La BD
- Convierte los objetos a JSON (con ayuda del serializer)
- Devuelve JsonResponse


Incluimos librerias e importamos desde `models` el objeto `Task`

con la funcion `json.loads(request.body)`podemos parsear el body de la request y devuelve un diccionario de python.

Hay funciones especificas de django para gestionar GET y POST

`request.method` por ejemplo: `if request.method == "POST"`

La view decide que hacer segun el metodo.

Si recibo "GET", convierto los datos a JSON y devuelvo jsonResponse().

1. Obtengo los datos del model (`Task.object.all()`)
2. Convierto la lista a diccionario (cada tarea)
3. Devuelvo jsonResponse

Si recibo "POST", leo el `request.body` con `json.loads()`, creo una instancia del objeto y delvuelvo `jsonResponse`.

1. Leo `request.body` con `json.loads()` -> diccionario de datos.
2. Creo la instancia de model. (Task(**data))
3. Lo guardo con `save()`
4. Devuelvo jsonResponse con la tarea creada o mensaje de exito.


## Código ejemplo metodo get


Creamos una lista con diccionarios de los objetos de la DB.

EN el caso de las tareas es algo como :

``` json
[
  {"id": 1, "name": "...", "importance": 2, "completed": false},
  {"id": 2, "name": "...", "importance": 1, "completed": true}
]
```

``` python
def get_tasks(request):
    if (request.method == "GET"):
        lista = list(Task.objects.all().values())
        return JsonResponse(lista, safe=False)
```

creamos una lista y añadimos todos los elementos de la clase de models, esta se tranforma en un QuerySet que corresponde a una lista de diccionarios usando el metodo .values().

Con safe=False indicamos que puee aceptar una lista y no solo un diccionario.

No podemos serializar un QS directamente lo tnemos que convertir a lista para que Json lo pueda leer.



# Creando un serializer


Añado archivo `serializers.py` y creo una clase que hereda de `serialziers.ModelSerializer` esto viene importado de la libreria de rest_framework.

Creo la clase Meta dentro del serializer y le paso dos tipos de datos. 

``` python 
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__' #incluye todos los campos del modelo.

```


Una vez tenemos el serializer he creado una vista api usando el serializer.

# Creando distintas vistas de API

Dentro de views.py, creo una clase que herede de `ListAPIView` y completo los parametros `queryset` y `serializer_class`.

```python 
class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

```

Luego conecto todo en las url


Continuamos con el resto de funciones de HTTP.

Con la plantilla de `ModelViewSet`podemos hacer modificaciones muy facil. Solamente importamos la libreriua necesaria de `rest_framework.viewset`.

USamos el quersyet de antes y el serializer que ya hemos creado para tasks.

```python
class TaskModelViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

```

Vamos a conectar las urls con las clases que hemos creado, para ello usamos un router.

Importamos la libreria correcta en el archivo de urls. Creamos una instancia y registamos el viewset. Añadimos las urls del router a la lista.


Ahora que funciona el en buscador, he creado una nueva tarea con POST.

Para editar una, necesitamos especificar el id en la barra.


# Permisos

He añadido permisos al proyecto global y ademas al ViewSet. Para ello importamos libreria de rest con el permiso que queremos configurar: `from rest_framework.permissions import IsAuthenticated`

Luego he implementado una forma para loguearse y comprobar que funcionan los persmisos, en la url he añadido `    path('api-auth/', include('rest_framework.urls')), ` .
