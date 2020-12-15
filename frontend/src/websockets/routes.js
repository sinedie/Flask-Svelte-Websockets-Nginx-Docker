import { socket } from './socket'


socket.on('connected', (msg) => {
    console.log(msg)
})


socket.on('healtcheck', (msg) => {
    console.log(msg)
})


socket.on('user_joined', (msg) => {
    console.log(msg)
})


socket.on('user_left', (msg) => {
    console.log(msg)
})


socket.on('task_finished', (data) => {
    console.log('Long task as finished with result: ')
    console.log(data);
});


function WS_healtcheck() {
    socket.emit('ping')
}


setInterval(WS_healtcheck, 30000)