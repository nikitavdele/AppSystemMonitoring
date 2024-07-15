const request = new XMLHttpRequest();


//let temp = document.getElementById('temp')
//console.log(temp.innerHTML)
//temp.innerHTML = "16%"

fetch('/get_params', { method: 'GET' }).then(res => res.json()).then(function(data_names) {
            let load_1min=document.getElementById('load_1min')
                          //console.log(CpuCores.innerHTML)
                          load_1min.innerHTML=data_names.load_1min

            let load_5min=document.getElementById('load_5min')
                          //console.log(CpuCores.innerHTML)
                          load_5min.innerHTML=data_names.load_5min

            let load_15min=document.getElementById('load_15min')
                          //console.log(CpuCores.innerHTML)
                          load_15min.innerHTML=data_names.load_15min

            let cpu_MHz1=document.getElementById('cpu_MHz1')
                          //console.log(CpuCores.innerHTML)
                          cpu_MHz1.innerHTML=data_names.cpu_MHz1+' MHz'

            let cpu_MHz2=document.getElementById('cpu_MHz2')
                          //console.log(CpuCores.innerHTML)
                          cpu_MHz2.innerHTML=data_names.cpu_MHz2+' MHz'

            let cpu_MHz3=document.getElementById('cpu_MHz3')
                          //console.log(CpuCores.innerHTML)
                          cpu_MHz3.innerHTML=data_names.cpu_MHz3+' MHz'

            let cpu_MHz4=document.getElementById('cpu_MHz4')
                          //console.log(CpuCores.innerHTML)
                          cpu_MHz4.innerHTML=data_names.cpu_MHz4+' MHz'

            let cpu_MHz5=document.getElementById('cpu_MHz5')
                          //console.log(CpuCores.innerHTML)
                          cpu_MHz5.innerHTML=data_names.cpu_MHz5+' MHz'

            let cpu_MHz6=document.getElementById('cpu_MHz6')
                          //console.log(CpuCores.innerHTML)
                          cpu_MHz6.innerHTML=data_names.cpu_MHz6+' MHz'

            let cpu_MHz7=document.getElementById('cpu_MHz7')
                          //console.log(CpuCores.innerHTML)
                          cpu_MHz7.innerHTML=data_names.cpu_MHz7+' MHz'

            let cpu_MHz8=document.getElementById('cpu_MHz8')
                          //console.log(CpuCores.innerHTML)
                          cpu_MHz8.innerHTML=data_names.cpu_MHz8+' MHz'



             let CpuCores=document.getElementById('cpu_cores')
                          //console.log(CpuCores.innerHTML)
                          CpuCores.innerHTML=data_names.cpu_cores

             let MemTotal=document.getElementById('MemTotal')
                          //console.log(MemTotal.innerHTML)
                          MemTotal.innerHTML=data_names.MemTotal


             let MemFree=document.getElementById('MemFree')
                          //console.log(MemFree.innerHTML)
                          MemFree.innerHTML=data_names.MemFree

             let MemAvailable=document.getElementById('MemAvailable')
                          //console.log(MemAvailable.innerHTML)
                          MemAvailable.innerHTML=data_names.MemAvailable

             let SwapTotal=document.getElementById('SwapTotal')
                          //console.log(SwapTotal.innerHTML)
                          SwapTotal.innerHTML=data_names.SwapTotal

             let disk_size=document.getElementById('disk_size')
                          //console.log(SwapTotal.innerHTML)
                          disk_size.innerHTML=data_names.disk_size

             let disk_used=document.getElementById('disk_used')
                          //console.log(SwapTotal.innerHTML)
                          disk_used.innerHTML=data_names.disk_used

             let disk_free=document.getElementById('disk_free')
                          //console.log(SwapTotal.innerHTML)
                          disk_free.innerHTML=data_names.disk_free



        })

