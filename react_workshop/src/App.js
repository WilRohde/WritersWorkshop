import {Component} from 'react'
import 'react-bootstrap';
import './App.css';
import './style.css';
import WHeader from './WHeader';
import {router, Route, HashRouter, Link} from 'react-router-dom'
import Sidebar from './Sidebar';
import Dashboard from './Dashboard';

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
    const hdrConfig = {
      firstname: this.state.firstname,
      lastname: this.state.lastname
  }

    return(
    <div className="App">
      <WHeader authorName = {hdrConfig} />
      <div className="main-container">
        <Sidebar />
        <Dashboard />
      </div>
    </div>
  )
  }
}

export default App;
