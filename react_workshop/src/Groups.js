import React, {Component} from 'react';
import 'react-bootstrap';
import Group from './Group';

class Groups extends Component {
    constructor(props) {
        super(props);
        this.state = {
            groups: props.groups
        }
    }

    change(props) {
        //this.setState(groups)
    }

    render () {
        const groups = this.state.groups
        const groupList = groups.map(group => <Group
                key = {group.name} {...group} />);
        return(
            <div className='wgroup-container'>
                <h2>Collection of Groups</h2>
                {groupList.length > 0 &&
                    <ul>{groupList}</ul>
                }
                {groupList.length === 0 &&
                    <ul>No Groups to Display.</ul>
                }
            </div>
        )
    }
}
export default Groups
