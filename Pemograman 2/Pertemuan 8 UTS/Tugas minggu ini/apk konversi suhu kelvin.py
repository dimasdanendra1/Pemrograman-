import tkinter as tk
from tkinter import ttk

def konversi_suhu():
    try:
        kelvin = float(entry_kelvin.get())
        celcius = kelvin - 273.15
        fahrenheit = (kelvin * 9/5) - 459.67
        reamur = (kelvin - 273.15) * 4/5

        label_celcius.config(text=f"Celcius: {celcius:.2f} °C", fg="blue")
        label_fahrenheit.config(text=f"Fahrenheit: {fahrenheit:.2f} °F", fg="green")
        label_reamur.config(text=f"Reamur: {reamur:.2f} °Re", fg="red")
    except ValueError:
        label_celcius.config(text="Input tidak valid", fg="black")
        label_fahrenheit.config(text="Fahrenheit:", fg="black")
        label_reamur.config(text="Reamur:", fg="black")

# Membuat jendela utama
root = tk.Tk()
root.title("Konversi Suhu Kelvin")
root.geometry("400x200")

# Membuat label dan entry untuk input suhu dalam Kelvin
label_kelvin = tk.Label(root, text="Masukkan suhu dalam Kelvin:", font=("Times New Roman", 12), fg="black")
label_kelvin.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_kelvin = tk.Entry(root, font=("Times New Roman", 12), bg="#FFD700")  # Warna kuning muda
entry_kelvin.grid(row=0, column=1, padx=10, pady=10)

# Membuat tombol konversi
button_konversi = tk.Button(root, text="Konversi", command=konversi_suhu, font=("Times New Roman", 12), bg="#98FB98")
button_konversi.grid(row=1, column=0, columnspan=2, pady=10)

# Membuat label untuk menampilkan hasil konversi
label_celcius = tk.Label(root, text="Celcius:", font=("Times New Roman", 12), fg="blue")
label_celcius.grid(row=2, column=0, padx=10, pady=5, sticky="w")

label_fahrenheit = tk.Label(root, text="Fahrenheit:", font=("Times New Roman", 12), fg="green")
label_fahrenheit.grid(row=3, column=0, padx=10, pady=5, sticky="w")

label_reamur = tk.Label(root, text="Reamur:", font=("Times New Roman", 12), fg="red")
label_reamur.grid(row=4, column=0, padx=10, pady=5, sticky="w")

# Menjalankan aplikasi
root.mainloop()
