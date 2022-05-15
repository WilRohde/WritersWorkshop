import { Formik, Form, Field, ErrorMessage } from 'formik';
import React, {Component} from 'react';
import axios from 'axios';
import GitHubUsers from './GitHubUsers';
handleChange(e) {
    this.setState({searchTerm: e.target.value});
}

class Register extends Component {
    constructor (props) {
        super(props);
    }
    // event handlers
    handleFirstNameChange(e) {
        this.setState({firstname: e.target.value});
    }
    handleLastNameChange(e) {
        this.setState({lastname: e.target.value});
    }
    handleUsernameChange(e) {
        this.setState({username: e.target.value});
    }
    handleEmailChange(e) {
        this.setState({email: e.target.value});
    }
    handlePasswordChange(e) {
        this.setState({email: e.target.value});
    }
    handlePasswordConfirmChange(e) {
        this.setState({passwordConfirm: e.target.value});
    }

    render() {
        return (
            <div>
                <h3>Enter your Information</h3>
                <input placeholder="First Name" onChange={this.handleFirstNameChange}/>
                <input placeholder="Last Name" onChange={this.handleLastNameChange}/>
                <input placeholder="Username" onChange={this.handleUsernameChange}/>
                <input placeholder="Email" onChange={this.handleEmailChange}/>
                <input placeholder="Password" type="password" onChange={this.handlePasswordChange}/>
                <input placeholder="Confirm Password" type="password" onChange={this.handleConfirmPasswordChange}/>
                <button onClick="{this.handleClick">Submit</button>
            </div>

        )
    }
}