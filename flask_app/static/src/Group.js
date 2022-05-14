import React, {Component} from 'react';
//import Rating from './Rating';
import Card from 'react-bootstrap/Card'

class Group extends Component {
    render() {
        return(
            <h2>{this.props.name}</h2>
        )
    }
}
export default Group