import ListGroup from "./components/ListGroup";
import Alert from "./components/Alert";
import Button from "./components/Button";
import { useState } from "react";

function App() {
  const items = [
    'New York',
    'Budapest',
    'London',
    'Paris',
    'Tokyo'
  ];

  const [alertVisible, setAlertVisibility] = useState(false);

  const handleClick = () => {
    setAlertVisibility(true);
  }

  const handleClose = () => {
    setAlertVisibility(false);
  }

  return <div>
    <ListGroup items={items} heading="Cities"></ListGroup>
    <Button onClick={() => console.log("click")} color="success">Success</Button>
    { alertVisible === true && <Alert onClose={handleClose}>My alert</Alert> }
    <Button onClick={handleClick}>Primary</Button>
  </div>;
}

export default App;