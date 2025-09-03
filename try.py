# try.py
from maths import circle_area, fraction, f, meters_to_feet, polynomial, pythagoras, Cylinder_volume, feet_to_meters
from datetime import datetime
from colorama import Fore, Style, init
from pyfiglet import figlet_format
init(autoreset=True)

print(figlet_format("My Calculator", font="slant"))

# Initialize result variables
error_occurred = None
frac_result = None
f_result = None
poly_result = None
pythagoras_result = None
Cylinder_volume_result = None
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
        "Enter your choice: "
    ).strip().lower()


try:
    while again == 'yes':
        name = input("name: " )
        print(figlet_format(name, font="isometric1"))

        respond = show_menu()

        if respond == 'a':
            x = float(input("x = "))
            y = float(input("y = "))
            frac_result = round(fraction(x, y), 3)
            print(Fore.GREEN + "Fraction:", frac_result)

        elif respond == 'c':
            x = float(input("x = "))
            a = int(input("a = "))
            b = int(input("b = "))
            c = int(input("c = "))
            f_result = round(f(x, a, b, c), 3)
            print(Fore.CYAN  + "f(x):", f_result)

        elif respond == 'b':
            x = int(input("x = "))
            a = int(input("a = "))
            b = int(input("b = "))
            poly_result = round(polynomial(x, a, b), 3)
            print(Fore.CYAN  + "Polynomial:", poly_result)

        elif respond == 'd':
            a = float(input("a = "))
            b = float(input("b = "))
            pythagoras_result = round(pythagoras(a, b) , 3)
            print(Fore.CYAN  + "Pythagoras:", pythagoras_result)

        elif respond == 'e':
            r = float(input("r = "))
            h = float(input("h = "))
            Cylinder_volume_result = round(Cylinder_volume(r, h), 3)
            print(Fore.CYAN  + "Cylinder Volume:", Cylinder_volume_result)

        elif respond == 'f':
            m = float(input("m = ")) 
            meters_to_feet_result = round(meters_to_feet(m), 3)
            print(Fore.CYAN  + "feet: ", meters_to_feet_result)
        
        elif respond == 'g':
            r = float(input("r= "))
            circle_area_result = round(circle_area(r), 3)
            print(Fore.CYAN  + "Cicle area : ", circle_area_result)

        elif respond =='h':
            f = float(input("Feet = "))
            feet_to_meters_result = round(feet_to_meters(f), 3)
            print(Fore.CYAN  + "meters : ", feet_to_meters_result)

        else:
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
    if error_occurred is not None:
        file.write(f"Date and time: {now}\nSomething went wrong: {error_occurred}\n")
    if name is not None:
        file.write(f"Name : {name}\n")
    if frac_result is not None:
        file.write(f"Date and time: {now}\nFraction result: {frac_result}\n")
    if f_result is not None:
        file.write(f"Date and time: {now}\nf(x) result: {f_result}\n")
    if poly_result is not None:
        file.write(f"Date and time: {now}\nPolynomial result: {poly_result}\n")
    if pythagoras_result is not None:
        file.write(f"Date and time: {now}\nPythagoras result: {pythagoras_result}\n")
    if Cylinder_volume_result is not None:
        file.write(f"Date and time: {now}\nCylinder Volume result: {Cylinder_volume_result}\n")
    if meters_to_feet_result is not None:
        file.write(f"Date and time: {now}\nFeet result: {meters_to_feet_result}\n")
    if circle_area_result is not None:
        file.write(f"Date and time: {now}\nCircle result: {circle_area_result}\n")
    if feet_to_meters_result is not None:
        file.write(f"Date and time: {now}\nMeters result: {feet_to_meters_result}\n")

