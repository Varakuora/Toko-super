# File: models/product.py

class Product:
    """
    Representasi objek produk dalam inventori.

    Attributes:
        name (str): Nama produk.
        price (float): Harga produk.
        quantity (int): Jumlah produk dalam inventori.
    """

    def __init__(self, name, price, quantity):
        """
        Inisialisasi objek produk.

        Parameters:
            name (str): Nama produk.
            price (float): Harga produk.
            quantity (int): Jumlah produk dalam inventori.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        """
        Mengonversi objek produk ke bentuk kamus.

        Returns:
            dict: Representasi produk dalam bentuk kamus.
        """
        return {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }

    def __str__(self):
        """
        Representasi string dari objek produk.

        Returns:
            str: Representasi string dari objek produk.
        """
        return f"{self.name} - Price: ${self.price} - Quantity: {self.quantity}"
