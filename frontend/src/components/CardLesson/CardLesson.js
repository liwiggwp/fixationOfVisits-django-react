import Model from './Model'
import './CardLesson.css';
import { Button, ListGroup, Card, Col } from "react-bootstrap";

import { useNavigate } from "react-router-dom"
import React, { useState } from 'react';

const lesson = require('../../store/list_for_card.json');


const CardLesson = () => {
  const [model, setModel] = useState(false)
  const [tempData, setTempdata] = useState([])

  const getData = (subject, modul, student) => {
    let tempData = [subject, modul, student]
    setTempdata(item => [1, ...tempData])
    return setModel(true)
  }
  return (
    <>
      <section className='py-4 py-lg-5 container'>
        <div className='row justify-content-center align-item-center'>
          {lesson.map((item, index) => {
            return (
              <div className='col-11 col-md-6 col-lg-3 mx-0 mb-4' key={index}>
                <div className='card p-0 overflow-hidden h-100 shadow'>
                  <div className='card-body'>
                    <h4 className='card-title'>{item.subject}</h4>
                    <p className='card-text'>{item.modul}</p>
                    <h6 className='card-title'>Время:</h6>
                    <p className='card-title'>{item.time}</p>
                    <h6 className='card-title'>Преподаватель:</h6>
                    <p className='card-title'>{item.teacher[1]}</p>
                    <button className='btn btn-primary'
                      onClick={() => getData(item.subject, item.modul, item.student[1])}>Показать</button>
                  </div>
                </div>
              </div>
            )
          }
          )}
        </div>
      </section>
      {
        model === true ? <Model subject={tempData[1]} modul={tempData[2]} student={tempData[3]} hide={() => setModel(false)} /> : ''
      }
    </>
  )

}


export default CardLesson;
