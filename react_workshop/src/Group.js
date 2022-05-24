import React, {Component} from 'react';
import 'react-bootstrap';
import Card from 'react-bootstrap/Card';

class Group extends Component {
    constructor(props) {
        super(props);
        this.state = {
            group: props.group
        }
    }

    render() {
        return (
            <Card>
                <Card.Body>
                    <h5>{this.props.name}</h5>
                    {this.props.GenreName}
                    <p>
                        {this.props.founding_date}
                    </p>
                    <p>
                        {this.props.description}
                    </p>
                    <p>
                        This group has {this.props.count} members.

                    </p>
                </Card.Body>
            </Card>
        );
    }
}
export default Group;