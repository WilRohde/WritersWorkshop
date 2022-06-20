import React from 'react';
import 'react-bootstrap';

export const Genre = (props) => {
    return (
        <div>
            <h5>{props.name}</h5>
            {props.GenreName}
            <p>
                {props.short_description}
            </p>
            <p>
                {props.description}
            </p>
        </div>
    );
}
export default Genre