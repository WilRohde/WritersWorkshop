import React, {Component} from 'react'
import 'react-bootstrap';
import './App.css';
import './style.css';
import WHeader from './WHeader';
import Dashboard from './Dashboard';
import Groups from './Groups';
import {Link} from 'react-router-dom'
// import {
//   Account,
//   About,
//   Genres,
//   Submissions
// } from './Pages'

 class App extends Component{
  constructor(props) {
    super(props)
    this.state = {
      groups: [],
      genres: [],
      submissions: [],
      firstname: 'William',
      lastname: 'Hearst',
      loading: false
    }
  }
  render () {
  //   const hdrConfig = {
  //     firstname: this.state.firstname,
  //     lastname: this.state.lastname
  // }

    return(
    <div className="App">
    {/* // <Link to="/groups">Groups</Link> |{" "}
        // <Link to="/genres">Genres</Link>
        // <Link to="/about">About</Link>
        // <Link to="/account">Account</Link>
        // <Link to="/submissions">Submissions</Link> /*}

      <WHeader authorName = {hdrConfig} />
      {/* <div className="main"> */}
      {/*  // <Dashboard /> */}
      {/* </div> */}
    </div>
  )
  }
 }

export default App;
