"""
Dijkstra's algorithm implementation returning (distance, path)
If unreachable, returns (float('inf'), [])
"""
# shortest_path.py
import networkx as nx
from graph import G  # Import the graph from graph.py

def get_shortest_path(city1, city2):
    """
    Returns the shortest path and total distance between two cities.
    Raises an exception if no path exists.
    """
    if city1 not in G.nodes or city2 not in G.nodes:
        raise ValueError("One or both cities do not exist in the graph.")
    
    try:
        path = nx.dijkstra_path(G, city1, city2, weight='weight')
        distance = nx.dijkstra_path_length(G, city1, city2, weight='weight')

        return path, distance
    except nx.NetworkXNoPath:
        return None, None
