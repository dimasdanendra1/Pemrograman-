import tkinter as tk
from tkinter import ttk

def konversi_suhu():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celcius = (fahrenheit - 32) * 5/9
        reamur = (fahrenheit - 32) * 4/9
        kelvin = (fahrenheit + 459.67) * 5/9

        label_celcius.config(text=f"Celcius: {celcius:.2f} °C")
        label_reamur.config(text=f"Reamur: {reamur:.2f} °Re")
        label_kelvin.config(text=f"Kelvin: {kelvin:.2f} K")
    except ValueError:
        label_celcius.config(text="Input tidak valid")
        label_reamur.config(text="Reamur:")
        label_kelvin.config(text="Kelvin:")

# Membuat jendela utama
root = tk.Tk()
root.title("Konversi Suhu Fahrenheit")
root.geometry("400x200")

# Membuat label dan entry untuk input suhu dalam Fahrenheit
label_fahrenheit = tk.Label(root, text="Masukkan suhu dalam Fahrenheit:")
label_fahrenheit.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_fahrenheit = tk.Entry(root, font=("Times New Roman", 12), bg="#FFFFE0")
entry_fahrenheit.grid(row=0, column=1, padx=10, pady=10)

# Membuat tombol konversi
button_konversi = tk.Button(root, text="Konversi", command=konversi_suhu, font=("Times New Roman", 12), bg="#98FB98")
button_konversi.grid(row=1, column=0, columnspan=2, pady=10)

# Membuat label untuk menampilkan hasil konversi
label_celcius = tk.Label(root, text="Celcius:", font=("Times New Roman", 12), fg="blue")
label_celcius.grid(row=2, column=0, padx=10, pady=5, sticky="w")

label_reamur = tk.Label(root, text="Reamur:", font=("Times New Roman", 12), fg="green")
label_reamur.grid(row=3, column=0, padx=10, pady=5, sticky="w")

label_kelvin = tk.Label(root, text="Kelvin:", font=("Times New Roman", 12), fg="red")
label_kelvin.grid(row=4, column=0, padx=10, pady=5, sticky="w")

# Menjalankan aplikasi
root.mainloop()
