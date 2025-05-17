import osmnx as ox
import geopandas as gpd
import pandas as pd

def fetch_osm_data(city_name, network_type='drive'):
    """
    Fetch OpenStreetMap data for the given city and network types.
    Args:
        city_name (str): Name of the city.
        network_types (str): Type of network to fetch (e.g., 'drive', 'walk').
    Returns:
        gdf_nodes, gdf_edges: Geodataframes for nodes and edges.
    """
    graph = ox.graph_from_place(city_name, network_type=network_type)
    gdf_nodes, gdf_edges = ox.graph_to_gdfs(graph)
    return gdf_nodes, gdf_edges

# Example usage:
# data = fetch_osm_data("Castellón, Valencian Community, Spain", network_types='drive')

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