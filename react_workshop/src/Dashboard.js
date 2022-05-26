import {HashRouter, Link} from 'react-router-dom'
import Groups from './Groups'

export const Dashboard = (props) => 
    <div className="dashboard">
        {/* <Groups groups = {myGroups} /> */}
        <Groups groups = {props.myGroups} />
    </div>

export default Dashboard
