document.addEventListener('DOMContentLoaded', function() {
    console.log("123");

    // Другой код здесь
});

let temp = document.getElementById('temp')
console.log(temp.innerHTML)
temp.innerHTML = "15%"

let response = await fetch('/get_params');

// получить один заголовок
alert(response.headers.get('cpu MHz'));
    
console.log(temp.innerHTML(response.headers.get('cpu MHz')))


let response = await fetch('/get_params', {
  method: 'POST',
  headers: {
    'cpu cores': 'application/json;charset=utf-8'
  },
  body: JSON.stringify(user)
});