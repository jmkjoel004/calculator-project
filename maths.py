from math import *

def fraction(x, y):
    return 3 * (x**2) + sqrt(x**2 + y**2) + exp(log(x))

def linear_formula(m, x, b):
    return m * x + b

def cubic_function(x, a, b, c, d):
    return a * (x**3) + b * (x**2) + c * x + d

def trigonometric_function(x):
    return sin(x)

def f(x, a, b, c):
    expr = a * (x**2) + b * x + c
    return (log(expr) - sin(expr)) / (4 * pi * x**2 + cos(x - 2) * expr)

def polynomial(x, a, b):
    return a * (x**2) + b * x

def pythagoras(a, b):
    return sqrt(a**2 + b**2)

def Cylinder_volume(r, h):
    return pi * r**2 * h

def circle_area(r):
    return 2 * pi * r

def meters_to_feet(m):
    return m / 0.3048

def feet_to_meters(f):
    return f * 0.3048