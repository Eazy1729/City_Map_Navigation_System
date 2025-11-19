"""
Main CLI for City Map Navigation
"""
# map.py
import folium
from graph import G, cities

def create_map(shortest_path=None, path_distance=None):
    """
    Creates and returns a Folium map with:
    - All cities as markers
    - All roads as blue lines
    - Shortest path as a red line (optional)
    """
    # Center the map approximately
    m = folium.Map(location=[30.5, 71.5], zoom_start=5)

    # Add city markers
    for city, coord in cities.items():
        folium.Marker(location=coord, popup=city).add_to(m)

    # Draw all roads
    for c1, c2, data in G.edges(data=True):
        coords = [cities[c1], cities[c2]]
        folium.PolyLine(coords, color="blue", weight=3, tooltip=f"{data['weight']} km").add_to(m)

    # Draw shortest path if provided
    if shortest_path:
        path_coords = [cities[city] for city in shortest_path]
        folium.PolyLine(path_coords, color="red", weight=5, tooltip=f"{path_distance} km").add_to(m)

    return m
