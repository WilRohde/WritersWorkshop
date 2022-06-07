import {Link, NavLink} from 'react-router-dom'
import GroupForm from './GroupForm'

function linkStyle(isActive){
    return {
        display: "block",
        margin: "1rem 0",
        color: isActive ? "red" : "blue",
    };
}
export const Sidebar = () =>
    <nav className="nav-column">
        <Link to="home">[Dashboard]</Link>
        <Link to="account">[Account]</Link> 
        <NavLink
            style={({ isActive }) => {
            return {
                display: "block",
                margin: "1rem 0",
                color: isActive ? "red" : "blue",
            };
            }}
            to="account/view"
            key="accountView"
        >
            {'[My Account]'}
        </NavLink>
        {/* <Link to="account/view">[My Account]</Link> */}
        <NavLink
            style={({ isActive }) => {
            return {
                display: "block",
                margin: "1rem 0",
                color: isActive ? "red" : "blue",
            };
            }}
            to="account/upgrade"
            key="accountUpgrade"
        >
            {'[Upgrade to Premium]'}
        </NavLink>
        {/* <Link to="account/upgrade">[Upgrade to Pemium]</Link> */}
        <NavLink
            style={({ isActive }) => {
            return {
                display: "block",
                margin: "1rem 0",
                color: isActive ? "red" : "blue",
            };
            }}
            to="logout"
            key="logout"
        >
            {'[LogOut]'}
        </NavLink>
        {/* <Link to="logout">[LogOut]</Link> */}
        <NavLink
            style={({ isActive }) => {
            return {
                display: "block",
                margin: "1rem 0",
                color: isActive ? "red" : "blue",
            };
            }}
            to="groups"
            key="groups"
        >
            {'[Groups]'}
        </NavLink>
        {/* <Link to="groups">[Groups]</Link> */}
        <NavLink
            style={({ isActive }) => {
            return {
                display: "block",
                margin: "1rem 0",
                color: isActive ? "red" : "blue",
            };
            }}
            to="groups/create"
            key="groupsCreate"
        >
            {'[Create a Group]'}
        </NavLink>
        {/* <Link to="groups/create">[Start a Group]</Link> */}
        <NavLink
            style={({ isActive }) => {
            return {
                display: "block",
                margin: "1rem 0",
                color: isActive ? "red" : "blue",
            };
            }}
            to="groups/browse"
            key="groupsBrowse"
        >
            {'[Browse Groups]'}
        </NavLink>
        {/* <Link to="groups/browse">[Browse Groups]</Link> */}
        <NavLink
            style={({ isActive }) => {
            return {
                display: "block",
                margin: "1rem 0",
                color: isActive ? "red" : "blue",
            };
            }}
            to="genres"
            key="genres"
        >
            {'[Genres]'}
        </NavLink>
        {/* <Link to="genres">[Genres]</Link> */}
        <NavLink
            style={({ isActive }) => {
            return {
                display: "block",
                margin: "1rem 0",
                color: isActive ? "red" : "blue",
            };
            }}
            to="genres/create"
            key="genresCreate"
        >
            {'[Create a Genre]'}
        </NavLink>
        {/* <Link to="genres/create">[Create a Genre]</Link> */}
        <NavLink
            style={({ isActive }) => {
            return {
                display: "block",
                margin: "1rem 0",
                color: isActive ? "red" : "blue",
            };
            }}
            to="submissions"
            key="submissions"
        >
            {'[Submissions]'}
        </NavLink>
        {/* <Link to="submissions">[Submissions]</Link> */}
        <NavLink
            style={({ isActive }) => {
            return {
                display: "block",
                margin: "1rem 0",
                color: isActive ? "red" : "blue",
            };
            }}
            to="submissions/create"
            key="submissionsCreate"
        >
            {'[Submit Your Work]'}
        </NavLink>
        {/* <Link to="submissions/create">[Submit Your Work]</Link> */}
        <NavLink
            style={({ isActive }) => {
            return {
                display: "block",
                margin: "1rem 0",
                color: isActive ? "red" : "blue",
            };
            }}
            to="submissions/view"
            key="submissionsView"
        >
            {'[View Your Submissions]'}
        </NavLink>
        <Link to="submissions/view">[View Your Submissions]</Link>
    </nav>

export default Sidebar
