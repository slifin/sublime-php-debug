import sublime
import socket
import threading
from .thread_event import start as event_start, stop as event_stop, is_listening

def start():
  event_start()
  threading.Thread(
    target=create_socket,
  ).start()

def stop():
  event_stop()

def create_socket():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server.bind(("localhost", 9000))
  server.listen(1)
  connection, address = server.accept()

  tuplelol = read_until_null(connection)
  message = read_until_null(connection, tuplelol[1])

  sublime.message_dialog(tuplelol[0])
  sublime.message_dialog(message[0])
  connection.close()

def read_until_null(connection, buffer = '', read_size = 1024):
  while '\x00' not in buffer and is_listening():
    buffer += (connection.recv(read_size)).decode('utf8')
  return buffer.split('\x00', 1)


