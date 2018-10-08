import threading

def thread_event(event = None):

  if (event is not None):
    thread_event.event = event

  return event or getattr(thread_event, "event", None)

def is_listening(event = None):
  event = event or thread_event()
  listening = event is not None and not event.is_set()
  return listening

def start():
  thread_event(threading.Event())

def stop():
  thread_event().set()