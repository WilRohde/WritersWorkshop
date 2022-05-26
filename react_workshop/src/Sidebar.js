import {HashRouter, Link} from 'react-router-dom'

export const Sidebar = () =>
    <HashRouter>
        <nav className="nav-column">
            <Link to="dashboard">[Dashboard]</Link>
            <Link to="account">[Account]</Link> 
            <Link to="#">[My Account]</Link>
            <Link to="#">[Upgrade to Pemium]</Link>
            <Link to="#">[LogOut]</Link>
            <Link to="groups">[Groups]</Link>
            <Link to="#">[Start a Group]</Link>
            <Link to="#">[Join a Group]</Link>
            <Link to="genres">[Genres]</Link>
            <Link to="#">[Create a Genre]</Link>
            <Link to="submissions">[Submissions]</Link>
            <Link to="#">[Submit Your Work]</Link>
            <Link to="#">[View Your Submissions]</Link>
            <Link to="#">[Author's Submissions]</Link>
        </nav>
    </HashRouter>

export default Sidebar
