

const time = document.querySelector(".Time")
setInterval(function(){
    let date = new Date()
    time.innerHTML= date.toLocaleTimeString();
},1000)