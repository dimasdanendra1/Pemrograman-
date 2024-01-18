import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Perawat import data_Perawat

class FormPerawat:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='nip:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtnip = Entry(mainFrame) 
        self.txtnip.grid(row=0, column=1, padx=5, pady=5) 
        self.txtnip.bind("<Return>",self.onCari) # menambahkan event Enter key

        Label(mainFrame, text='Nama:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='bagian:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtbagian = Entry(mainFrame) 
        self.txtbagian.grid(row=2, column=1, padx=5, pady=5) 

        # Label(mainFrame, text='Kode Prodi:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        # self.txtKodeProdi = StringVar()
        # Cbo = ttk.Combobox(mainFrame, width = 27, textvariable = self.txtKodeProdi) 
        # Cbo.grid(row=4, column=1, padx=5, pady=5)
        # Cbo['values'] = ('TIF','IND','PET')
        # Cbo.current()      
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        self.btncari = Button(mainFrame, text='Cari', command=self.onCari, width=10)
        self.btncari.grid(row=3, column=3, padx=5, pady=5)

        # define columns
        columns = ('id', 'nip', 'nama','bagian')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('nip', text='nip')
        self.tree.column('nip', width="60")
        self.tree.heading('nama', text='Nama')
        self.tree.column('nama', width="200")
        self.tree.heading('bagian', text='bagian')
        self.tree.column('bagian', width="100")
        # self.tree.heading('kode_prodi', text='Kode Prodi')
        # self.tree.column('kode_prodi', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtnip.delete(0,END)
        self.txtnip.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")       
        self.txtbagian.delete(0,END)
        self.txtbagian.insert(END,"")       
        # self.txtKodeProdi.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        prwt = data_Perawat()
        result = prwt.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        nip = self.txtnip.get()
        prwt = data_Perawat()
        res = prwt.getBynip(nip)
        rec = prwt.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtnip.focus()
        return res
        
    def TampilkanData(self, event=None):
        nip = self.txtnip.get()
        prwt = data_Perawat()
        res = prwt.getBynip(nip)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,prwt.nama)
        self.txtbagian.insert(END,prwt.bagian)
        # self.txtKodeProdi.set(prwt.kode_prodi)   
        self.btnSimpan.config(text="Update")
    
    def onSimpan(self, event=None):
        nip = self.txtnip.get()
        nama = self.txtNama.get()
        bagian = self.txtbagian.get()
        # prodi = self.txtKodeProdi.get()
        
        prwt = data_Perawat()
        prwt.nip = nip
        prwt.nama = nama
        prwt.bagian = bagian
        # prwt.kode_prodi = prodi
        if(self.ditemukan==True):
            res = prwt.updateBynip(nip)
            ket = 'Diperbarui'
        else:
            res = prwt.simpan()
            ket = 'Disimpan'
            
        rec = prwt.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        nip = self.txtnip.get()
        prwt = data_Perawat()
        prwt.nip = nip
        if(self.ditemukan==True):
            res = prwt.deleteBynip(nip)
            rec = prwt.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormPerawat(root, "Aplikasi Data Mahasiswa")
    root.mainloop() 