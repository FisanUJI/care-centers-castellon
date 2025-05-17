import pytest
from src.data import fetch_osm_data, clean_data

def test_fetch_osm_data():
    city_name = "Castellón, Valencian Community, Spain"
    gdf_nodes, gdf_edges = fetch_osm_data(city_name)
    assert not gdf_nodes.empty
    assert not gdf_edges.empty

def test_clean_data():
    city_name = "Castellón, Valencian Community, Spain"
    _, gdf_edges = fetch_osm_data(city_name)
    cleaned_data = clean_data(gdf_edges)
    assert "bridge" not in cleaned_data.columns