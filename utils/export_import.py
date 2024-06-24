import json
import networkx as nx

def export_map(graph, file_name):
    data = nx.node_link_data(graph)
    with open(file_name, 'w') as f:
        json.dump(data, f)

def import_map(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return nx.node_link_graph(data)
