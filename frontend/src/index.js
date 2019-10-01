import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

function Welcome(props) {
    return <h1> <p><a> Price Predict {props.name} </a></p> </h1>;
  }
  
  const element = <Welcome name="PricePredict.com" />;
  ReactDOM.render(
    element,
    document.getElementById('root')
  );
