from functools import partial
import pyproj
from shapely.ops import transform
from shapely.geometry import Point


# g = partial(f, a, b) => g(x, y) = f(a, b, x, y)

project = partial(
    pyproj.transform,
    pyproj.Proj(init='epsg:4326'),  # GPS
    pyproj.Proj(init='epsg:3857'))  # Webmercator

bordeaux_center = Point(-0.5667, 44.8333)  # Longitude, Latitude
projected_bordeaux_center = transform(project, bordeaux_center)

# In degrees
str(bordeaux_center)
# In meters
str(projected_bordeaux_center)
