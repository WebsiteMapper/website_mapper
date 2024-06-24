from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QInputDialog
from core.graph import Graph

class Mapper:
    def __init__(self, browser):
        self.browser = browser
        self.graph = Graph()

    def start_mapping(self):
        url = self.browser.url().toString()
        if url:
            self.browser.setUrl(QUrl(url))
            self.browser.loadFinished.connect(self.page_loaded)
            self.graph.clear()
            self.graph.add_node(url, "Start Page")

    def page_loaded(self):
        current_url = self.browser.url().toString()
        self.browser.page().runJavaScript("""
            var links = Array.from(document.links).map(link => ({href: link.href, text: link.textContent}));
            var title = document.title;
            ({links: links, title: title});
        """, self.process_page_data)

    def process_page_data(self, data):
        current_url = self.browser.url().toString()
        self.graph.add_node(current_url, data['title'])
        for link in data['links']:
            self.graph.add_edge(current_url, link['href'], link['text'])
        self.update_map()

    def update_map(self):
        # This method should update the visual representation of the map
        # The actual implementation will depend on how you want to display the map
        pass

    def add_note(self, url):
        note, ok = QInputDialog.getText(self, "Add Note", "Enter note for " + url)
        if ok and note:
            self.graph.add_note_to_node(url, note)
            self.update_map()

    def capture_endpoint(self):
        url = self.browser.url().toString()
        self.browser.page().runJavaScript("""
            var endpoints = performance.getEntriesByType('resource').map(e => ({name: e.name, method: e.initiatorType}));
            endpoints;
        """, self.process_endpoints)

    def process_endpoints(self, endpoints):
        current_url = self.browser.url().toString()
        self.graph.add_endpoints_to_node(current_url, endpoints)
        self.update_map()
