

export const Button = () => {
    const handleClick = () => {
        console.log("Clicking...");
    }


    return (
        <button onClick={handleClick} className="submit-button"> Click me :3 </button>
    )
}