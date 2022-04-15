#!.python_venv/bin/python3

from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO
from flask_socketio import SocketIO, join_room, leave_room
from flask_cors import CORS
import logging
import os

template_dir = os.path.abspath('./html/')
app = Flask(__name__,template_folder=template_dir, static_folder="./bootstrap/")
CORS(app)
app.logger.setLevel(logging.INFO)
socketio = SocketIO(app,cors_allowed_origins="*")

#https://www.youtube.com/watch?v=uJC8A_7VZOA&ab_channel=IndianPythonista
#https://github.com/nikhilkumarsingh/flask-chat-app/tree/cac07d1d01a1afe60f35fbe1f08340ee2b16b832
class chatter:
	def __init__(self,name = ""):
		self.name = name

class message:
	def __init__(self, data = "", roomID = "", msgID = ""):
		data = ""
		self.roomID = roomID
		self.msgID = msgID



class room:
	def __init__(self,roomID = ""):
		self.roomID = roomID

	#@app.route("/")
	#def main_page():
	#	return render_template("index.html")

	@app.route("/chat")
	def chat_page():
		return render_template("index.html")
	#	return render_template("chat.html")

	@socketio.on('send_message')
	def handle_send_message_event(data):
		data['username'] = 'a user'
		data['room'] = '1'
		app.logger.info("{} has sent message to the room {}: {}".format(data['username'],
	  		                                                                data['room'],
	  		                                                                data['message']))
		
		socketio.emit('receive_message', data, room=data['room'])
	
	
	@socketio.on('join_room')
	def handle_join_room_event(data):
	    app.logger.info("{} has joined the room {}".format(data['username'], data['room']))
	    join_room(data['room'])
	    socketio.emit('join_room_announcement', data, room=data['room'])
	
	
	@socketio.on('leave_room')
	def handle_leave_room_event(data):
	    app.logger.info("{} has left the room {}".format(data['username'], data['room']))
	    leave_room(data['room'])
	    socketio.emit('leave_room_announcement', data, room=data['room'])



if __name__ == "__main__":
	socketio.run(app,debug=True)