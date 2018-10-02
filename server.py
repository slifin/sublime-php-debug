import sublime
import socket
import threading

def listen_event(event = None):

  if (event is not None):
    listen_event.event = event

  return event or getattr(listen_event, "event", None)

def is_listening():
  event = listen_event()
  return event is not None and not event.is_set()


def start():
  evt = listen_event(threading.Event())

  threading.Thread(
    target=create_socket,
    args=(evt,)
  ).start()

def stop():
  listen_event().set()

def create_socket(evt):
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server.bind(("localhost", 9000))
  server.listen(1)
  connection, address = server.accept()
  sublime.message_dialog(read_until_null(connection, evt))
  connection.close()

def read_until_null(connection, evt, buffer = '', read_size = 1024):
  while not evt.is_set() and '\x00' not in buffer:
    buffer += (connection.recv(read_size)).decode('utf8')
  data, buffer = buffer.split('\x00', 1)
  return data
