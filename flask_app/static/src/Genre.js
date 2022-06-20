import React, {Component} from 'react';
//import Rating from './Rating';
import Card from 'react-bootstrap/Card'

class Genre extends Component {
    render() {
        return(
            <Card>
            <Card.Body>
                <h2>{this.props.name}</h2>
                <h3>{this.props.short_description}</h3>
                <p>{this.props.description}</p>
            </Card.Body>
            </Card>
        )
    }
}
export default Genre