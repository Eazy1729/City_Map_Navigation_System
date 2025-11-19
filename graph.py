"""
Graph implementation using adjacency list.
Undirected, weighted graph representing cities and roads.
"""

# graph.py
import networkx as nx

# Predefined cities with coordinates
cities = {
    "Karachi": (24.8607, 67.0011),
    "Lahore": (31.5204, 74.3587),
    "Islamabad": (33.6844, 73.0479),
    "Multan": (30.1575, 71.5249),
    "Peshawar": (34.0151, 71.5249),
    "Quetta": (30.1798, 66.9750)
}

# Initialize Graph
G = nx.Graph()

# Add all predefined cities as nodes
for city in cities:
    G.add_node(city)

# Function to add a road dynamically
def add_road(city1, city2, distance):
    if city1 == city2:
        raise ValueError("Cannot connect a city to itself.")
    G.add_edge(city1, city2, weight=distance)  # <- Important!
    return f"Road added: {city1} ⟶ {city2} ({distance} km)"

