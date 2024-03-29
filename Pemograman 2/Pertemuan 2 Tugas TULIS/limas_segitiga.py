from tkinter import *
import tkinter as tk


app = tk.Tk()
app.minsize(width=500, height=400)
app.title("Luas Dan Alas Bangun Limas Segitiga")


def hitung():
    output_hasil_luas.delete(0, END)
    output_hasil_volume.delete(0, END)

    alas = float(entry_alas.get())
    tinggi = float(entry_tinggi.get())
    ls = 0.5 * alas * tinggi

    luas = ls * 4
    volume = (1/3) * ls * tinggi
    output_hasil_luas.insert(0, round(luas, 2))
    output_hasil_volume.insert(0, round(volume, 2))


# Label Nama
label_nama = tk.Label(
    app, text="Dimas danendra (220511016)")
label_nama.grid(row=0, column=2, padx=5, pady=5)

# Alas Limas
label_alas = tk.Label(app, text="Alas Limas :")
label_alas.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
entry_alas = tk.Entry(app)
entry_alas.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

# Tinggi Limas
label_tinggi = tk.Label(app, text="Tinggi Limas :")
label_tinggi.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
entry_tinggi = tk.Entry(app)
entry_tinggi.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

# button nya
spacer = tk.Label(app, text="")
spacer.grid()
hitung = tk.Button(
    app, text="Hitung", command=hitung, pady=3, padx=3)
hitung.grid(row=5, column=2, padx=5, pady=5)

# output hasilnya
label_hasil_luas = tk.Label(app, text="Luas :", height=2)
label_hasil_luas.grid(row=6, column=0, padx=5, pady=5)
output_hasil_luas = tk.Entry(app)
output_hasil_luas.grid(row=6, column=2, padx=5, pady=5)

label_hasil_volume = tk.Label(app, text="Volume :", height=1)
label_hasil_volume.grid(row=7, column=0, padx=5, pady=5)
output_hasil_volume = tk.Entry(app)
output_hasil_volume.grid(row=7, column=2, padx=5, pady=5)


app.mainloop()
