from user import User
from database import Database

class ProductManager(User):
    def __init__(self, username, password):
        super().__init__(username, password, 'product_manager')

    def manage_product_stock(self, product_name, stock, price):
        db = Database()
        query = "INSERT INTO products (product_name, stock, price) VALUES (%s, %s, %s)"
        params = (product_name, stock, price)
        db.execute_query(query, params)

    def view_all_stocks(self):
        db = Database()
        query = "SELECT * FROM products"
        return db.fetch_all(query)
