from PyQt6.QtCore import QUrl

class Browser:
    def __init__(self, web_view):
        self.web_view = web_view

    def load_url(self, url):
        self.web_view.setUrl(QUrl(url))

    def get_current_url(self):
        return self.web_view.url().toString()

    def run_javascript(self, script, callback):
        self.web_view.page().runJavaScript(script, callback)
