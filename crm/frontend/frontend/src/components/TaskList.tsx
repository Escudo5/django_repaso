import { useState } from "react";
import { useEffect } from "react";


type Task = {
    id: number;
    title: string;
    description: string;
    project: string;
};

export default function TaskList() {



    const [tasks, setTasks] = useState<Array<Task>>([]);
    const [loading, setLoading] = useState<boolean>(false);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchTasks = async () => {
            setLoading(true);
            setError(null);
            try {
                const response = await fetch('http://localhost:8000/api/tasks/', {
                    headers: {
                        

  return <div><p>Lista de tareas</p></div>;
}
