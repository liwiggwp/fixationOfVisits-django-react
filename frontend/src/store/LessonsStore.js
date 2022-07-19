import {makeAutoObservable} from 'mobx';

export default class LessonsStore{
    constructor(){
        this._lessons = [
            {
                'id': 1,
                'title': 'КЗ',
                'modul': 'Проектная работа',
                'time': '8:30 - 10:15',
                'teacher': 'Ступников Алексей Анатольевич'
            },
            {
                'id': 2,
                'title': 'КЗ',
                'modul': 'Глубокое обучение с подкреплением',
                'time': '10:30 - 12:00',
                'teacher': 'Аврискин Михаил Владимирович'
            },
            {
                'id': 3,
                'title': 'АТПРВ',
                'modul': 'Параллелизм данных. Класс Parallel',
                'time': '12:30 - 14:00',
                'teacher': 'Ромазанов Артур Ринатович'
            }

        ]
        this._selectedLesson = {}


    }

    setLesson(lessons){
        this._lessons = lessons
    }
    get lessons(){
        return this._lessons
    }
    setSelectedLesson(lesson){
        this._selectedLesson = lesson
    }

}