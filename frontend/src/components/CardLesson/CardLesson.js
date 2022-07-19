
import './CardLesson.css';
import {Button, Card, Col} from "react-bootstrap";

import {useNavigate} from "react-router-dom"


const CardLesson = ({lesson}) =>{
 
  return (
  
    <Col md={3}>
      <Card style={{width: 300, cursor: 'pointer', margin: 20 }} border={"primary"}>
        <Card.Body>
          <Card.Title>{lesson.title}</Card.Title>
          <Card.Title>{lesson.modul}</Card.Title>
          
          <Card.Text>
              {lesson.time}
          </Card.Text>
          <Card.Text>
              Преподаватель: {lesson.teacher}
          </Card.Text>
        
        </Card.Body>
      </Card>
    </Col>
  );
}

export default CardLesson;
