import sublime
import sublime_plugin
from .thread_event import is_listening
from .server import start, stop

class StartListenCommand(sublime_plugin.WindowCommand):
  def run(self):
    start()
  def is_enabled(self):
    return not is_listening()

class StopListenCommand(sublime_plugin.WindowCommand):
  def run(self):
    stop()
  def is_enabled(self):
    return is_listening()