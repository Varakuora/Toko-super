# File: views/menu.py
import tkinter as tk
from tkinter import messagebox, simpledialog
from controllers.sales_controller import SalesController

class MenuView:
    def __init__(self, root, inventory_controller, sales_controller):
        self.root = root
        self.root.title("Toko Super")
        self.inventory_controller = inventory_controller
        self.sales_controller = sales_controller

        # Inisialisasi informasi login
        self.logged_in = False
        self.username = ""

        # GUI
        self.root.geometry("400x300")
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Submenu Produk
        self.product_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Produk", menu=self.product_menu)
        self.product_menu.add_command(label="Tambah Produk", command=self.add_product)

        # Submenu Penjualan
        self.sales_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Penjualan", menu=self.sales_menu)
        self.sales_menu.add_command(label="Buat Penjualan", command=self.make_sale)
        self.sales_menu.add_command(label="Laporan Penjualan", command=self.generate_sales_report)

        # Submenu Keamanan
        self.security_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Keamanan", menu=self.security_menu)
        self.security_menu.add_command(label="Login", command=self.login)

    def add_product(self):
        product_name = simpledialog.askstring("Tambah Produk", "Masukkan nama produk:")
        product_price = simpledialog.askfloat("Tambah Produk", "Masukkan harga produk:")
        product_quantity = simpledialog.askinteger("Tambah Produk", "Masukkan jumlah produk:")

        if product_name and product_price is not None and product_quantity is not None:
            success = self.inventory_controller.add_product(product_name, product_price, product_quantity)

            if success:
                messagebox.showinfo("Tambah Produk", "Produk berhasil ditambahkan.")
            else:
                messagebox.showwarning("Tambah Produk Gagal", "Gagal menambahkan produk. Periksa input Anda.")
        else:
            messagebox.showwarning("Input Tidak Valid", "Masukkan nama, harga, dan jumlah produk yang valid.")

    def make_sale(self):
        if self.logged_in:
            product_name = simpledialog.askstring("Buat Penjualan", "Masukkan nama produk:")
            quantity = simpledialog.askinteger("Buat Penjualan", "Masukkan jumlah produk:")
            
            if product_name and quantity is not None:
                success = self.sales_controller.make_sale(product_name, quantity)
                
                if success:
                    messagebox.showinfo("Penjualan Berhasil", "Penjualan berhasil dicatat.")
                else:
                    messagebox.showwarning("Stok Tidak Cukup", "Stok produk tidak mencukupi untuk melakukan penjualan.")
            else:
                messagebox.showwarning("Input Tidak Valid", "Masukkan nama produk dan jumlah produk yang valid.")
        else:
            messagebox.showwarning("Login Diperlukan", "Anda harus login untuk membuat penjualan.")

    def generate_sales_report(self):
        sales_report = self.sales_controller.generate_sales_report()
        messagebox.showinfo("Laporan Penjualan", sales_report)

    def login(self):
        if not self.logged_in:
            self.username = simpledialog.askstring("Login", "Masukkan username:")
            password = simpledialog.askstring("Login", "Masukkan password:", show='*')

            if self.verify_credentials(self.username, password):
                self.logged_in = True
                messagebox.showinfo("Login Berhasil", f"Selamat datang, {self.username}!")
            else:
                messagebox.showinfo("Login Gagal", "Username atau password salah.")
        else:
            messagebox.showinfo("Logout", f"Logout berhasil. Sampai jumpa, {self.username}!")
            self.logged_in = False
            self.username = ""

    def verify_credentials(self, username, password):
        # Fungsi verifikasi otentikasi sederhana (ganti sesuai kebutuhan)
        return username == "admin" and password == "admin123"
