import sublime_plugin

class StartListenCommand(sublime_plugin.WindowCommand):
  def run(self):
    from .server import start
    start()

class StopListenCommand(sublime_plugin.WindowCommand):
  def run(self):
    from .server import stop
    stop()