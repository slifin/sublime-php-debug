import sublime
import socket

def start():
	sublime.message_dialog("hey 131")

def stop():
	sublime.message_dialog("stopping")

def create_socket():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



