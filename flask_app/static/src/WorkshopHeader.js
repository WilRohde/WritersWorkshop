import React, {Component} from 'react';

class WorkshopHeader extends Component {
    render() {
        return (
            <div>
                <h1 class="h1-workshop">Welcome Back Your-Name-Here!</h1>
                 <div class="workshop-header-btns">
                    <form action="/genre/new"><button type="submit" class="btn-warning btn-workshop">Create a New Genre</button></form>
                    <form action="/group/new"><button type="submit" class="btn-primary btn-workshop">Create a New Group</button></form>
                    <form action="/logout"><button type="submit" class="btn-primary btn-workshop">Logout</button></form>
                </div> 
            </div>
        )
    }
}
export default WorkshopHeader