import 'bootstrap/dist/css/bootstrap.min.css';

import React, {useContext, useEffect, useState} from "react";
import {observer} from "mobx-react-lite";
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import  AuthProvider from './context/AuthContext'
import {Context} from "./index";

import PrivateRoute from './utils/PrivateRoute'
import LoginPage from './pages/LoginPage'
import Header from './components/Header/Header'
import LessonsList from './components/LessonsList/LessonsList'

const App = observer(() => {
const {user} = useContext(Context)
const [loading, setLoading] = useState(true)
  return (    
    <div className="App">      
      <BrowserRouter>
        <AuthProvider>
          <Header />
          <Routes>
          <Route path="/"
              element={<PrivateRoute>
                <LessonsList />
                </PrivateRoute>}
              exact />
            <Route path="/login" element={<LoginPage />} />
          </Routes>
        </AuthProvider>
      </BrowserRouter>
    </div>
  )
})

export default App


