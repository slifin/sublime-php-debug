import sublime
import socket
import threading
from .thread_event import start as thread_start, stop as thread_stop

def start():
  threading.Thread(
    target=create_socket,
    args=(thread_start(),)
  ).start()

def stop():
  thread_stop()

def create_socket(event):
  sublime.message_dialog(str(event))
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server.bind(("localhost", 9000))
  server.listen(1)
  connection, address = server.accept()

  tuplelol = read_until_null(connection, event)
  message = read_until_null(connection, event, tuplelol[1])

  sublime.message_dialog(tuplelol[0])
  sublime.message_dialog(message[0])
  connection.close()

def read_until_null(connection, event, buffer = '', read_size = 1024):
  while '\x00' not in buffer and not event.is_set():
    buffer += (connection.recv(read_size)).decode('utf8')
  return buffer.split('\x00', 1)


