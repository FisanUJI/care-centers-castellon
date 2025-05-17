# import folium
# from src.config import CASTELLON_CENTER, CASTELLON_ZOOM, GEOJSON_PATH

# def generate_castellon_map():
#     """
#     Generate an interactive map of Castellon de la Plana.
#     Returns:
#         folium.Map: A Folium map object.
#     """
#     castellon_map = folium.Map(location=CASTELLON_CENTER, zoom_start=CASTELLON_ZOOM)
#     folium.GeoJson(
#         GEOJSON_PATH,
#         name="Castellon Boundary",
#         style_function=lambda x: {
#             'fillColor': 'grey',
#             'color': 'black',
#             'weight': 2,
#             'fillOpacity': 0.5
#         }
#     ).add_to(castellon_map)
#     folium.Marker(
#         location=CASTELLON_CENTER,
#         popup="Castellon de la Plana",
#         icon=folium.Icon(color='blue')
#     ).add_to(castellon_map)
#     folium.LayerControl().add_to(castellon_map)

#     # Save the map to an HTML file
#     castellon_map.save("../data/images/castellon_map.html")
#     return castellon_map

import folium
import json
from pathlib import Path
from src.config import CASTELLON_CENTER, CASTELLON_ZOOM, GEOJSON_PATH

def generate_castellon_map(output_path="data/images/castellon_map.html"):
    """
    Generate an interactive map of Castellon de la Plana and save as HTML.

    Args:
        output_path (str): Relative or absolute path to save the HTML map.
        Default is "data/images/castellon_map.html"

    Returns:
        folium.Map: A Folium map object.
    """
    # Initialize the map centered on Castellon
    castellon_map = folium.Map(
        location=CASTELLON_CENTER,
        zoom_start=CASTELLON_ZOOM,
        control_scale=True,
        tiles="OpenStreetMap"
    )

    # Load GeoJSON data
    geo_path = Path(GEOJSON_PATH)
    if not geo_path.exists():
        raise FileNotFoundError(f"GeoJSON file not found: {geo_path}")

    with geo_path.open('r', encoding='utf-8') as f:
        geojson_data = json.load(f)

    # Add boundary layer
    folium.GeoJson(
        geojson_data,
        name="Castellon Boundary",
        style_function=lambda feature: {
            'fillColor': 'lightgray',
            'color': 'black',
            'weight': 2,
            'fillOpacity': 0.5,
        }
    ).add_to(castellon_map)

    # Add marker
    folium.Marker(
        location=CASTELLON_CENTER,
        popup="📍 Castellon de la Plana",
        tooltip="Click for more info",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(castellon_map)

    # Add layer control
    folium.LayerControl().add_to(castellon_map)

    # Save map as HTML
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)  # Ensure directory exists
    castellon_map.save(output_path)

    return castellon_map
