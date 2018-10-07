'use strict';

function post(){

    let payload = JSON.stringify({
        description: document.getElementById('message').value,
        itemName: document.getElementById('name').value
    });

    $.post('/' + payload, (result) => {
        alert('returned with:' + result);
    });
}