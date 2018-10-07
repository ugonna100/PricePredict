'use strict';

function post(){

    let payload = JSON.stringify({
        description: document.getElementById('data').innerHTML,
        itemName: document.getElementById('name').innerHTML
    });

    $.post('/' + payload, (result) => {
        alert('returned with:' + result);
    });
}