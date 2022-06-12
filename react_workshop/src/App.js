import React, { Component } from 'react'
import 'react-bootstrap';
import './App.css';
import './style.css';
import Dashboard from './Dashboard'
import {BrowserRouter, Routes, Route, NavLink} from 'react-router-dom'
class App extends Component {
  constructor(props) {
    super(props);
    this.state = {user: 
      {
        firstname: "William",
        lastname: "Hearst",
        email: "WHearst@rosebud.com"
      },
      authorName: "William Hearst",
      groups: 
      [{
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
      }],
    genres: 
    [{
      name: "Science Fiction",
      short_description: "Stuff blowing up in space.",
      description: "if you yearn for stories from the great beyond, this is the group for you."
    },
    {
      name: "Teenage Vampire Fiction",
      short_description: "Lots of angsty vampire foolishness.",
      description: "Vampires have angst. They have nothing on teenagers. You'll find the best of both worlds here."
    },
    {
      name: "Pirates",
      short_description: "Write to make Jack Sparrow proud.",
      description: "Buried treasure, high seas adventure, lots of bad food and dysentery. If that's your thing, you've found a home."
    },
    {
      name: "Steampunk",
      short_description: "An aquired taste, not for you if your characters don't like wearing googles.",
      description: "Entire civilizations that just can't get a handle on electricity and are satisfied with boiling water running everything."
    }],
    submissions: [],
    reviews: [],
    loading: "False"
  }
}
  render () {
    return (
      <div className="App">
      </div>
      );  
  }
};
export default App