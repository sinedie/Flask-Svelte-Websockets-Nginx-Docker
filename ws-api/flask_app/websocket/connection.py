from flask_socketio import join_room, leave_room, emit

from flask_app.websocket.socket import socketio


@socketio.on('ping')
def test_connect():
    emit('healtcheck', {'status': 'OK'})


@socketio.on('connect')
def test_connect():
    emit('connected', {'msg': 'Connected'})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    emit('user_joined', username + ' has entered the room.', room=room)


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    emit('user_left', username + ' has left the room.', room=room)
