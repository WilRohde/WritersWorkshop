import React, {Component} from 'react';
import 'react-bootstrap';
import Group from './Group';
import './style.css';
import {addGroup} from './Actions'

export const GroupForm = (props, {store}) => {

    let _name, _description, _short_description, _genre, _founding_date

    const submit = e => {
        e.preventDefault()
        store.dispatch( addGroup(_name.value, _short_description.value,_genre.value,_founding_date.value,_description.value))
        _name.value = ''
        _description.value = ''
        _short_description.value = ''
        _genre.value = ''
        _founding_date.value = ''
    }
    return (
    <form className="addGroup" onSubmit={submit}>
        <input ref={input => _name=input}
            type = 'text'
            placeholder = "group name" required />
        <input ref={input => _short_description = input}
                type = 'text'
                placeholder = "short description" required />
        <input ref={input => _genre = input}
                type='text'
                placeholder = "genre" required />
        <input ref={input => _founding_date = input}
                type="date"
                placeholder="founding date" required />
        <input ref={input => _description = input}
                type="textarea"
                placeholder = "description" required />
        <button>Add</button>
    </form>
    )
}
export default GroupForm