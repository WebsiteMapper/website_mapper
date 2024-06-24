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

    def get_visualization(self):
        net = Network(notebook=True, directed=True)
        net.from_nx(self.graph)
        return net
