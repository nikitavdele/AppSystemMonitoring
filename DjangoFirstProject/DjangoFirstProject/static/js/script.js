document.addEventListener('DOMContentLoaded', function() {
    console.log("123");

    // Другой код здесь
});

//let temp = document.getElementById('temp')
//console.log(temp.innerHTML)
//temp.innerHTML = "16%"

fetch('/get_params', { method: 'GET' }).then(res => res.json()).then(function(data_names) {
             let CPUCORES=document.getElementById('cpu_cores')
                          console.log(CPUCORES.innerHTML)
                          CPUCORES.innerHTML=data_names.cpu_cores

             let MemTotal=document.getElementById('MemTotal')
                          console.log(MemTotal.innerHTML)
                          MemTotal.innerHTML=data_names.MemTotal


             let MemFree=document.getElementById('MemFree')
                          console.log(MemFree.innerHTML)
                          MemFree.innerHTML=data_names.MemFree

             let MemAvailable=document.getElementById('MemAvailable')
                          console.log(MemAvailable.innerHTML)
                          MemAvailable.innerHTML=data_names.MemAvailable

             let SwapTotal=document.getElementById('SwapTotal')
                          console.log(SwapTotal.innerHTML)
                          SwapTotal.innerHTML=data_names.SwapTotal



        })

//try {
//  let response = fetch('/get_params');
//
//  if (response.ok) {
//    let data = response.json();
//    console.log(data)
//
//    if (data.cpu_cores !== undefined) {
//      document.getElementById('cpu_cores').innerText = `CPU Cores: ${data.cpu_cores}`;
//    } else {
//      console.error("Invalid data format", data);
//    }
//  } else {
//    throw new Error(`HTTP error! Status: ${response.status}`);
//  }
//} catch (error) {
//  console.error("An error occurred:", error);
//}


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
