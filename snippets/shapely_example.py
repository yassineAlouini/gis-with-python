from shapely.geometry import Point
from math import pi

radius = 10.0
approximate_circle = Point(0.0, 0.0).buffer(radius, resolution=256)

approximate_circle.area

pi * radius ** 2
