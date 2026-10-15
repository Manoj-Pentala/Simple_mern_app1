import { useState } from 'react'

import './App.css'
import Header from './components/Header'
import Footer from './components/footer'
import 'bootstrap/dist/css/bootstrap.min.css'
import Services from './pages/services'
import Home from './pages/Home'
import About from './pages/About'
import Contact from './pages/Contact'
import { Routes, Route } from 'react-router-dom'
import AdminLogin from './pages/AdminLogin'
import AdminHome from './pages/adminhome'



function App() {

  return (
    <div>
      <Header />
      <Routes>
        <Route path='/' element={<Home></Home>}> </Route>
        <Route path='/about' element={<About></About>}> </Route>
        <Route path='/contact' element={<Contact></Contact>}> </Route>
        <Route path='/services' element={<Services></Services>}></Route>
        <Route path='/adminlogin' element={<AdminLogin></AdminLogin>}></Route>
        <Route path='/adminhome' element={<AdminHome></AdminHome>}></Route>

      </Routes>
      <Footer />
    </div>
  )
}

export default App
