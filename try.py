# try.py
from maths import circle_area, fraction, f, meters_to_feet, polynomial, pythagoras, Cylinder_volume, feet_to_meters
from utils import plot_function, toggle_unit_system, UnitSystem
unit_system = UnitSystem.METRIC
from datetime import datetime
import numpy as np
from colorama import Fore, Style, init
from pyfiglet import figlet_format
init(autoreset=True)

print(figlet_format("My Calculator", font="slant"))

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Initialize result variables
error_occurred = None
frac_result = None
f_result = None
poly_result = None
pythagoras_result = None
cylinder_volume_result = None
meters_to_feet_result = None
circle_area_result = None
feet_to_meters_result = None
again = 'yes'

def show_menu():
    return input(
        "What do you want to solve?\n"
        "A - Fraction\n"
        "B - Polynomial\n"
        "C - f(x)\n"
        "D - Pythagoras\n"
        "E - Cylinder Volume\n"
        "F - Meters to Feet\n"
        "G - Circle Area\n"
        "H - Feet to Meters\n"
        "I - Graph f(x)\n"
        "J - Graph Polynomial\n"
        "K - Toggle Unit System\n"

        "Enter your choice: "
    ).strip().lower()

name = input("name: " )


try:
    while again == 'yes':
        print(figlet_format(name, font="isometric1"))

        respond = show_menu()

        match respond :
            case 'a':
                x = float(input("x = "))
                y = float(input("y = "))
                frac_result = round(fraction(x, y), 3)
                print(Fore.GREEN + "Fraction:", frac_result)

            case 'c':
                x = float(input("x = "))
                a = float(input("a = "))
                b = float(input("b = "))
                c = float(input("c = "))
                f_result = round(f(x, a, b, c), 3)
                print(Fore.CYAN  + "f(x):", f_result)

            case 'b':
                x = float(input("x = "))
                a = float(input("a = "))
                b = float(input("b = "))
                poly_result = round(polynomial(x, a, b), 3)
                print(Fore.CYAN  + "Polynomial:", poly_result)

            case 'd':
                a = float(input("a = "))
                b = float(input("b = "))
                pythagoras_result = round(pythagoras(a, b) , 3)
                print(Fore.CYAN  + "Pythagoras:", pythagoras_result)

            case 'e':
                r = float(input("raduis r = "))
                h = float(input("h = "))
                cylinder_volume_result = round(Cylinder_volume(r, h), 3)
                print(Fore.CYAN  + "Cylinder Volume:", cylinder_volume_result)

            case 'f':
                m = float(input("m = ")) 
                meters_to_feet_result = round(meters_to_feet(m), 3)
                print(Fore.CYAN  + "feet: ", meters_to_feet_result)
        
            case 'g':
                r = float(input("radius r= "))
                circle_area_result = round(circle_area(r), 3)
                print(Fore.CYAN  + "Circle area : ", circle_area_result)

            case 'h': # Meter
                f = float(input("Feet = "))
                feet_to_meters_result = round(feet_to_meters(f), 3)
                print(Fore.CYAN  + "meters : ", feet_to_meters_result)

            case 'i':  # Graph f(x)
                a = float(input("a = "))
                b = float(input("b = "))
                c = float(input("c = "))
                def fx(x):  # Vectorized version using NumPy
                    expr = a * (x**2) + b * x + c
                    return (np.log(expr) - np.sin(expr)) / (4 * np.pi * x**2 + np.cos(x - 2) * expr)
                plot_function(fx, label="f(x)")

            case 'j':  # Graph Polynomial
                a = float(input("a = "))
                b = float(input("b = "))
                def poly(x):
                    return a * (x**2) + b * x
                plot_function(poly, label="Polynomial")

            case 'k':
                unit_system = toggle_unit_system(unit_system)
                print(Fore.YELLOW + f"Unit system switched to: {unit_system.value}")

            case __:
                print(Fore.RED + "Invalid choice. Please try again.")
                respond = show_menu()

        again = input("Continue? (yes/no): ").strip().lower()

    goodbye_text = figlet_format("Goodbye!", font="starwars", width=80)
    print(Fore.BLUE + goodbye_text)


except Exception as e:
    error_occurred = str(e)
    print(Fore.RED + "Something went wrong:", e)

# Save results to file
with open("results.txt", "a", encoding="utf-8") as file:
    now = datetime.now()
    file.write(f"\n==== Session on {now} ====\n")

    if error_occurred is not None:
        file.write(f"\nSomething went wrong: {error_occurred}\n")
    if name is not None:
        file.write(f"Name : {name}\n")
    if frac_result is not None:
        file.write(f"Fraction result: {frac_result}\n")
    if f_result is not None:
        file.write(f"f(x) result: {f_result}\n")
    if poly_result is not None:
        file.write(f"Polynomial result: {poly_result}\n")
    if pythagoras_result is not None:
        file.write(f"Pythagoras result: {pythagoras_result}\n")
    if cylinder_volume_result is not None:
        file.write(f"Cylinder Volume result: {cylinder_volume_result}\n")
    if meters_to_feet_result is not None:
        file.write(f"Feet result: {meters_to_feet_result}\n")
    if circle_area_result is not None:
        file.write(f"Circle result: {circle_area_result}\n")
    if feet_to_meters_result is not None:
        file.write(f"Meters result: {feet_to_meters_result}\n")

