import sublime
import sublime_plugin
class StartListenCommand(sublime_plugin.WindowCommand):
  def run(self):
    from .server import start
    start()
  def is_enabled(self):
    from .server import listen_event
    event = listen_event()
    return event is None or not event.is_set()


class StopListenCommand(sublime_plugin.WindowCommand):
  def run(self):
    from .server import stop
    stop()
  def is_enabled(self):
    from .server import listen_event
    event = listen_event()
    return event is not None and event.is_set()