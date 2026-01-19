import { useState, useRef } from 'react'
import './App.css'
import TaskList from './components/TaskList'
import TaskForm from './components/TaskForm'
import Contador from './components/count'

function App() {
  // Usamos una key para forzar re-render del TaskList
  const [refreshKey, setRefreshKey] = useState(0)

  // Función que se ejecuta cuando se crea una tarea
  const handleTaskCreated = () => {
    // Incrementar la key fuerza al TaskList a recargar
    setRefreshKey(prev => prev + 1)
  }

  return (
    <div className="app-container">
      <header>
        <h1>📝 Gestor de Tareas</h1>
        <p>Conectado con Django REST API</p>
      </header>

      <main>
        {/* Componente Contador para pruebas */}
        <Contador />
        
        {/* Formulario para crear tareas */}
        <TaskForm onTaskCreated={handleTaskCreated} />
        
        {/* Lista de tareas - se recarga cuando cambia refreshKey */}
        <TaskList key={refreshKey} />
      </main>
    </div>
  )
}

export default App
