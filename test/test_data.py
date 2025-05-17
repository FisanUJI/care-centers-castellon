import pytest
import os
import sys

# Go up to the project root from the 'test' directory
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if repo_root not in sys.path:
    sys.path.append(repo_root)

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