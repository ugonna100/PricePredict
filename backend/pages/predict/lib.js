'use strict';

function post(){
    

    let payload = JSON.stringify({
        description: document.getElementById('data').value,
        itemName: document.getElementById('name').value
    });
    
    $.post('/predict' + payload, (result) => {
        alert('returned with:' + result);
    });
}