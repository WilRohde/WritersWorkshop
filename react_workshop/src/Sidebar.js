import {Link, NavLink} from 'react-router-dom'

function linkStyle(isActive){
    return {
        display: "block",
        margin: "1rem 0",
        color: isActive ? "red" : "blue",
    };
}
export const Sidebar = () =>
    <nav className="nav-column">
        <NavLink to="/">[Dashboard]</NavLink>
        <NavLink to="account">[Account]</NavLink> 
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
    </nav>

export default Sidebar
