


function serverRequest(link){
    const xhr = new XMLHttpRequest()
    xhr.open("GET", link, true)
    xhr.onreadystatechange=function(){
        console.log('inside server')
        if (xhr.readyState === 4 && xhr.status == '200'){
            const data = JSON.parse(this.responseText);

            displaydata(data);
        }
    }
    xhr.send()
}
// url = https://api.github.com/users/ChaithanyaKrishna28
function displaydata(data){
    const name = data.name;
    const followers = data.followers;
    const following = data.following;
    const repos = data.public_repos;
    const created_date = data.created_at;
    const profile_pic_url = data.avatar_url

    document.getElementById('name').textContent = name;
    document.getElementById('followers').textContent =  followers;
    document.getElementById('following').textContent = following;
    document.getElementById('repos').textContent = repos;
    document.getElementById('date').textContent =  created_date;
    document.getElementById('profilePic').src = profile_pic_url;

    // const img = document.createElement('img')
    // img.src = profile_pic_url;
    // img.alt = "Profile Picture"
    // img
    // document.body.appendChild(img)
}

document.querySelector('form').addEventListener("submit",function(e){
    e.preventDefault();
})

document.querySelector('button').addEventListener("click",function(){
    const inputtext = document.querySelector("#url")
    const link = inputtext.value
    if(link){
        console.log("out side serve")
        serverRequest(link)
        inputtext.value=""
    }
    else{
        alert("Please enter a Github api url")
    }
})