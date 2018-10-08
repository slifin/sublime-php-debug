import threading

def thread_event(event = None):

  if (event is not None):
    thread_event.event = event

  return event or getattr(thread_event, "event", None)

def is_listening(event = None):
  event = event or thread_event()
  return event is not None and not event.is_set()


def start():
  return thread_event(threading.Event())

def stop():
  event = thread_event()
  event.set()
  return event