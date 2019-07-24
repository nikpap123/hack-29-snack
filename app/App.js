import React, { Component } from 'react';
import Header from './components/Header';
import Navigation from './components/Navigation';
import './App.css';

class App extends Component {
  constructor (props) {
    super(props)

    this.state = {}
  }

  componentDidMount () {
  }

  render() {
    return (
      <div className="app">
        <Navigation/>
        <img width="100%" height="100%" src={require('./images/snack.jpg')} />
      </div>
    )
  }
}

export default App;
