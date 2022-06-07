import React from 'react';
import { render } from 'react-dom';

import {
    BrowserRouter,
    Link,
} from 'react-router-dom'
import App from './App.js';

import {
    About,
    Dashboard
} from './Pages'

import Screen from './Screen'

window.React = React

render (
    <BrowserRouter>
        <div className="main">
        <Link to="/invoices">Invoices</Link> |{" "}
        <Link to="/expenses">Expenses</Link>
        </div>
    </BrowserRouter>,
    document.getElementById('root')
)
export default App
