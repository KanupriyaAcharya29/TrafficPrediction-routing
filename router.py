import networkx as nx
import random

def build_graph():
    G = nx.Graph()
    for i in range(5):
        G.add_node(i)
    G.add_edges_from([(0,1),(1,2),(2,3),(3,4),(0,4)])
    return G

def get_best_route(G, source, target):
    for u,v in G.edges():
        G[u][v]['weight'] = random.uniform(1, 10)  # simulated congestion
    path = nx.shortest_path(G, source, target, weight='weight')
    return path