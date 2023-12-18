import React from 'react'
import { useState } from 'react';
import { Routes, Route, Link, Outlet } from 'react-router-dom';

const Router = () => {
    const [isLogin,setIslogin] = useState(false)
  return (
    <Routes>
        <Route path="/" element={<>
      <nav>
        <ul>
          <li>
            <Link to="/">login</Link>
          </li>
          <li>
            <Link to="/register">register</Link>
          </li>
          <li>
            <Link to="/home">home</Link>
          </li>
        </ul>
      </nav>

      <Outlet />
    </>}>
            <Route index element={<h1> login</h1>} />
            <Route path="login" element={<h1> login</h1>} />
            <Route path="register" element={<h1> register</h1>} />
            <Route path="home" element={<h1> home</h1>} />
            <Route path="*" element={<p>There's nothing here: 404!</p>} />
        </Route>
        <Route path="*" element={<p>There's nothing here: 404!</p>} />
    </Routes>
  )
}

export default Router