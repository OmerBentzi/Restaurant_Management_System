from menu_items import MenuItem
import csv

# Order class
class Order:
    def __init__(self, order_id, customer_name, phone_number, menu_items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.menu_items = menu_items

    def add_order_item(self, menu_item: MenuItem):
      
       # Adds a menu item to the order's list of menu items.
      
        self.menu_items.append({"menu_item": menu_item})

    def remove_order_item(self, menu_item: MenuItem):
        
       # Removes a specific menu item from the order's list of menu items.
       
        for item in self.menu_items:
            if item["menu_item"] == menu_item:
                self.menu_items.remove(item)
                return

    def get_total_price(self):
        
       # Calculates and returns the total price of the order.
        
        return sum(item["menu_item"].price for item in self.menu_items)

    def contains(self, menu_item: MenuItem) -> bool:
        
       # Checks if the order contains a specific menu item.
       # Returns True if the menu item is found, False otherwise.
        
        for item in self.menu_items:
            if item["menu_item"] == menu_item:
                return True
        return False

    def save_to_csv(self, filename):
        
      #  Saves the order details to a CSV file.
        
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["order_id", "customer_name", "phone_number", "menu_item"])
            for item in self.menu_items:
                writer.writerow([self.order_id, self.customer_name, self.phone_number, item['menu_item'].name])

    @staticmethod
    def load_from_csv(filename):
        
       # Loads an order from a CSV file and returns an Order object.
        
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            order_id = None
            customer_name = None
            phone_number = None
            order_items = []
            for row in reader:
                if order_id is None:
                    order_id = int(row['order_id'])
                    customer_name = row['customer_name']
                    phone_number = row['phone_number']
                menu_item_name = row['menu_item']
                menu_item_price = 0.0  # Provide the correct price value
                menu_item = MenuItem(order_id, menu_item_name, menu_item_price)
                order_items.append({"menu_item": menu_item})
            return Order(order_id, customer_name, phone_number, order_items)
