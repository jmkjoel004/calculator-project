import tkinter as tk
from tkinter import ttk, messagebox
from maths import (
    fraction, polynomial, f, pythagoras,
    circle_area, Cylinder_volume, meters_to_feet, feet_to_meters
)

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maths Calculator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Title
        ttk.Label(root, text="Calculator", font=("Helvetica", 18)).pack(pady=10)

        # Dropdown for function selection
        self.function_var = tk.StringVar()
        self.function_list = [
            "Fraction (3x² + √(x² + y²) + e^ln(x))",
            "Polynomial (ax² + bx)",
            "f(x) = (ln(ax² + bx + c) - sin(...)) / ...",
            "Pythagoras (√(a² + b²))",
            "Circle Area (2πr)",
            "Cylinder Volume (πr²h)",
            "Meters to Feet",
            "Feet to Meters"
        ]
        ttk.Label(root, text="Choose Function:").pack()
        self.dropdown = ttk.Combobox(root, values=self.function_list, state="readonly", textvariable=self.function_var)
        self.dropdown.pack(pady=5)
        self.dropdown.bind("<<ComboboxSelected>>", self.update_inputs)

        # Frame for dynamic inputs
        self.input_frame = ttk.Frame(root)
        self.input_frame.pack(pady=10)

        # Calculate button
        ttk.Button(root, text="Calculate", command=self.calculate).pack(pady=10)

        # Result
        self.result_var = tk.StringVar()
        ttk.Label(root, textvariable=self.result_var, font=("Helvetica", 14), foreground="blue").pack(pady=10)

    def update_inputs(self, event=None):
        # Clear current inputs
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        self.entries = {}
        selected = self.function_var.get()

        if "Fraction" in selected:
            vars_needed = ['x', 'y']
        elif "Polynomial" in selected:
            vars_needed = ['x', 'a', 'b']
        elif "f(x)" in selected:
            vars_needed = ['x', 'a', 'b', 'c']
        elif "Pythagoras" in selected:
            vars_needed = ['a', 'b']
        elif "Circle" in selected:
            vars_needed = ['r']
        elif "Cylinder" in selected:
            vars_needed = ['r', 'h']
        elif "Meters to Feet" in selected:
            vars_needed = ['Meters']
        elif "Feet to Meters" in selected:
            vars_needed = ['Feet']
        else:
            vars_needed = []

        for var in vars_needed:
            ttk.Label(self.input_frame, text=f"{var} = ").pack()
            entry = ttk.Entry(self.input_frame)
            entry.pack()
            self.entries[var] = entry

    def calculate(self):
        selected = self.function_var.get()
        try:
            values = {k: float(v.get()) for k, v in self.entries.items()}

            if "Fraction" in selected:
                result = fraction(values['x'], values['y'])
            elif "Polynomial" in selected:
                result = polynomial(values['x'], values['a'], values['b'])
            elif "f(x)" in selected:
                result = f(values['x'], values['a'], values['b'], values['c'])
            elif "Pythagoras" in selected:
                result = pythagoras(values['a'], values['b'])
            elif "Circle" in selected:
                result = circle_area(values['r'])
            elif "Cylinder" in selected:
                result = Cylinder_volume(values['r'], values['h'])
            elif "Meters to Feet" in selected:
                result = meters_to_feet(values['Meters'])
            elif "Feet to Meters" in selected:
                result = feet_to_meters(values['Feet'])
            else:
                result = "Unknown operation"

            self.result_var.set(f"Result: {round(result, 3)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
