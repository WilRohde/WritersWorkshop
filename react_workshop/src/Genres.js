import React, {useState, useEffect} from 'react';
import 'react-bootstrap';
import Genre from './Genre';
import fetch from 'isomorphic-fetch';
import './style.css';
import { fetchGenres } from './APIFunctions';

const apiurl = 'http://localhost:5000/api/'
const origin = "http:/WritersWorkshop/testApi.html"

export const Genres = () => {
    const [genres,setGenres] = useState([])
    const [loading,setLoading] = useState(true)
    useEffect(() => {
        fetchGenres(setGenres, setLoading);
    }, [])
    return (
        <div className="items-box">
        <h2>Genres</h2>
            {loading===true &&
                <p>Loading Genres...</p>
            }
            {genres.length > 0 &&
                // <div className='groups-container'>
                <table>
                    <tbody>
                        <tr>
                            {/* <td className='groups-container'> */}
                            {genres.map(genre => 
                            <td className='itemCell'><Genre key = {genre.name} {...genre} /></td>)}
                            {/* </td> */}
                        </tr>
                    </tbody>
                </table>
                // </div>
            }
            {loading===false &&
                (genres.length === 0) &&
                    <p>There are no Genres to Display.</p>
                
            }
    </div>
    )
}
export default Genres