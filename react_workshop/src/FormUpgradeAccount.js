import React from 'react';
import 'react-bootstrap';
import './style.css';
import {upgradeAccount} from './Actions'

export const FormUpgradeAccount = (props,{store}) => {
    let _id, _firstname, _mi, _lastname, _address1, _address2, _city, _state, _zip, _creditcard, _securitynumber, _expiration

        const submit = e => {
        e.preventDefault()
        store.dispatch( upgradeAccount(_firstname.value, _mi.value, _lastname.value, _address1.value, _address2.value, _city.value, _state.value, _zip.value, _creditcard.value, _securitynumber.value, _expiration.value))
        _firstname.value = ""
        _mi.value.value = ""
        _lastname.value = ""
        _address1.value = ""
        _address2.value = ""
        _city.value = ""
        _state.value = ""
        _zip.value = ""
        _creditcard.value = ""
        _securitynumber.value = ""
        _expiration.value = ""
    }
    return(
        <form className="upgradeAccount" onSubmit={submit}>
            <tabel>
                <tr>
                    <td>
                        <label>First Name: </label>
                    </td>
                    <td>
                        <input ref={input => _firstname=input}
                            type = 'text'
                            placeholder = "first name" required />
                    </td>
                    <td>
                        <label>Middle Initial: </label>
                    </td>
                    <td>
                        <input ref={input => _mi=input}
                            type = 'text'
                            placeholder = "middle initial" required />
                    </td>
                    <td>
                        <label>Last Name: </label>
                    </td>
                    <td>
                        <input ref={input => _lastname=input}
                            type = 'text'
                            placeholder = "last name" required />
                    </td>
                </tr>
                <tr>
                    <td>
                        <label>Address Line 1: </label>
                    </td>
                    <td>
                        <input ref={input => _address1=input}
                            type = 'text'
                            placeholder = "address line 1" required />
                    </td>
                </tr>
                <tr>
                    <td>
                        <label>Address Line 2: </label>
                    </td>
                    <td>
                        <input ref={input => _address2=input}
                            type = 'text'
                            placeholder = "address line 2" />
                    </td>
                </tr>
                <tr>
                    <td>
                        <label>City: </label>
                    </td>
                    <td>
                        <input ref={input => _city=input}
                            type = 'text'
                            placeholder = "city" required />
                    </td>
                    <td>
                        <label>State: </label>
                    </td>
                    <td>
                        <input ref={input => _state=input}
                            type = 'text'
                            placeholder = "state" required />
                    </td>
                    <td>
                        <label>Zip Code: </label>
                    </td>
                    <td>
                        <input ref={input => _zip=input}
                            type = 'text'
                            placeholder = "state" required />
                    </td>
                </tr>
                <tr>
                    <td>
                        <label>Credit Card Number: </label>
                    </td>
                    <td>
                        <input ref={input => _creditcard=input}
                            type = 'text'
                            placeholder = "credit card number" required />
                    </td>
                    <td>
                        <label>Security Code: </label>
                    </td>
                    <td>
                        <input ref={input => _securitynumber=input}
                            type = 'text'
                            placeholder = "security code" required />
                    </td>
                    <td>
                        <label>Expiration Date: </label> 
                    </td>
                    <td>
                        <input ref={input => _expiration=input}
                            type = 'text'
                            placeholder = "expiration date" required />
                    </td>
                </tr>
            </tabel>

            <button>Add</button>
        </form>
    )
}
export default FormUpgradeAccount