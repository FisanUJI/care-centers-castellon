import folium
from src.config import CASTELLON_CENTER, CASTELLON_ZOOM, GEOJSON_PATH

def generate_castellon_map():
    """
    Generate an interactive map of Castellon de la Plana.
    Returns:
        folium.Map: A Folium map object.
    """
    castellon_map = folium.Map(location=CASTELLON_CENTER, zoom_start=CASTELLON_ZOOM)
    folium.GeoJson(
        "../data/raw/georef-spain-provincia.geojson",
        name="Castellon Boundary",
        style_function=lambda x: {
            'fillColor': 'grey',
            'color': 'black',
            'weight': 2,
            'fillOpacity': 0.5
        }
    ).add_to(castellon_map)
    return castellon_map