import React, { Component } from 'react';
import Header from './components/Header';
import Navigation from './components/Navigation';
import SimpleTable from './components/SimpleTable';
import Modal from 'react-bootstrap/Modal';  
import Button from 'react-bootstrap/Button';
import NutritionalTable from './components/NutritionalTable';
import StarRatingComponent from 'react-star-rating-component';
import './App.css';
import $ from 'jquery';

class App extends Component {
  constructor (props) {
    super(props)

    this.state = {
      show: false,
      current_snack: "",
      floor: 2,
      rating: 0,
      availability: {},
      nutrition: {},
      ratings: {},
      photo_view: true
    }
  }

  componentWillMount() {
    this.getAvailability();
    this.getNutrition();
  }

  getPhoto() {
  }

  getRatings() {
    $.ajax({
      method: "GET",
      url: "/rating"
    }).done((response) => {
      console.log(response);
      this.setState({ratings: response})
    });
  }

  getNutrition() {
    $.ajax({
      method: "GET",
      url: "/nutrition"
    }).done((response) => {
      this.setState({nutrition: response})
    });
  }

   getAvailability() {
    $.ajax({
      method: "GET",
      url: "/availability"
    }).done((response) => {
      this.setState({availability: response})
    });
  }
  
  handleClose () {
    this.setState({show: false})
  } 

  handleSaveAndClose() {
    this.submitRating(this.state.rating);
    this.handleClose();
  }

  handleClick(name) {
    this.setState({show: true})
    this.setState({current_snack: name})
  }

  submitRating(rating) { 
    $.ajax({
      method: "POST",
      url: "/rating/" + this.state.current_snack,
      data: {
        rating: this.state.rating
      }
    }).done((response) => {
      this.setState({nutrition: response})
    });

  }

  onStarClick(nextValue, prevValue, name){
    this.setState({rating: nextValue})
  }

  changeView(){
    this.setState({photo_view: !this.state.photo_view});
  }

  render() {
    return (
      <div className="app">

        <Navigation/>
        
        <h2>
              <img style={{position: 'relative', top: '-10px'}}src={require('./images/corgif.gif')} />
              Welcome to the Snackathon!
        </h2>

        {this.state.photo_view && 
          <div>
            <a className="link" onClick={() => this.changeView()}> see live photo </a>
            <SimpleTable availability={this.state.availability} nutrition={this.state.nutrition} clickAction={(name) => this.handleClick(name)}/>
          </div>
        }
        {!this.state.photo_view &&
          <div>
            <a className="link" onClick={() => this.changeView()}> see snack details </a>
            <img width="100%" height="100%" style={{paddingTop: '20px'}} src={require('./images/snack.jpg')} />
          </div>
        }

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
            <NutritionalTable nutrition={this.state.nutrition} snack={this.state.current_snack}/>
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
