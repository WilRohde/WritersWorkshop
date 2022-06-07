import React, {Component} from 'react';
import 'react-bootstrap';
import './style.css';
import {addGenre} from './Actions'

export const AddGroupForm = (props,{store}) => {
    let _id, _name, _short_description, _description

        const submit = e => {
        e.preventDefault()
        store.dispatch( addGenre(_name.value, _short_description.value, _description.value))
        _name.value = ''
        _description.value = ''
        _short_description.value = ''
    }
    return(
        <form className="addGenre" onSubmit={submit}>
            <input ref={input => _name=input}
                type = 'text'
                placeholder = "genre name" required />
            <input ref={input => _short_description=input}
                type = 'text'
                placeholder = "short description" required />
            <input ref={input => _description=input}
                type = 'text'
                placeholder = "description" required />
            <button>Add</button>
        </form>
    )
}
export default AddGroupForm