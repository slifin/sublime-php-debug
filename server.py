import sublime
import socket

def start():
	create_socket()

def stop():
	sublime.message_dialog("hey")

def create_socket():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.bind(("localhost", 9000))
	server.listen(1)
	connection, address = server.accept()
	sublime.message_dialog(read_until_null(connection))
	connection.close()

def read_until_null(connection, buffer = '', read_size = 1024):
	while '\x00' not in buffer:
		buffer += (connection.recv(read_size)).decode('utf8')
	data, buffer = buffer.split('\x00', 1)
	return data


def read_data():
	return 2