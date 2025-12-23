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

SUpongamos que creamos una app de tareas, podemos crearlas con los atributos: nombre, fecha, importancia y booleano de completado.
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

1. Leo `requet.body` con `json.loads()` -> diccionario de datos.
2. Creo la instancia de model. (Task(**data))
3. Lo guardo con `save()`
4. Devuelvo jsonResponse con la tarea creada o mensaje de exito.