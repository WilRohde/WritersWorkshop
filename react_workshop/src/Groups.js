import React, {useState, useEffect} from 'react';
import 'react-bootstrap';
import Group from './Group';
import './style.css';
import {fetchGroups} from './APIFunctions'

export const Groups = () => {
    const [groups, setGroups] = useState([])
    const [loading, setLoading] = useState(true)
    useEffect(() => {
        fetchGroups(setGroups,setLoading);
    }, [])

    return (
        <div className="items-box">
        <h2>Groups</h2>
            {loading === true &&
                <p>Loading Groups...</p>}
            {(groups.length > 0) & (loading===false) &&
                <div className='groups-container'>
                    {groups.map(group => 
                    <Group key = {group.name} {...group} />)}
                </div>
            }
            {(groups.length === 0) & (loading===false) &&
                <p>There are no Groups to Display.</p>
            }
    </div>
    )
}
export default Groups