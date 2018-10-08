import sublime
import sublime_plugin

class StartListenCommand(sublime_plugin.WindowCommand):
  def run(self):
    from .server import start
    start()
  def is_enabled(self):
    from .thread_event import is_listening
    return not is_listening()

class StopListenCommand(sublime_plugin.WindowCommand):
  def run(self):
    from .server import stop
    stop()
  def is_enabled(self):
    from .thread_event import is_listening
    return is_listening()