# File: src/main.py
import tkinter as tk
from controllers.inventory_controller import InventoryController
from controllers.sales_controller import SalesController
from views.menu import MenuView

# Inisialisasi kontroler
inventory_controller = InventoryController()
sales_controller = SalesController(inventory_controller)

# Inisialisasi Tkinter root window
root = tk.Tk()

# Buat objek MenuView untuk memulai aplikasi
menu_view = MenuView(root, inventory_controller, sales_controller)

# Menampilkan window Tkinter
root.mainloop()
