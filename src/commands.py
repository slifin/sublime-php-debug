class PhpDebugCommand(sublime_plugin.WindowCommand):
  def run(self):
    sublime.message_dialog("hey")
  def is_enabled(self):
    return True
  def is_visible(self):
    return True
