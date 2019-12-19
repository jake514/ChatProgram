document.addEventListener('DOMContentLoaded', function(){
    if(localStorage.getItem('username') == null || localStorage.getItem('username') == ""){
        var txt;
        var username = prompt("Please enter a username:", "")
        if(username == null || username == "") {
            username = prompt("Please enter a valid username:", "")
        }
        localStorage.setItem('username', username)
        txt = "Hello " + username + ". Welcome to my chat app!"
    }else{
        txt = "Hello " + localStorage.getItem('username') + (". Welcome back to the chat app!")
    }
    document.getElementById("welcome").innerHTML = txt;
});