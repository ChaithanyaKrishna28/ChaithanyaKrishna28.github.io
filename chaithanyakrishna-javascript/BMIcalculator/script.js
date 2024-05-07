const form = document.querySelector('form')
form.addEventListener('submit',function(e){
    e.preventDefault()
    const heightInput = document.querySelector("#height")
    const weightInput = document.querySelector("#weight")
    const height1 = parseInt(heightInput.value);
    const height = height1/100
    const weight = parseInt(weightInput.value);
    const results = document.querySelector(".results")
    if (isNaN(height) || isNaN(weight)) {
        alert("Please enter valid numbers")
        return;
    }
    else{
        const bmi = (weight/(height*height)).toFixed(2);
        results.innerHTML=`<span>Your BMI is: ${bmi}<span>`
        heightInput.value=''
        weightInput.value=''
    }  

})