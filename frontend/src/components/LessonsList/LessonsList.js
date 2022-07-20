
import './LessonsList.css';
import {Button, Card} from "react-bootstrap";
import React, {useContext} from "react";
import { Link } from "react-router-dom";
import CardLesson from '../CardLesson/CardLesson'
import {Context} from '../../index'
import {Row} from 'react-bootstrap'
import {observer} from 'mobx-react-lite'

const LessonsList = observer(() => {
  const {lesson} = useContext(Context)
 
  return (
    <Row>
         {/* {lesson.lessons.map(lesson=> */}
            <CardLesson key={lesson.id} lesson={lesson}/>
              
                
        {/* )} */}
        
    </Row>
  );
})

export default LessonsList;
