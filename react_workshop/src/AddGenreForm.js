import React from 'react';
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
            <table>
                <tr>
                    <td>
                        <label>Genre Name: </label>
                    </td>
                    <td>
                        <input ref={input => _name=input}
                            type = 'text'
                            placeholder = "genre name" required />
                    </td>
                </tr>
                <tr>
                    <td>
                        <label>Short Description: </label>
                    </td>
                    <td>
                        <input ref={input => _short_description=input}
                            type = 'text'
                            placeholder = "short description" required />
                    </td>
                </tr>
                <tr>
                    <td>
                        <label>Description: </label>
                    </td>
                    <td>
                        <input ref={input => _description=input}
                            type = 'text'
                            placeholder = "description" required />
                    </td>
                </tr>
            </table>
            <button>Add</button>
        </form>
    )
}
export default AddGroupForm