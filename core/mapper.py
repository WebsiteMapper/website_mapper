from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QInputDialog, QMessageBox
from core.graph import Graph
from pyvis.network import Network
import tempfile
import os

class Mapper:
"""
Core class handling the website mapping functionality.
    
This class manages the process of crawling websites, building
the site map, and updating the visualization.
"""
    def __init__(self, browser):
        self.browser = browser
        self.graph = Graph()

    def start_mapping(self):
    """
    Begin the mapping process for the current URL.
        
    Validates the URL, initializes the graph, and starts
    the page loading process.
    """
        url = self.browser.url().toString()
        if not url.startswith(('http://', 'https://')):
            QMessageBox.warning(None, "Invalid URL", "Please enter a valid URL starting with http:// or https://")
            return
        
        try:
            self.browser.setUrl(QUrl(url))
            self.browser.loadFinished.connect(self.page_loaded)
            self.graph.clear()
            self.graph.add_node(url, "Start Page")
        except Exception as e:
            QMessageBox.critical(None, "Error", f"An error occurred while starting the mapping: {str(e)}")

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
        net = self.graph.get_visualization()
        
        # Create a temporary file to save the HTML
        with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as tmp_file:
            net.save_graph(tmp_file.name)
            
        # Load the temporary file in the browser view
        self.browser.setUrl(QUrl.fromLocalFile(tmp_file.name))
        
        # Schedule the temporary file for deletion after it's loaded
        self.browser.loadFinished.connect(lambda: os.unlink(tmp_file.name))

    def add_note(self, url):
        note, ok = QInputDialog.getText(None, "Add Note", f"Enter note for {url}")
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
