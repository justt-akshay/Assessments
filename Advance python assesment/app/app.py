import tkinter as tk
from tkinter import messagebox
from product_manager import ProductManager
from customer import Customer

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Product Management System")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self)
        self.frame.pack(pady=20)
        
        self.label = tk.Label(self.frame, text="Welcome to Product Management System")
        self.label.pack(pady=10)

        self.pm_button = tk.Button(self.frame, text="Product Manager", command=self.pm_login)
        self.pm_button.pack(pady=5)

        self.customer_button = tk.Button(self.frame, text="Customer", command=self.customer_login)
        self.customer_button.pack(pady=5)

    def pm_login(self):
        self.clear_frame()
        self.label = tk.Label(self.frame, text="Product Manager Login")
        self.label.pack(pady=10)
        
        self.username_label = tk.Label(self.frame, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack()

        self.password_label = tk.Label(self.frame, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.frame, text="Login", command=self.pm_authenticate)
        self.login_button.pack(pady=10)

    def pm_authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        pm = ProductManager(username, password)
        if pm.login():
            messagebox.showinfo("Success", "Login successful!")
            self.pm_dashboard(pm)
        else:
            messagebox.showerror("Error", "Invalid credentials. Please try again.")

    def pm_dashboard(self, pm):
        self.clear_frame()
        self.label = tk.Label(self.frame, text="Product Manager Dashboard")
        self.label.pack(pady=10)

        self.add_product_button = tk.Button(self.frame, text="Add Product", command=lambda: self.add_product(pm))
        self.add_product_button.pack(pady=5)

        self.view_stocks_button = tk.Button(self.frame, text="View Stocks", command=self.view_stocks)
        self.view_stocks_button.pack(pady=5)

    def add_product(self, pm):
        self.clear_frame()
        self.label = tk.Label(self.frame, text="Add Product")
        self.label.pack(pady=10)

        self.product_name_label = tk.Label(self.frame, text="Product Name")
        self.product_name_label.pack()
        self.product_name_entry = tk.Entry(self.frame)
        self.product_name_entry.pack()

        self.stock_label = tk.Label(self.frame, text="Stock")
        self.stock_label.pack()
        self.stock_entry = tk.Entry(self.frame)
        self.stock_entry.pack()

        self.price_label = tk.Label(self.frame, text="Price")
        self.price_label.pack()
        self.price_entry = tk.Entry(self.frame)
        self.price_entry.pack()

        self.add_button = tk.Button(self.frame, text="Add", command=lambda: self.save_product(pm))
        self.add_button.pack(pady=10)

    def save_product(self, pm):
        product_name = self.product_name_entry.get()
        stock = int(self.stock_entry.get())
        price = float(self.price_entry.get())
        pm.manage_product_stock(product_name, stock, price)
        messagebox.showinfo("Success", "Product added successfully!")
        self.pm_dashboard(pm)

    def view_stocks(self):
        self.clear_frame()
        self.label = tk.Label(self.frame, text="All Stocks")
        self.label.pack(pady=10)
        
        db = Database()
        products = db.fetch_all("SELECT * FROM products")
        for product in products:
            product_label = tk.Label(self.frame, text=f"ID: {product[0]}, Name: {product[1]}, Stock: {product[2]}, Price: {product[3]}")
            product_label.pack()

        self.back_button = tk.Button(self.frame, text="Back", command=self.pm_login)
        self.back_button.pack(pady=10)

    def customer_login(self):
        self.clear_frame()
        self.label = tk.Label(self.frame, text="Customer Login")
        self.label.pack(pady=10)
        
        self.username_label = tk.Label(self.frame, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack()

        self.password_label = tk.Label(self.frame, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.frame, text="Login", command=self.customer_authenticate)
        self.login_button.pack(pady=10)

    def customer_authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        customer = Customer(username, password)
        if customer.login():
            messagebox.showinfo("Success", "Login successful!")
            self.customer_dashboard(customer)
        else:
            messagebox.showerror("Error", "Invalid credentials. Please try again.")

    def customer_dashboard(self, customer):
        self.clear_frame()
        self.label = tk.Label(self.frame, text="Customer Dashboard")
        self.label.pack(pady=10)

        self.purchase_button = tk.Button(self.frame, text="Purchase Stock", command=lambda: self.purchase_stock(customer))
        self.purchase_button.pack(pady=5)

        self.view_orders_button = tk.Button(self.frame, text="View Orders", command=lambda: self.view_orders(customer))
        self.view_orders_button.pack(pady=5)

    def purchase_stock(self, customer):
        self.clear_frame()
        self.label = tk.Label(self.frame, text="Purchase Stock")
        self.label.pack(pady=10)

        self.product_id_label = tk.Label(self.frame, text="Product ID")
        self.product_id_label.pack()
        self.product_id_entry = tk.Entry(self.frame)
        self.product_id_entry.pack()

        self.quantity_label = tk.Label(self.frame, text="Quantity")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(self.frame)
        self.quantity_entry.pack()

        self.purchase_button = tk.Button(self.frame, text="Purchase", command=lambda: self.save_purchase(customer))
        self.purchase_button.pack(pady=10)

    def save_purchase(self, customer):
        product_id = int(self.product_id_entry.get())
        quantity = int(self.quantity_entry.get())
        customer.purchase_stock(product_id, quantity)
        messagebox.showinfo("Success", "Purchase successful!")
        self.customer_dashboard(customer)

    def view_orders(self, customer):
        self.clear_frame()
        self.label = tk.Label(self.frame, text="All Orders")
        self.label.pack(pady=10)
        
        orders = customer.view_all_orders()
        for order in orders:
            order_label = tk.Label(self.frame, text=f"Order ID: {order[0]}, Product ID: {order[2]}, Quantity: {order[3]}, Total Price: {order[4]}")
            order_label.pack()

        self.back_button = tk.Button(self.frame, text="Back", command=lambda: self.customer_dashboard(customer))
        self.back_button.pack(pady=10)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
