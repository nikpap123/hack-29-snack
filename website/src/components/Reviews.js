import React, { Component } from 'react';
import { Card, ListGroup } from 'react-bootstrap'
import $ from 'jquery';

export default class Reviews extends Component {
  constructor(props) {
    super(props)

    this.state = {
      reviews: []
    }
  }

  getReviews() {
    $.ajax({
      method: "GET",
      url: "/review/" + this.props.currentSnack
    }).done(response => {
      this.setState({reviews: response.reviews})
    })
  }
  
  componentDidMount() {
    this.getReviews();
  }

  render() {
    return (
      <Card style={{ width: '18rem' }}>
        <ListGroup variant="flush">
          {this.state.reviews.map(review => (
            <ListGroup.Item key={review}>{review}</ListGroup.Item>
          ))}
        </ListGroup>
      </Card>
    )
  }
}