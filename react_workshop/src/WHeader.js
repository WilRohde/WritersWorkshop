import React, {Component} from 'react';
import 'react-bootstrap'
import './App.css'
import './style.css'

class WHeader extends Component {
    constructor (props) {
        super(props)
        this.state = {
            firstname: props.author.firstname,
            lastname: props.author.lastname
        }
        console.log(this.state.firstname + "  " + this.state.lastname)
    }
    change(firstname, lastname) {
        this.setState(this.firstname = firstname)
        this.setState(this.lastname = lastname)
    }
    render() {
        return(
            <header className="ws-header">
                <h2>Hello {this.state.firstname} {this.state.lastname} !</h2>
                <p>
                    Edit <code>src/App.js</code> and save to reload.
                </p>
            </header>
        )
    }
}
export default WHeader
