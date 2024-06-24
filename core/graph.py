import networkx as nx
from pyvis.network import Network

class Graph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def clear(self):
        self.graph.clear()

    def add_node(self, url, title):
        if url not in self.graph.nodes:
            self.graph.add_node(url, title=title)

    def add_edge(self, source, target, label):
        if not self.graph.has_edge(source, target):
            self.graph.add_edge(source, target, label=label)

    def add_note_to_node(self, url, note):
        if url in self.graph.nodes:
            self.graph.nodes[url]['note'] = note

    def add_endpoints_to_node(self, url, endpoints):
        if url in self.graph.nodes:
            if 'endpoints' not in self.graph.nodes[url]:
                self.graph.nodes[url]['endpoints'] = []
            for endpoint in endpoints:
                if endpoint not in self.graph.nodes[url]['endpoints']:
                    self.graph.nodes[url]['endpoints'].append(endpoint)

    def get_visualization(self):
        net = Network(notebook=True, directed=True)
        net.from_nx(self.graph)
        return net
