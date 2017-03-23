import geopandas as gpd

GEOJSON_PATH = '../.data/bordeaux.geojson'

gdf = gpd.read_file(GEOJSON_PATH)

gdf.crs

# In angular degrees

float(gdf.geometry.area)


# Webmercator area (in Km^2)

float(gdf.to_crs({'init': 'epsg:3857'}).area / (1000 * 1000))


# Equal Area Cylindrical (in Km^2)


float(gdf.to_crs({'proj': 'cea'}).area / (1000 * 1000))
