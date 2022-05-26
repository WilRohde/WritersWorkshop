import React, {Component} from 'react';
import 'react-bootstrap';
import Group from './Group';
import fetch from 'isomorphic-fetch';
import './style.css';

class Groups extends Component {
    constructor(props) {
        super(props);
        this.state = {
            groups: [],
            loading: false
        }
    }

    // 05/25/2022 - have to uncomment and get this working...
    // componentDidMount() {
    //     this.setState({loading: true})
    //     const api = 'http://localhost:5000/api/group/all'
    //     const request = fetch(api,{
    //         method: 'GET',
    //         headers: {
    //             'Content-Type': 'text/html',
    //             'Origin': "http:/WritersWorkshop/testApi.html"
    //         },
    //     })
    //         .then(response => response.json())
    //         .then(data => {buildGroups(data)})
    //         .then(groups => 
    //             this.state({groups, loading: false}))
    //         .catch(error => console.log(error))
    // }

    // buildGroups(answer) {
    //     console.log(answer)
    //     var groups = []
    //     for (k=0; k <= answer.count-1; k++) {
    //         groups[k] = answer.groups[k] // build array
    //     }
    //     return groups
    // }

    componentDidMount() {
        const myGroups = [{
            name: 'Yo Ho Hokum',
            GenreName: 'Pirates',
            founding_date: '05/16/2020',
            description: 'Lots of goofy pirate weirdness',
            count: 2
          },
          {
            name: "Sci Fi Rangers",
            GenreName: 'Science Fiction',
            founding_date: '08/13/2010',
            description: 'sci fi foolishness',
            count: 11
            
          }
        ]
        this.setState({groups: myGroups})
    }

    render () {
        const groups = this.state.groups
        const groupList = groups.map(group => <Group
                key = {group.name} {...group} />);
        console.log(groupList)
        return(
            <div className="items-box">
                <h2>Your Groups</h2>
                    {groups.length > 0 &&
                        <div className='groups-container'>
                            {groups.map(group => 
                            <Group key = {group.name} {...group} />)}
                        </div>
                    }
                    {groups.length === 0 &&
                        <p>No Groups to Display.</p>
                    }
            </div>
        )
    }
}
export default Groups
