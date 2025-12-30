---

## Filtros en DRF

### ¿Qué son los filtros?
Los filtros te permiten buscar y mostrar solo los datos que te interesan. Por ejemplo, puedes pedir solo las tareas que tienen cierta palabra en el título, o que están marcadas como completadas.

---

### ¿Por qué son útiles?
Imagina que tienes cientos de tareas. Sin filtros, verías todo junto y sería difícil encontrar lo que buscas. Con filtros, puedes pedir solo lo que necesitas y la API te lo da ordenado y limpio.

---

### ¿Cómo se activan los filtros?
DRF trae un sistema de filtros que puedes activar fácilmente:
1. Instala el paquete de filtros:
	```bash
	pip install django-filter
	```
2. Añade el backend de filtros en settings.py:
	```python
	REST_FRAMEWORK = {
		 'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
	}
	```
3. En tu ViewSet, define los campos por los que quieres filtrar:
	```python
	class TaskModelViewSet(ModelViewSet):
		 filterset_fields = ['title', 'completed']
	```

---

### Ejemplo de uso
Si tienes el campo `title`, puedes pedir:
```
/api/tasks/?title=limpiar
```
Y la API te devuelve solo las tareas que tienen "limpiar" en el título.

---

### Esquema visual
```bash
Request con filtro
  ↓
API busca solo lo que pides
  ↓
Respuesta con los datos filtrados
```

---

¿Por qué crees que es útil poder combinar varios filtros? ¿Te gustaría probar a buscar tareas por diferentes campos?
---

## Permisos personalizados en DRF

### ¿Qué es un permiso personalizado?
Es una regla que tú mismo defines para controlar el acceso a tu API según tus propias condiciones. Por ejemplo, solo el creador de una tarea puede editarla.

---

### ¿Cómo se crea?
1. Crea una clase que herede de `BasePermission`.
2. Escribe el método `has_permission` (para acceso general) o `has_object_permission` (para acceso a un objeto concreto).

---

### Ejemplo básico
Supongamos que solo el usuario que creó la tarea puede editarla o borrarla:

```python
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
		def has_object_permission(self, request, view, obj):
				# Solo permite si el usuario es el creador
				return obj.owner == request.user
```

Luego, lo usas en tu ViewSet:
```python
class TaskModelViewSet(ModelViewSet):
		permission_classes = [IsOwner]
		# ...
```

---

### Esquema de flujo
```bash
Request
	↓
¿Es el dueño?
	↓         ↓
Sí        No
	↓         ↓
Sigue    Error 403
```

---

¿Qué tipo de reglas personalizadas crees que podrías necesitar en tu API? ¿Te gustaría probar a crear una?
# Teoría básica de Django REST Framework (DRF)

## ¿Qué es DRF?
Django REST Framework es una biblioteca que facilita la creación de APIs en Django, permitiendo exponer datos de tus modelos en formato JSON y gestionar peticiones HTTP de forma sencilla y segura.

---

## ¿Qué es una API?
Una API (Interfaz de Programación de Aplicaciones) es como un menú en un restaurante: te dice qué puedes pedir y cómo pedirlo. En el contexto web, una API permite que diferentes programas (por ejemplo, tu frontend y tu backend) se comuniquen y compartan datos.

---

## ¿Por qué usar DRF?
DRF te ahorra mucho trabajo repetitivo. En vez de escribir mucho código para convertir datos y manejar peticiones, DRF te da herramientas listas para usar. Además, te ayuda a mantener tu código organizado y seguro.

---

## Serializers
- Un serializer convierte datos complejos (como modelos, QuerySets, objetos Python) en formatos simples (JSON, XML) para enviarlos por la web.
- También valida y transforma datos recibidos en peticiones (por ejemplo, al crear o actualizar objetos).
- Permite definir qué campos se exponen y cómo se procesan.

### Ejemplo sencillo:
Si tienes un modelo de Tarea, el serializer te ayuda a convertirlo en un diccionario que se puede enviar como JSON:

```python
class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = '__all__'
```

Así, DRF sabe cómo transformar tus tareas en datos que el frontend puede entender.

---

## Vistas basadas en clase vs función
- **Vistas basadas en función:** Son funciones que gestionan una petición y devuelven una respuesta. Son simples y directas.
- **Vistas basadas en clase:** Permiten reutilizar y extender comportamientos, agrupar métodos HTTP (GET, POST, etc.) y aprovechar herencia y mixins para lógica común.
- DRF ofrece clases como `APIView`, `ViewSet`, y mixins para operaciones CRUD.

### ¿Por qué usar vistas basadas en clase?
Imagina que tienes muchas operaciones parecidas (listar, crear, borrar tareas). Las vistas basadas en clase te permiten escribir menos código y mantenerlo más limpio. Puedes usar "ViewSets" para que DRF genere automáticamente las funciones necesarias para cada operación.

---

## Routers y URLs
- Los routers de DRF generan automáticamente las rutas para tus vistas, especialmente para los ViewSets.
- Esto ahorra tiempo y evita errores, ya que no tienes que definir cada URL manualmente.
- Ejemplo: Un `TaskViewSet` puede crear rutas para listar, crear, actualizar y borrar tareas automáticamente.

### ¿Qué es un router en DRF?
Un router es como un "GPS automático" para tu API: le dices qué ViewSets tienes y él se encarga de crear todas las rutas necesarias para que puedas listar, crear, editar y borrar objetos sin escribir cada URL a mano.

#### ¿Cómo se usa?
1. Importas el router:
	```python
	from rest_framework.routers import DefaultRouter
	```
2. Creas una instancia:
	```python
	router = DefaultRouter()
	```
3. Registras tu ViewSet:
	```python
	router.register(r'tasks', TaskModelViewSet)
	```
4. Incluyes las URLs del router en tus urlpatterns:
	```python
	from django.urls import include
	urlpatterns += [
		 path('api/', include(router.urls)),
	]
	```

#### ¿Qué rutas te crea automáticamente?
- `/api/tasks/` para listar y crear tareas (GET y POST)
- `/api/tasks/<id>/` para ver, actualizar o borrar una tarea concreta (GET, PUT, PATCH, DELETE)

Así, puedes tener una API completa con muy poco código y sin preocuparte de escribir cada ruta manualmente.

### ¿Cómo funciona un router?
Un router es como un GPS para tu API: le dices qué vistas tienes y él crea las rutas por ti. Así, puedes acceder a tus datos con URLs como `/tasks/` o `/tasks/1/` sin escribir cada ruta a mano.

---

## Permisos y autenticación
- DRF permite definir quién puede acceder a cada endpoint usando clases de permisos.
- Ejemplos: Solo usuarios autenticados, solo administradores, permisos personalizados.
- Es fundamental para proteger los datos y controlar el acceso según roles.

---

## Permisos en DRF

### ¿Qué son los permisos?
Los permisos en DRF son reglas que deciden quién puede hacer qué en tu API. Por ejemplo, puedes permitir que cualquiera vea las tareas, pero solo los usuarios registrados puedan crearlas o borrarlas.

---

### ¿Por qué son importantes?
Imagina que tu API es una casa:
- **Sin permisos:** cualquiera puede entrar, mover cosas, borrar lo que quiera.
- **Con permisos:** solo los invitados pueden entrar, y solo tú puedes cambiar los muebles.

---

### Tipos de permisos en DRF
DRF trae varios permisos listos para usar:

- `AllowAny`: cualquiera puede acceder (no recomendado para datos sensibles).
- `IsAuthenticated`: solo usuarios registrados pueden acceder.
- `IsAdminUser`: solo administradores pueden acceder.
- `IsAuthenticatedOrReadOnly`: cualquiera puede ver, pero solo usuarios registrados pueden modificar.

También puedes crear tus propios permisos personalizados.

---

### ¿Dónde se configuran los permisos?
Puedes poner permisos a nivel global (para toda la API) o solo en una vista o ViewSet.

#### Global (en settings.py):
```python
REST_FRAMEWORK = {
		'DEFAULT_PERMISSION_CLASSES': [
				'rest_framework.permissions.IsAuthenticated',
		]
}
```

#### Por vista:
```python
from rest_framework.permissions import IsAuthenticated

class TaskModelViewSet(ModelViewSet):
		permission_classes = [IsAuthenticated]
		# ...
```

---

### Esquema de flujo de permisos

```bash
Request
	↓
Permiso global (settings.py)
	↓
Permiso en la vista (si hay)
	↓
¿Tiene permiso?
	↓         ↓
Sí        No
	↓         ↓
Sigue    Error 403
```

---

### Ejemplo práctico
Si pones `IsAuthenticated` en tu ViewSet, solo los usuarios logueados podrán crear, editar o borrar tareas. Si no estás logueado, verás un error 403 (prohibido).

---

¿Por qué crees que es útil tener permisos a diferentes niveles? ¿Qué ventajas tiene poder combinarlos?

¿Te gustaría probar a proteger tu API para que solo usuarios autenticados puedan modificar datos?

### ¿Por qué es importante?
No quieres que cualquiera pueda borrar o modificar tus datos. Los permisos te ayudan a decidir quién puede hacer qué. Por ejemplo, solo el dueño de una tarea puede editarla, o solo los administradores pueden borrar datos.

---

## Documentación y exploración
- DRF incluye una interfaz web para explorar y probar tu API (Browsable API).
- Facilita la documentación automática y la interacción para desarrolladores y testers.

### ¿Qué es la Browsable API?
Es una página web que DRF genera automáticamente donde puedes probar tu API, ver los datos y enviar peticiones sin necesidad de usar herramientas externas. Es muy útil para aprender y para depurar errores.

---

## Métodos HTTP principales
- **GET:** Pedir datos (como ver la lista de tareas)
- **POST:** Crear nuevos datos (añadir una tarea)
- **PUT/PATCH:** Modificar datos existentes (editar una tarea)
- **DELETE:** Borrar datos

---

## Buenas prácticas con DRF
- Define bien tus serializers para controlar qué datos expones.
- Usa permisos para proteger tu API.
- Aprovecha los routers y ViewSets para escribir menos código repetitivo.
- Prueba tu API con la Browsable API antes de conectar el frontend.

---

## ¿Cómo empezar?
1. Instala DRF: `pip install djangorestframework`
2. Añade `'rest_framework'` a tu `INSTALLED_APPS` en `settings.py`
3. Crea un serializer para tu modelo.
4. Crea una vista API (puedes usar ViewSet para más comodidad).
5. Registra la vista en un router y añade el router a tus URLs.
6. Prueba tu API en el navegador.

---

---

## Recursos recomendados
- [Documentación oficial DRF](https://www.django-rest-framework.org/)
- Tutoriales y ejemplos en la web oficial
- Prueba crear un serializer, una vista API y explora la interfaz web

---

¿Te gustaría que te proponga ejercicios prácticos para cada concepto, o prefieres seguir profundizando en la teoría primero?
