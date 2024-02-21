import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Radiobutton, ttk, VERTICAL, YES, BOTH, END, Tk, W, StringVar, messagebox
from Apkresto import Apkresto


class AplikasiPemesanan:

    def __init__(self, parent, title, update_main_window):
        self.parent = parent
        self.parent.geometry("1200x700")
        self.update_main_window = update_main_window
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = False
        self.id_order = None
        self.aturKomponen()
        self.onReload()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # Label

        Label(mainFrame, text='Pesan, tunggu, dan nikmati kebahagiaan tak terbatas', font=('Helvetica', 19)).grid(
            row=0, column=2, padx=5, pady=5)

        Label(mainFrame, text='Nama:').grid(
            row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtNama = Entry(mainFrame)
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)

        Label(mainFrame, text='No Hp:').grid(
            row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtNoHp = Entry(mainFrame)
        self.txtNoHp.grid(row=2, column=1, padx=5, pady=5)
        # menambahkan event Enter key

        Label(mainFrame, text='Alamat:').grid(
            row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtAlmt = StringVar()
        self.plered = Radiobutton(mainFrame, text='Plered (10k)',
                                  value='plered', variable=self.txtAlmt)
        self.plered.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        self.plered.select()  # set pilihan yg pertama

        self.watubelah = Radiobutton(mainFrame, text='Watubelah (12k)',
                                     value='watubelah', variable=self.txtAlmt)
        self.watubelah.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        self.sumber = Radiobutton(mainFrame, text='Sumber (14k)',
                                  value='sumber', variable=self.txtAlmt)
        self.sumber.grid(row=5, column=1, padx=5, pady=5, sticky=W)

        # Makanan

        Label(mainFrame, text='Makanan:').grid(
            row=6, column=0, sticky=W, padx=5, pady=5)
        self.txtMakanan = StringVar()
        self.ayambakar = Radiobutton(mainFrame, text='ayam bakar (15k)',
                                     value='ayam bakar', variable=self.txtMakanan)
        self.ayambakar.grid(row=6, column=1, padx=5, pady=5, sticky=W)
        self.ayambakar.select()  # set pilihan yg pertama

        self.sotoayam = Radiobutton(mainFrame, text='soto ayam (12k)',
                                    value='soto ayam', variable=self.txtMakanan)
        self.sotoayam.grid(row=6, column=2, padx=5, pady=5, sticky=W)

        self.ayamgoreng = Radiobutton(mainFrame, text='ayam goreng (14k)',
                                      value='ayam goreng', variable=self.txtMakanan)
        self.ayamgoreng.grid(row=7, column=1, padx=5, pady=5, sticky=W)

        self.ayammadu = Radiobutton(mainFrame, text='ayam madu (14k)',
                                    value='ayam madu', variable=self.txtMakanan)
        self.ayammadu.grid(row=7, column=2, padx=5, pady=5, sticky=W)

        # Minuman

        Label(mainFrame, text='Minuman:').grid(
            row=8, column=0, sticky=W, padx=5, pady=5)
        self.txtMinuman = StringVar()
        self.tehmanis = Radiobutton(mainFrame, text='teh manis (5k)',
                                    value='teh manis', variable=self.txtMinuman)
        self.tehmanis.grid(row=8, column=1, padx=5, pady=5, sticky=W)
        self.tehmanis.select()  # set pilihan yg pertama

        self.jusjeruk = Radiobutton(mainFrame, text='jus jeruk (10k)',
                                    value='jus jeruk', variable=self.txtMinuman)
        self.jusjeruk.grid(row=8, column=2, padx=5, pady=5, sticky=W)

        self.airtawar = Radiobutton(mainFrame, text='air tawar (3k)',
                                    value='air tawar', variable=self.txtMinuman)
        self.airtawar.grid(row=9, column=1, padx=5, pady=5, sticky=W)

        self.jusapel = Radiobutton(mainFrame, text='jus apel (14k)',
                                   value='jus apel', variable=self.txtMinuman)
        self.jusapel.grid(row=9, column=2, padx=5, pady=5, sticky=W)

        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan',
                                command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=10, column=0, pady=5)
        self.btnClear = Button(mainFrame, text='Hapus',
                               command=self.onDelete, width=10)
        self.btnClear.grid(row=10, column=1, pady=5)

        # define columns
        columns = ('idorder', 'nama', 'no hp', 'alamat',
                   "ongkir", "makanan", "minuman", "total")

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idorder', text='ID')
        self.tree.column('idorder', width="30")
        self.tree.heading('nama', text='Nama')
        self.tree.column('nama', width="200")
        self.tree.heading('no hp', text='No HP')
        self.tree.column('no hp', width="80")
        self.tree.heading('alamat', text='Alamat')
        self.tree.column('alamat', width="100")
        self.tree.heading('ongkir', text='Ongkir')
        self.tree.column('ongkir', width="80")
        self.tree.heading('makanan', text='Makanan')
        self.tree.column('makanan', width="200")
        self.tree.heading('minuman', text='Minuman')
        self.tree.column('minuman', width="200")
        self.tree.heading('total', text='Total')
        self.tree.column('total', width="80")
        # set tree position
        self.tree.place(x=0, y=400)
        self.onReload()

        # Mengaitkan fungsi on_tree_click dengan event Button-1 (klik kiri mouse)
        self.tree.bind("<<TreeviewSelect>>",
                       self.on_tree_click)

    def on_tree_click(self, event):
        selected_item = self.tree.selection()[0]  # Get the selected item
        # Get the value in the first column (ID)
        id_order = self.tree.item(selected_item, "values")[0]
        print(self.tree.item(selected_item, "values"))
        # print("ID Order:", id_order)
        self.id_order = id_order
        return

    def onClear(self, event=None):
        self.txtNoHp.delete(0, END)
        self.txtNoHp.insert(END, "")
        self.txtNama.delete(0, END)
        self.txtNama.insert(END, "")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False

    def onReload(self, event=None):
        # get data mahasiswa
        order = Apkresto()
        result = order.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        pesanan = []
        for row_data in result:
            pesanan.append(row_data)

        for psnn in pesanan:
            self.tree.insert('', END, values=psnn)

    # def onCari(self, event=None):
    #     nip = self.txtNoHp.get()
    #     order = Apkresto()
    #     res = order.getByNIP(nip)
    #     rec = order.affected
    #     if (rec > 0):
    #         messagebox.showinfo("showinfo", "Data Ditemukan")
    #         # self.TampilkanData()
    #         self.ditemukan = True
    #     else:
    #         self.ditemukan = False
    #         self.txtNama.focus()
    #     return res

    # def TampilkanData(self, event=None):
    #     nip = self.txtNoHp.get()
    #     order = Apkresto()
    #     res = order.getByNIP(nip)
    #     self.txtNama.delete(0, END)
    #     self.txtNama.insert(END, order.nama)
    #     jk = order.jk
    #     if (jk == "P"):
    #         self.P.select()
    #     else:
    #         self.L.select()

    #     self.btnSimpan.config(text="Update")

    def onSimpan(self, event=None):
        nama = self.txtNama.get()
        nohp = self.txtNoHp.get()
        alamat = self.txtAlmt.get()
        makanan = self.txtMakanan.get()
        minuman = self.txtMinuman.get()
        ongkir = 0
        total = 0
        hargaMakanan = 0
        hargaMinuman = 0

        order = Apkresto()
        order.nohp = nohp
        order.nama = nama
        order.alamat = alamat
        order.makanan = makanan
        order.minuman = minuman

        if alamat == "plered":
            ongkir = 10000
        elif alamat == "watubelah":
            ongkir = 12000
        else:
            ongkir = 14000

        if makanan == "ayam bakar":
            hargaMakanan = 15000
        elif makanan == "soto ayam":
            hargaMakanan = 12000
        elif makanan == "ayam goreng":
            hargaMakanan = 14000
        else:
            hargaMakanan = 14000

        if minuman == "teh manis":
            hargaMinuman = 5000
        elif minuman == "jus jeruk":
            hargaMinuman = 10000
        elif minuman == "air tawar":
            hargaMinuman = 3000
        else:
            hargaMinuman = 14000

        total = ongkir + hargaMinuman + hargaMakanan

        order.simpan(total, ongkir)

        rec = order.affected
        if (rec > 0):
            messagebox.showinfo("Dimas Restauran",
                                "Pesanan berhasil di Pesan ")
        else:
            messagebox.showwarning("Dimas Restauran", "Pesanan gagal di Pesan")
        self.onClear()
        return rec

    def onDelete(self, event=None):
        order = Apkresto()
        if self.id_order == None:
            messagebox.showerror("Dimas Restaurant",
                                 "Pilih Orderan yang mau di hapus")
            return

        order.delete(self.id_order)
        rec = order.affected

        if (rec > 0):
            messagebox.showinfo("Dimas Restaurant",
                                "Orderan Berhasil dihapus")
        else:
            messagebox.showinfo("showinfo", "Orderan Gagal dihapus")

        self.onClear()

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()


if __name__ == '__main__':
    def update_main_window(result):
        print(result)

    root = tk.Tk()
    aplikasi = AplikasiPemesanan(
        root, "Dimas Restaurant", update_main_window)
    root.mainloop()
