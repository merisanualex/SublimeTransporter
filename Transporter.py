import sublime, sublime_plugin

class move_caret(sublime_plugin.WindowCommand):
  def run(self, scope=""):
        self.window.show_input_panel("Move caret:", "", self.on_done, None, None)
  
  def on_done(self, text):
    if len(text) > 0:
        line = int(text)
        if self.window.active_view():
            self.window.active_view().run_command("mv_crt", {"n": line} )

class mv_crt(sublime_plugin.TextCommand):
    def run(self, edit, n):
        (row,col) = self.view.rowcol(self.view.sel()[0].begin())
        target = self.view.text_point(row+n, col)
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(target))
        self.view.show(target)
