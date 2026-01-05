

## Ejemplo práctico: Contador con useState y eventos

```tsx
import { useState } from "react";

function Contador() {
  // Creamos una variable de estado llamada "cuenta" y una función para cambiarla
  const [cuenta, setCuenta] = useState<number>(0);

  // Funciones para manejar los eventos de los botones
  const sumar = () => setCuenta(cuenta + 1);
  const restar = () => setCuenta(cuenta - 1);

  return (
    <div>
      <h2>Contador: {cuenta}</h2>
      <button onClick={sumar}>Sumar</button>
      <button onClick={restar}>Restar</button>
    </div>
  );
}
```

- `useState<number>(0)` crea el estado inicial en 0 y lo tipa como número.
- `onClick={sumar}` y `onClick={restar}` son eventos que llaman a las funciones para cambiar el estado.
- Cada vez que haces clic, el estado cambia y el componente se actualiza.

¿Te gustaría probar a crear este componente y usarlo en tu App.tsx?


## ¿Qué es el estado (state) en React?

El estado es una forma de que un componente "recuerde" información entre renderizados. Por ejemplo, un contador, el texto de un input, o una lista de tareas.

Cuando el estado cambia, el componente se vuelve a renderizar automáticamente para mostrar el nuevo valor.

---

## ¿Qué es useState?

`useState` es un hook de React que te permite añadir estado a un componente funcional.

- Te da una variable con el valor actual y una función para cambiarlo.
- Cuando usas la función para cambiar el estado, React actualiza la interfaz.

**Ejemplo de uso básico:**
```tsx
import { useState } from "react";

const [contador, setContador] = useState(0);
```
- `contador` es el valor actual.
- `setContador` es la función para cambiarlo.
- El valor inicial es 0.

---


## Ejemplos de tipos en TypeScript para React

### 1. Tipar props de un componente
```tsx
type Props = { mensaje: string };
function Saludo(props: Props) {
  return <h1>{props.mensaje}</h1>;
}
// Uso:
// <Saludo mensaje="¡Hola, mundo!" />
```

---

### 2. Tipar variables
```tsx
let nombre: string = "Juan";
let edad: number = 30;
let tareas: string[] = ["leer", "escribir"];
```

---

### 3. Tipar el estado con useState
```tsx
import { useState } from "react";

// Estado simple
const [contador, setContador] = useState<number>(0);

// Estado con un objeto
type Task = { id: number; title: string };
const [tarea, setTarea] = useState<Task>({ id: 1, title: "Aprender React" });

// Estado con un array de objetos
const [tareas, setTareas] = useState<Task[]>([]);
```

---

### 4. Tipar funciones
```tsx
function suma(a: number, b: number): number {
  return a + b;
}
```

---

**Resumen:**
- Usa `type` o `interface` para definir la forma de los datos.
- Usa los tipos en props, variables, estado y funciones para que tu código sea más seguro y fácil de entender.

¿Te gustaría practicar creando un componente que reciba props y maneje estado tipado?
# Teoría básica de React + TypeScript

---

## 1. Estructura inicial de un proyecto React + TypeScript (Vite)

Cuando creas un proyecto con Vite y la plantilla `react-ts`, se genera una estructura como esta:

```
frontend/
  ├─ public/           # Archivos estáticos (index.html, favicon, etc.)
  ├─ src/              # Código fuente de la app
  │   ├─ assets/       # Imágenes y recursos
  │   ├─ App.tsx       # Componente principal de la app
  │   ├─ main.tsx      # Punto de entrada de React
  │   └─ ...           # Otros archivos
  ├─ index.html        # HTML principal
  ├─ package.json      # Dependencias y scripts
  ├─ tsconfig.json     # Configuración de TypeScript
  ├─ vite.config.ts    # Configuración de Vite
```

### ¿Por qué esta estructura?
- **Separación de responsabilidades:**
  - `public/` contiene archivos que no cambian y se copian tal cual al build final.
  - `src/` contiene todo el código que tú escribes y que React va a "interpretar".
- **Facilita el mantenimiento y la escalabilidad.**

### Archivos clave
- `App.tsx`: El componente raíz de tu aplicación. Aquí puedes empezar a construir tu interfaz.
- `main.tsx`: El punto de entrada donde React "monta" la app en el HTML.
- `package.json`: Lista las dependencias y scripts útiles (como `npm run dev`).
- `tsconfig.json`: Define cómo se comporta TypeScript en tu proyecto.

---

## 2. Primeros pasos tras la instalación

1. Entra en la carpeta del frontend:
   ```bash
   cd frontend
   ```
2. Instala las dependencias:
   ```bash
   npm install
   ```
3. Arranca el servidor de desarrollo:
   ```bash
   npm run dev
   ```
4. Abre el navegador en la URL que te indica la terminal (normalmente http://localhost:5173).

---

## 3. ¿Qué es un componente en React?
Un componente es como una "pieza" de la interfaz. Puede ser tan simple como un botón o tan complejo como una página entera.

**Ejemplo básico:**
```tsx
function Saludo() {
  return <h1>¡Hola, React!</h1>;
}
```

**¿Por qué usar componentes?**
- Permiten reutilizar código.
- Hacen que la interfaz sea más fácil de entender y mantener.

---

## 4. ¿Qué es JSX?
JSX es una "mezcla" de JavaScript y HTML. Permite escribir HTML dentro de tu código JS/TS de forma sencilla.

**Ejemplo:**
```tsx
const elemento = <h2>Esto es JSX</h2>;
```

---

## 5. ¿Qué es TypeScript y por qué usarlo en React?
TypeScript añade tipos a JavaScript. Esto ayuda a:
- Evitar errores tontos (por ejemplo, pasar un número donde esperabas un texto).
- Saber qué datos espera cada componente.
- Mejorar la autocompletación y la documentación del código.

**Ejemplo de tipo en una prop:**
```tsx
type Props = { mensaje: string };
function Saludo(props: Props) {
  return <h1>{props.mensaje}</h1>;
}
```

---

## 6. Ejercicio práctico: Tu primer componente

1. Crea un archivo `Saludo.tsx` en la carpeta `src/components/`.
2. Escribe un componente que reciba un mensaje por props y lo muestre en pantalla.
3. Importe y usa ese componente en `App.tsx`.

**Reflexiona:**
- ¿Por qué crees que es útil dividir la interfaz en componentes?
- ¿Qué ventajas ves en usar tipos para las props?

---

## 7. Siguiente paso: Estado y eventos
¿Te gustaría que te explique cómo manejar el estado (`useState`) y los eventos en React, o prefieres practicar primero con componentes y props?

## ¿Qué es React?
React es una librería de JavaScript para construir interfaces de usuario de forma rápida y modular. Permite crear componentes reutilizables que se actualizan automáticamente cuando cambian los datos.

---

## ¿Por qué usar TypeScript?
TypeScript es un "superconjunto" de JavaScript que añade tipos. Esto ayuda a evitar errores y hace el código más fácil de mantener y entender.

---

## Estructura típica de carpetas para un proyecto React + TypeScript

```
frontend/
  ├─ public/           # Archivos estáticos (index.html, favicon, etc.)
  ├─ src/              # Código fuente de la app
  │   ├─ components/   # Componentes reutilizables
  │   ├─ pages/        # Vistas principales (Home, Dashboard, etc.)
  │   ├─ hooks/        # Custom hooks (lógica reutilizable)
  │   ├─ types/        # Definiciones de tipos TS
  │   ├─ services/     # Funciones para conectar con la API
  │   ├─ App.tsx       # Componente principal
  │   ├─ index.tsx     # Punto de entrada
  ├─ package.json      # Dependencias y scripts
  ├─ tsconfig.json     # Configuración de TypeScript
  ├─ README.md         # Documentación del frontend
```

---

## ¿Cómo se conecta el frontend con el backend?

El frontend (React) hace peticiones HTTP (fetch, axios) a la API REST de Django para obtener o enviar datos. Por ejemplo, puedes pedir la lista de tareas en `/api/tasks/` y mostrarla en React.

**Pistas para integración:**
- Asegúrate de que Django permita peticiones desde el frontend (CORS).
- Usa rutas relativas o variables de entorno para la URL de la API.
- Piensa: ¿cómo manejarías el login/logout desde React usando la API de Django?

---

## Conceptos clave de React
- **Componente:** Bloque de construcción de la interfaz. Puede ser una función o una clase.
- **Props:** Datos que se pasan a los componentes.
- **State:** Datos internos que pueden cambiar y hacen que el componente se actualice.
- **Hook:** Función especial para usar lógica de React (por ejemplo, `useState`, `useEffect`).

---

## Conceptos clave de TypeScript en React
- **Tipo:** Define qué forma tienen los datos (por ejemplo, un objeto Task).
- **Interfaz:** Forma de definir tipos complejos para props, state, etc.
- **Props tipadas:** Así React sabe qué datos espera cada componente.

---


Segun entiendo, props son como objetos que creas con propiedades que luego le vas a pasar a las funciones.




















































---

# Planning de 2 días: React + TypeScript + Django API

## Día 1: Fundamentos y conexión con Django

**Hora 1: Repaso teórico y primeros pasos**
- ¿Qué es React? ¿Qué es TypeScript? ¿Cómo se comunican con Django?
- Diferencia entre componentes de función y clase.
- ¿Qué es JSX?
- Instala un proyecto React+TS (Vite recomendado) dentro de la carpeta frontend.
- Ejercicio: Crea un componente funcional simple y muéstralo en pantalla.

**Hora 2: Componentes, Props y State**
- Crea un componente funcional que reciba props tipadas.
- Usa `useState` para manejar estado.
- Ejercicio: Crea un contador con botones + y -.

**Hora 3: Eventos y listas**
- Maneja eventos (onClick, onChange).
- Renderiza una lista de tareas (array en el estado).
- Ejercicio: Muestra una lista de tareas y permite añadir una nueva tarea localmente.

**Hora 4: Tipos e interfaces en TS**
- Define tipos e interfaces para props y state (por ejemplo, una tarea: id, title, completed).
- Refactoriza los componentes anteriores usando interfaces para las props.
- Ejercicio: Crea una interfaz Task y úsala en la lista de tareas.

---

## Día 2: Hooks, conexión con Django y mini-CRUD

**Hora 1: useEffect y fetch a la API de Django**
- ¿Qué es `useEffect`? ¿Para qué sirve?
- Haz un fetch a `/api/tasks/` de Django y muestra los datos en React.
- Ejercicio: Muestra la lista de tareas reales desde la API.

**Hora 2: Añadir tareas a Django desde React**
- ¿Cómo hacer un POST a la API de Django?
- Ejercicio: Crea un formulario en React para añadir una tarea usando la API.

**Hora 3: Borrar y actualizar tareas**
- ¿Cómo hacer DELETE y PUT/PATCH a la API?
- Ejercicio: Permite borrar y editar tareas desde React usando la API de Django.

**Hora 4: Repaso, dudas y mini-proyecto**
- Organiza el código en carpetas: components, hooks, types, services.
- Mini-proyecto: App de tareas conectada a Django (listar, crear, borrar, editar).
- Apunta dudas y conceptos clave.

---

## Ejercicios prácticos y método socrático
En cada bloque, reflexiona:
- ¿Por qué crees que React y Django se comunican así?
- ¿Qué ventajas tiene usar tipos en los datos que viajan entre frontend y backend?
- ¿Cómo manejarías los errores de red o validación?

¿Te gustaría que te proponga ejercicios paso a paso para cada bloque, o prefieres que te explique primero la teoría antes de practicar?