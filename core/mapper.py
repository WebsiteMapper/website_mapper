from core.browser import Browser
from core.graph import Graph

class Mapper:
    def __init__(self, web_view):
        self.browser = Browser(web_view)
        self.graph = Graph()

    def start_mapping(self):
        url = self.browser.get_current_url()
        if url:
            self.browser.load_url(url)
            self.browser.web_view.loadFinished.connect(self.page_loaded)
            self.graph.clear()
            self.graph.add_node(url, "Start Page")

    def page_loaded(self):
        current_url = self.browser.get_current_url()
        self.browser.run_javascript("""
            var links = Array.from(document.links).map(link => ({href: link.href, text: link.textContent}));
            var title = document.title;
            ({links: links, title: title});
        """, self.process_page_data)

    def process_page_data(self, data):
        current_url = self.browser.get_current_url()
        self.graph.add_node(current_url, data['title'])
        for link in data['links']:
            self.graph.add_edge(current_url, link['href'], link['text'])
        self.update_map()

    def update_map(self):
        # TODO: Implement map update logic
        pass
