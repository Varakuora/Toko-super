# File: controllers/sales_controller.py
from models.product import Product

class SalesController:
    def __init__(self, inventory_controller):
        self.inventory_controller = inventory_controller
        self.sales_history = []

    def make_sale(self, product_name, quantity):
        for product in self.inventory_controller.inventory:
            if product.name == product_name:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    self.sales_history.append({
                        'product': product_name,
                        'quantity': quantity,
                        'total_price': product.price * quantity
                    })
                    return f"Sale successful. Total: ${product.price * quantity}"
                else:
                    return "Insufficient quantity in inventory."
        return "Product not found in inventory."

    def generate_sales_report(self):
        if not self.sales_history:
            return "No sales made yet."
        else:
            report_str = "\n".join(f"{sale['product']} - Quantity: {sale['quantity']} - Total: ${sale['total_price']}" for sale in self.sales_history)
            return f"Sales Report:\n{report_str}"
