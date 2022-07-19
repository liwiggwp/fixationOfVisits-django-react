import 'bootstrap/dist/css/bootstrap.min.css';

import React, {useContext, useEffect, useState} from "react";
import {observer} from "mobx-react-lite";
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { AuthProvider } from './context/AuthContext'
import {Context} from "./index";

import HomePage from './pages/HomePage'
import LoginPage from './pages/LoginPage'
import Header from './components/Header/Header'
import LessonsList from './components/LessonsList/LessonsList'
import AppRouter from './components/AppRouter/AppRouter'

const App = observer(() => {
  const {user} = useContext(Context)
const [loading, setLoading] = useState(true)
  return (
    <div className="App">
      <BrowserRouter>
        <AuthProvider>
          <Header />

          <AppRouter />
          <Routes>
            <Route path="/"
              element={
                <LessonsList />}
              exact />
            <Route path="/login" element={<LoginPage />} />
          </Routes>
        </AuthProvider>
      </BrowserRouter>
    </div>
  )
})

export default App