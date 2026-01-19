import { useState} from "react";

function Contador(){
    const [cuenta, setCuenta] = useState<number>(0);
    
    const sumar = () => setCuenta(cuenta + 1);
    const restar = () => setCuenta(cuenta - 1);

    return(
        <div>
            <h2>Contador: {cuenta}</h2>
            <button onClick={sumar}> Sumar</button>
            <button onClick={restar}> Restar</button>
        </div>
    )
}


export default Contador