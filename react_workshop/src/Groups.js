import React, {useState, useEffect} from 'react';
import 'react-bootstrap';
import Group from './Group';
import fetch from 'isomorphic-fetch';
import './style.css';
import Axios from 'axios';

const apiurl = 'http://localhost:5000/api/'
const origin = "http:/WritersWorkshop/testApi.html"

export const Groups = (props) => {
    const [groups,setGroups] = useState([])
    useEffect(() => {
        fetchGroups();
    }, [])
    const fetchGroups = async() =>{
        const api = apiurl + 'group/all'
        const response = await fetch(api,{
            method: 'GET',
            headers: {
                'Content-Type': 'text/html',
                'Origin': origin
            },
        })
        const answer = await response.json()
        console.log(answer);
        const groups = await buildGroups(answer)
        setGroups(groups)
    }
    const buildGroups = async(answer) => {
        var groups = []
        for (let k=0; k <= answer.count-1; k++) {
            groups[k] = answer.groups[k] // build array
        }
        return groups
    }
    return (
        <div className="items-box">
        <h2>Groups</h2>
            {groups.length > 0 &&
                <div className='groups-container'>
                    {groups.map(group => 
                    <Group key = {group.name} {...group} />)}
                </div>
            }
            {groups.length === 0 &&
                <p>There are no Groups to Display.</p>
            }
    </div>
    )
}
export default Groups