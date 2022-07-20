import {makeAutoObservable} from 'mobx';
import data from './list_for_card.json'
export default class LessonsStore{
    constructor(){
        
       
        this._lessons = 0
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