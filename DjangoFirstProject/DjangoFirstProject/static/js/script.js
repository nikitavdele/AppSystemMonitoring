document.addEventListener('DOMContentLoaded', function() {
    console.log("123");

    // Другой код здесь
});

let temp = document.getElementById('temp')
console.log(temp.innerHTML)
temp.innerHTML = "15%"


  let response = await fetch('/get_params');
  console.log(data)
  if (response.ok) {
    let data = await response.json();

    if (data.cpu_cores !== undefined) {
      document.getElementById('cpu_cores').innerText = `CPU Cores: ${data.cpu_cores}`;
    } else {
      console.error("Invalid data format", data);
    }
  } else {
    throw new Error(`HTTP error! Status: ${response.status}`);
  }


// fetch('/get_params')
// console.log(data)
//   .then(response=>response.json())
//   .then(data=> {
//     if(data.cpu_cores!==undefined){
//       document.getElementById('cpu_cores').innerText ='CPU Cores: ${data.cpu_cores}';

//     }
//     else {
//       console.error("Invalid data format", data);
//     }
//   })
