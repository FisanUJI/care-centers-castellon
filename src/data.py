import osmnx as ox
import geopandas as gpd
import pandas as pd

def fetch_osm_data(city_name, network_types=['drive']):
    """
    Fetch OpenStreetMap data for the given city and network types.
    Args:
        city_name (str): Name of the city.
        network_types (list or str): List of network types to fetch (e.g., ['drive', 'walk'] or 'drive').
    Returns:
        dict: {network_type: (gdf_nodes, gdf_edges)}
    """
    import osmnx as ox

    # If a single string is given, convert to list
    if isinstance(network_types, str):
        network_types = [network_types]

    results = {}
    for net_type in network_types:
        graph = ox.graph_from_place(city_name, network_type=net_type)
        gdf_nodes, gdf_edges = ox.graph_to_gdfs(graph)
        results[net_type] = (gdf_nodes, gdf_edges)
    return results

# Example usage:
# data = fetch_osm_data("Castellón, Valencian Community, Spain", network_types=['drive', 'walk'])
# drive_nodes, drive_edges = data['drive']
# walk_nodes, walk_edges = data['walk']


def clean_data(gdf_edges):
    """
    Clean the edges GeoDataFrame by removing irrelevant columns.
    Args:
        gdf_edges (GeoDataFrame): DataFrame containing edge data.
    Returns:
        GeoDataFrame: Cleaned edge data.
    """
    columns_to_drop = ["lanes", "ref", "bridge", "maxspeed", "tunnel", "junction", "width", "access", "service"]
    return gdf_edges.drop(columns=columns_to_drop, errors='ignore')