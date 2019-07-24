import React, { Component } from 'react';
import Header from './components/Header';
import Navigation from './components/Navigation';
import SimpleTable from './components/SimpleTable';
import Modal from 'react-bootstrap/Modal';  
import Button from 'react-bootstrap/Button';
import NutritionalTable from './components/NutritionalTable';
import StarRatingComponent from 'react-star-rating-component';
import './App.css';

class App extends Component {
  constructor (props) {
    super(props)

    this.state = {
      show: false,
      current_snack: ""
    }
  }

  
  handleClose () {
    this.setState({show: false})
  } 

  handleSaveAndClose() {
  }

  handleClick(name) {
    this.setState({show: true})
    this.setState({current_snack: name})
  }

  submitRating(rating) {
  }

  componentDidMount () {
  }

  render() {
    return (
      <div className="app">

        <Navigation/>

        <SimpleTable clickAction={(name) => this.handleClick(name)}/>
        
        <img width="100%" height="100%" src={require('./images/snack.jpg')} />

        <Modal show={this.state.show}>
          <Modal.Header>
            <Modal.Title>{this.state.current_snack}</Modal.Title>
          </Modal.Header>

          <Modal.Body>
            <p>Leave a review!</p>
            <StarRatingComponent
              name={"leaveReview"}
              editing={true}
            />
            <p>Nutrition Details</p>
            <NutritionalTable/>
          </Modal.Body>

          <Modal.Footer>
            <Button variant="primary" onClick={() => this.handleClose()}>Save and Close</Button>
            <Button variant="secondary" onClick={() => this.handleClose()}>Close</Button>
          </Modal.Footer>
        </Modal>

      </div>
    )
  }
}

export default App;
