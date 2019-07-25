import React, { Component } from 'react';
import Header from './components/Header';
import Navigation from './components/Navigation';
import SimpleTable from './components/SimpleTable';
import Modal from 'react-bootstrap/Modal';  
import Button from 'react-bootstrap/Button';
import NutritionalTable from './components/NutritionalTable';
import StarRatingComponent from 'react-star-rating-component';
import './App.css';
import axios from 'axios';

class App extends Component {
  constructor (props) {
    super(props)

    this.state = {
      show: false,
      current_snack: "",
      floor: 2,
      rating: 0
    }
  }

  getNutrition() {
  }

  getAvailability() {
    console.log('Availability');
    axios.get('http://localhost:5000/availability')
      .then(response => console.log(response));
  }
  
  handleClose () {
    this.setState({show: false})
  } 

  handleSaveAndClose() {
    this.submitRating(this.state.rating);
    this.handleClose();
  }

  handleClick(name) {
    this.getAvailability();
    this.setState({show: true})
    this.setState({current_snack: name})
  }

  submitRating(rating) { 
    console.log(rating)
  }

  onStarClick(nextValue, prevValue, name){
    this.setState({rating: nextValue})
  }

  render() {
    return (
      <div className="app">

        <Navigation/>

        <SimpleTable clickAction={(name) => this.handleClick(name)}/>
        
        <img width="100%" height="100%" src={require('./images/snack.jpg')} />

        <Modal onHide={() => this.handleClose()} show={this.state.show}>
          <Modal.Header>
            <Modal.Title>{this.state.current_snack}</Modal.Title>
          </Modal.Header>

          <Modal.Body>
            <p>Leave a review!</p>
            <StarRatingComponent
              name={"leaveReview"}
              value={this.state.rating}
              onStarClick={this.onStarClick.bind(this)}
              editing={true}
            />
            <p>Nutrition Details</p>
            <NutritionalTable/>
          </Modal.Body>

          <Modal.Footer>
            <Button variant="primary" onClick={() => this.handleSaveAndClose()}>Save and Close</Button>
            <Button variant="secondary" onClick={() => this.handleClose()}>Close</Button>
          </Modal.Footer>
        </Modal>

      </div>
    )
  }
}

export default App;
