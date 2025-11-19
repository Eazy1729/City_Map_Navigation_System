"""
Connectivity check using BFS/DFS
"""
# connectivity.py
import networkx as nx
from graph import G  # Import the graph from graph.py

def is_connected(city1, city2):
    """
    Check if two cities are connected in the graph.
    Returns True if a path exists, False otherwise.
    """
    if city1 not in G.nodes or city2 not in G.nodes:
        raise ValueError("One or both cities do not exist in the graph.")
    return nx.has_path(G, city1, city2)
