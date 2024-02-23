import tkinter as tk
from tkinter import messagebox
import math
import scipy.constants as const

class WaveguideCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Waveguide Wavelength Calculator")

        self.frequency_label = tk.Label(master, text="Operating Frequency (Hz):")
        self.frequency_label.grid(row=0, column=0, sticky="w")
        self.frequency_entry = tk.Entry(master)
        self.frequency_entry.grid(row=0, column=1)

        self.width_label = tk.Label(master, text="Waveguide Width (m):")
        self.width_label.grid(row=1, column=0, sticky="w")
        self.width_entry = tk.Entry(master)
        self.width_entry.grid(row=1, column=1)

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate_wavelength)
        self.calculate_button.grid(row=2, column=0, columnspan=2)

        self.result_label = tk.Label(master, text="Result:")
        self.result_label.grid(row=3, column=0, sticky="w")
        self.result_value = tk.Label(master, text="")
        self.result_value.grid(row=3, column=1, sticky="w")

    def calculate_wavelength(self):
        try:
            f = float(self.frequency_entry.get())
            a = float(self.width_entry.get())

            c = const.c
            λ_g = (c / f)*(1 / math.sqrt(1 - (c / (2 * a * f)) ** 2))
            wavelength = λ_g * 10 ** 3  # in mm

            self.result_value.config(text=f"{wavelength:.2f} mm\nQuarter Wavelength: {wavelength/4:.2f} mm")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for Frequency and Width.")

def main():
    root = tk.Tk()
    app = WaveguideCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
