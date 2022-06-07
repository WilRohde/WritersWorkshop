import Sidebar from './Sidebar'
import {Outlet} from 'react-router-dom'
import WHeader from './WHeader'
// import {
//     Account,
//     About,
//     Genres,
//     Groups,
//     Submissions
//     } from './Pages'

export const Dashboard = (props) => 
        <div className="dashboard">
            <WHeader authorName = {props} />
            <div className="main">
                <Sidebar />
                <Outlet />
            </div>
        </div>

export default Dashboard
