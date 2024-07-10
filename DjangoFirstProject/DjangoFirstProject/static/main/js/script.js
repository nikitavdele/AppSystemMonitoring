document.addEventListener('DOMContentLoaded', function() {
    console.log("123");

    // Другой код здесь
});

let temp = document.getElementById('temp')
temp.set-attribute('value', 10)


let loadaverage = fetch(url, [options])
let response = await fetch(url);

if (response.ok) { // если HTTP-статус в диапазоне 200-299
  // получаем тело ответа (см. про этот метод ниже)
  let json = await response.json();
} else {
  alert("Ошибка HTTP: " + response.status);
}

//let loadaverage = {
//  name: 'John',
//  surname: 'Smith'
//};
//
//let response = await fetch('/article/fetch/post/loadaverage', {
//  method: 'POST',
//  headers: {
//    'Content-Type': 'application/json;charset=utf-8'
//  },
//  body: JSON.stringify(loadaverage)
//});
//
//let result = await response.json();
//alert(result.message);