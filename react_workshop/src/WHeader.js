import React, {Component} from 'react';
import 'react-bootstrap'
import './App.css'
import './style.css'

export const WHeader = (props)  =>
// {
//     return(
    <div className="ws-header">
        <h2>Hello {props.authorName.firstname} {props.authorName.lastname} !</h2>
        <p>
            Edit <code>src/App.js</code> and save to reload.
        </p>
    </div>
//     )
// }
export default WHeader
