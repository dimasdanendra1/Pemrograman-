import tkinter as tk

def konversi_suhu():
    try:
        suhu_celcius = float(entry_celcius.get())
        suhu_fahrenheit = (suhu_celcius * 9/5) + 32
        suhu_reamur = suhu_celcius * 4/5
        suhu_kelvin = suhu_celcius + 273.15

        label_fahrenheit_result.config(text=f"{suhu_fahrenheit:.2f} °F", fg="blue")
        label_reamur_result.config(text=f"{suhu_reamur:.2f} °Re", fg="green")
        label_kelvin_result.config(text=f"{suhu_kelvin:.2f} K", fg="red")

    except ValueError:
        label_fahrenheit_result.config(text="Masukkan suhu yang valid!", fg="red")

# Membuat GUI
app = tk.Tk()
app.title("Konversi Suhu")

# Label dan Entry untuk input suhu Celcius
label_celcius = tk.Label(app, text="Suhu Celcius:", font=("Times New Roman", 12))
label_celcius.grid(row=0, column=0, padx=10, pady=10)

entry_celcius = tk.Entry(app, font=("Times New Roman", 12))
entry_celcius.grid(row=0, column=1, padx=10, pady=10)

# Button untuk melakukan konversi suhu
button_konversi = tk.Button(app, text="Konversi", command=konversi_suhu, font=("Times New Roman", 12), bg="gray", fg="white")
button_konversi.grid(row=1, column=0, columnspan=2, pady=10)

# Tabel untuk menampilkan hasil konversi suhu
table_frame = tk.Frame(app)
table_frame.grid(row=2, column=0, columnspan=2, pady=10)

label_fahrenheit = tk.Label(table_frame, text="Fahrenheit:", font=("Times New Roman", 12))
label_fahrenheit.grid(row=0, column=0, padx=10, pady=5)

label_reamur = tk.Label(table_frame, text="Reamur:", font=("Times New Roman", 12))
label_reamur.grid(row=1, column=0, padx=10, pady=5)

label_kelvin = tk.Label(table_frame, text="Kelvin:", font=("Times New Roman", 12))
label_kelvin.grid(row=2, column=0, padx=10, pady=5)

label_fahrenheit_result = tk.Label(table_frame, text="", font=("Times New Roman", 12), fg="blue")
label_fahrenheit_result.grid(row=0, column=1, padx=10, pady=5)

label_reamur_result = tk.Label(table_frame, text="", font=("Times New Roman", 12), fg="green")
label_reamur_result.grid(row=1, column=1, padx=10, pady=5)

label_kelvin_result = tk.Label(table_frame, text="", font=("Times New Roman", 12), fg="red")
label_kelvin_result.grid(row=2, column=1, padx=10, pady=5)

# Menjalankan aplikasi
app.mainloop()
