import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';

class Form extends Component {
  render() {
    return (
      <div className="Form">
        <header className="Form-header">
            <img src={logo} className="Form-logo" alt="logo" />
            <p>
            Edit <code>src/Form.js</code> and save to reload.
            </p>
            Learn React
            <Link to="/Form">Form</Link>
        </header>
      </div>
    );
  }
}

export default Form;
