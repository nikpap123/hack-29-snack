import React from 'react'
import Nav from 'react-bootstrap/Nav'
import Navbar from 'react-bootstrap/Navbar'
import NavDropdown from 'react-bootstrap/NavDropdown'

const Navigation = props => (
  <Navbar variant="dark" expand="lg" fixed="top">
    <Navbar.Brand href="#home">HACK-29-SNACK</Navbar.Brand>
    <img src={require('../images/catto.png')} />
    <img src={require('../images/doggo.png')} />
    <NavDropdown title="2nd Floor" id="nav-dropdown">
        <NavDropdown.Item>2nd Floor</NavDropdown.Item>
    </NavDropdown>
    <Navbar.Toggle aria-controls="basic-navbar-nav" />
  </Navbar>
)

export default Navigation
