
import {Routes, Route, Navigate} from 'react-router-dom'
import {publicRoutes} from "../../routes";
import LessonsList from '../LessonsList/LessonsList';


const AppRouter = () => {
   


    return (
        <Routes>
            
            {publicRoutes.map(({path, Component}) =>
                <Route key={path} path={path} element={<Component/>} exact/>
            )}
            <Route path="/" />
            <Route path="/login" />
        </Routes>
    );
};

export default AppRouter;