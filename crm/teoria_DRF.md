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
