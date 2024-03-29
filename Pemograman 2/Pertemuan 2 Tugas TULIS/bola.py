from tkinter import *
import tkinter as tk
from math import pi

app = tk.Tk()
app.minsize(width=500, height=400)
app.title("Luas Dan Alas Bangun Bola")


def hitung():
    output_hasil_luas.delete(0, END)
    output_hasil_volume.delete(0, END)

    radius = float(entry_radius.get())
    luas = 4 * pi * radius**2
    volume = (4/3) * pi * radius**3
    output_hasil_luas.insert(0, round(luas, 2))
    output_hasil_volume.insert(0, round(volume, 2))


# Label Nama
label_nama = tk.Label(
    app, text="Dimas danendra (220511016)")
label_nama.grid(row=0, column=2, padx=5, pady=5)

# Radius
label_radius = tk.Label(app, text="Radius Bola : ")
label_radius.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
entry_radius = tk.Entry(app)
entry_radius.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

# button nya
spacer = tk.Label(app, text="")
spacer.grid()
hitung = tk.Button(
    app, text="Hitung", command=hitung, pady=3, padx=3)
hitung.grid(row=4, column=2, padx=5, pady=5)

# output hasilnya
label_hasil_luas = tk.Label(app, text="Luas : ", height=2)
label_hasil_luas.grid(row=6, column=0, padx=5, pady=5)
output_hasil_luas = tk.Entry(app)
output_hasil_luas.grid(row=6, column=2, padx=5, pady=5)

label_hasil_volume = tk.Label(app, text="Volume : ", height=1)
label_hasil_volume.grid(row=7, column=0, padx=5, pady=5)
output_hasil_volume = tk.Entry(app)
output_hasil_volume.grid(row=7, column=2, padx=5, pady=5)


app.mainloop()
