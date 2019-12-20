
document.addEventListener('DOMContentLoaded', function(){
    if(localStorage.getItem('username') == null || localStorage.getItem('username') == ""){
        var txt;
        var username = prompt("Please enter a username:", "")
        while(username==null || username == ""){
            username = prompt("Please enter a valid username:", "")
            print(username)
        }
        localStorage.setItem('username', username)
        txt = "Hello " + username + ". Welcome to the chat app!"
    }else{
        txt = "Hello " + localStorage.getItem('username') + (". Welcome back to the chat app!")
    }
    document.getElementById("welcome").innerHTML = txt;

    //****  Setting up sockets  ****
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port)
    socket.on('connect', () => {
        document.querySelector('.newChannelForm').onsubmit = () => {
            var channelName = document.getElementById("newChannel").value;
            console.log("emtting channel", channelName)
            socket.emit('channelName', {'channelName': channelName})
        }
    });

    socket.on('newChannel', data => {
        const li = document.createElement('li');
        console.log(data)
        console.log(data.channelName)
        li.innerHTML= `${data.channelName}`;
        document.querySelector('#channelNames').append(li);
    })
});