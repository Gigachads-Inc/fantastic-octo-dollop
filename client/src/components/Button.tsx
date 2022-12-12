type ButtonProps = {
    handleClick: () => void
}
export const Button = (props: ButtonProps) => {
    return (
        <button onClick={props.handleClick} className="submit-button"> Click me :3 </button>
    )
}