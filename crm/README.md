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