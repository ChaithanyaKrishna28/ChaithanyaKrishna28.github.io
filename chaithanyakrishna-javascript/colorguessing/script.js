const body = document.querySelector('body')
const box = document.querySelectorAll('.box')
box.forEach(function(button){
    button.addEventListener('click',function(e){
        console.log(e.target.id)
        body.style.backgroundColor = e.target.id
    })
});