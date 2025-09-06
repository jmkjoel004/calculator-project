import matplotlib.pyplot as plt
import numpy as np
from enum import Enum

class UnitSystem(Enum):
    METRIC = "Metric"
    IMPERIAL = "Imperial"

def plot_function(func, x_range=(-10, 10), label="f(x)", **kwargs):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = func(x)
    
    plt.plot(x, y, label=label)
    plt.title(f"Graph of {label}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

def toggle_unit_system(current_unit):
    return UnitSystem.METRIC if current_unit == UnitSystem.IMPERIAL else UnitSystem.IMPERIAL
