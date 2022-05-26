import React from "react";
import {
    Link,
    useLocation,
    Outlet
} from "react-router-dom";

export const navDashboard = () =>
    <section className="dashboard">
        <h1>[Home Page]</h1>
    </section>

export const About = () =>
    <section className="about">
        <h1>[About]</h1>
    </section>

export const Groups = () =>
    <section className="groups">
        <h1>[Groups]</h1>
    </section>

export const Genres = () =>
    <section className="genres">
        <h1>[Genres]</h1>
    </section>

export const Submissions = () =>
    <section className="submissions">
        <h1>[Submissions]</h1>
    </section>

export const Contact = () =>
    <section className="Contact">
        <h1>[Contact Us]</h1>
    </section>
// export function Dashboard() {
//     return (
//     <div>
//         <h1>[Writer's Workshop]</h1>
//         <nav>
//             <Link to="about">About</Link>
//             <Link to="groups">Events</Link>
//             <Link to="genres">Contact Us</Link>
//             <Link to="submissions">Products</Link>
//         </nav>
//     </div>
//     );
//     }
