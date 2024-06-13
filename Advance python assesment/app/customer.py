from user import User
from database import Database

class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password, 'customer')

    def purchase_stock(self, product_id, quantity):
        db = Database()
        product_query = "SELECT price, stock FROM products WHERE product_id=%s"
        product = db.fetch_one(product_query, (product_id,))
        if product and product[1] >= quantity:
            total_price = product[0] * quantity
            order_query = "INSERT INTO orders (customer_id, product_id, quantity, total_price) VALUES (%s, %s, %s, %s)"
            customer_id = self.get_user_id()
            order_params = (customer_id, product_id, quantity, total_price)
            db.execute_query(order_query, order_params)
            update_stock_query = "UPDATE products SET stock=stock-%s WHERE product_id=%s"
            db.execute_query(update_stock_query, (quantity, product_id))
        else:
            print("Not enough stock available.")

    def view_all_orders(self):
        db = Database()
        customer_id = self.get_user_id()
        query = "SELECT * FROM orders WHERE customer_id=%s"
        return db.fetch_all(query, (customer_id,))

    def get_user_id(self):
        db = Database()
        query = "SELECT user_id FROM users WHERE username=%s"
        return db.fetch_one(query, (self.username,))[0]
