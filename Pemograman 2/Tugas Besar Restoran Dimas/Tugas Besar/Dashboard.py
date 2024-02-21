import tkinter as tk
from tkinter import Menu, messagebox
from FrmLogin import *
from FrmApkresto import *


class Dashboard:
    def __init__(self):
        # root window
        self.root = tk.Tk()
        self.root.title('Restaurant Dimas Jaya')
        # self.root.attributes('-fullscreen', True)
        self.root.geometry("1200x800")
        self.__data = None
        self.__level = None
        # create a menubar
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        # create menus
        self.file_menu = Menu(self.menubar)
        self.guest_menu = Menu(self.menubar)
        self.admin_menu = Menu(self.menubar)
        self.mahasiswa_menu = Menu(self.menubar)
        self.dosen_menu = Menu(self.menubar)

        # add menu items to File menu
        self.file_menu.add_command(
            label='Login', command=lambda: self.new_window("Login", FormLogin))
        self.file_menu.add_command(label='Exit', command=self.root.destroy)

        # add menu items to menu Admin
        self.admin_menu.add_command(
            label='Order Makanan', command=lambda: self.new_window("Order", AplikasiPemesanan))

        # add menus to the menubar
        self.menubar.add_cascade(label="File", menu=self.file_menu)

    def new_window(self, number, _class):
        new = tk.Toplevel(self.root)
        new.transient()
        new.grab_set()
        _class(new, number, self.update_main_window)

    def update_main_window(self, data):
        # Method to receive data from child windows
        self.__data = data
        level = "admin"
        loginvalid = self.__data[1]
        if (loginvalid == True):
            index = self.file_menu.index('Login')
            # hapus menu login
            self.file_menu.delete(index)
            self.file_menu.add_command(label='Logout', command=self.Logout)

            # tambahkan menu sesuai level
            if (level == 'admin'):
                self.menubar.add_cascade(label="Order", menu=self.admin_menu)

                self.__level = 'Admin'

    def Logout(self):
        index = self.file_menu.index('Logout')
        self.file_menu.delete(index)
        self.file_menu.add_command(
            label='Login', command=lambda: self.new_window("Log Me In", FormLogin))
        self.remove_all_menus()

    def remove_all_menus(self):
        index = self.menubar.index(self.__level)
        if index is not None:
            self.menubar.delete(index)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    menu_app = Dashboard()
    menu_app.run()
