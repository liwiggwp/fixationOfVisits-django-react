import React, {createContext} from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import LessonsStore from "./store/LessonsStore";


export const Context = createContext(null)

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Context.Provider value={{
  lesson: new LessonsStore(),
  }}>
  <App/>
  </Context.Provider>
);