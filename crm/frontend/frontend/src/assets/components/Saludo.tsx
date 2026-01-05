
type Props = { mensaje: string };
function Saludo(props: Props) {
    return <h1>{props.mensaje}</h1>;
}

export default Saludo;