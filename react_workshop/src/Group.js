import React, {Component} from 'react';
import 'react-bootstrap';

class Group extends Component {
    constructor(props) {
        super(props);
        this.state = {
            group: props.group
        }
    }

    render() {
        return (
            <div className="item-box">
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
            </div>
        );
    }
}
export default Group;