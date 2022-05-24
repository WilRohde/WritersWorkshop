import logo from './logo.svg';
import {Component} from 'react'
import 'react-bootstrap';
import './App.css';
import './style.css';
import Group from './Group';
import Groups from './Groups'
import {Button} from 'react-bootstrap';
import WHeader from './WHeader';

class App extends Component{
  constructor(props) {
    super(props)
    this.state = {
      groups: [],
      genres: [],
      submissions: [],
      firstname: 'William',
      lastname: 'Hearst'
    }
  }
  render () {
    const hdrConfig = {
      firstname: this.state.firstname,
      lastname: this.state.lastname
  }

    const myGroups = [{
      name: 'Yo Ho Hokum',
      GenreName: 'Pirates',
      founding_date: '05/16/2020',
      description: 'Lots of goofy pirate weirdness',
      count: 2
    },
    {
      name: "Sci Fi Rangers",
      GenreName: 'Science Fiction',
      founding_date: '08/13/2010',
      description: 'sci fi foolishness',
      count: 11
    }]

    this.state.groups = myGroups
    
    return(
    <div className="App">
      <WHeader author = {hdrConfig} />
      <Groups groups = {myGroups} />
    </div>
  )
  }
}

export default App;
