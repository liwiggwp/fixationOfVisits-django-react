
import './OneCard.css';
import {Button, Card} from "react-bootstrap";

function OneCard(props) {
  return (
    <div style={{ display: 'flex' }} className="App">
      <Card xs={7} style={{ width: '300px'}} className="bg-black text-white">
     
      
        <Card.Title>{props.title}</Card.Title>
        <Card.Text>{props.modul}</Card.Text>
        <Card.Text>{props.time}</Card.Text>
      
      </Card>
    </div>
  );
}

export default OneCard;
