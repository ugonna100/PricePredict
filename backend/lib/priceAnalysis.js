'use strict'

const request = require('request');

function getData(){
    return new Promise((resolve, reject) => {
        let options = {
            method: 'POST', 
            url: 'http://0.0.0.0:5000'
        }
        request(options, (err, response, body) => {
            if (err) throw err;
            return resolve(JSON.parse(body));
        })
    });
}

module.exports = async function (data){
    return getData();
}