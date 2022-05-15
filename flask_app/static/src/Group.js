import React, {Component} from 'react';
//import Rating from './Rating';
import Card from 'react-bootstrap/Card'

class Group extends Component {
    render() {
        return(
            <div className='group-box'>
                <h2>{this.props.name}</h2>
                <h3>{this.props.short_description}</h3>
                <p>{this.props.description}</p>
            </div>
        )
    }
}
export default Group