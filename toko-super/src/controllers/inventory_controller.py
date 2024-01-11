# File: controllers/inventory_controller.py
from models.product import Product

class InventoryController:
    """
    Kontroler untuk mengelola inventori produk.

    Attributes:
        inventory (list): Daftar produk dalam inventori.
    """

    def __init__(self):
        """
        Inisialisasi objek kontroler inventori.
        """
        self.inventory = []

    def add_product(self, name, price, quantity):
        """
        Menambahkan produk baru ke inventori.

        Parameters:
            name (str): Nama produk.
            price (float): Harga produk.
            quantity (int): Jumlah produk.
        """
        new_product = Product(name, price, quantity)
        self.inventory.append(new_product)

    def view_inventory(self):
        """
        Menampilkan inventori.

        Returns:
            str: Representasi string dari inventori.
        """
        if not self.inventory:
            return "Inventory is empty."
        else:
            inventory_str = "\n".join(str(product) for product in self.inventory)
            return f"Current Inventory:\n{inventory_str}"

    def export_inventory(self, filename='inventory.txt'):
        """
        Menyimpan inventori ke file eksternal.

        Parameters:
            filename (str): Nama file untuk menyimpan inventori.
        """
        with open(filename, 'w') as file:
            for product in self.inventory:
                file.write(f"{product.to_dict()}\n")
