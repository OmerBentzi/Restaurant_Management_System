import csv
import os

class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price


    def update_price(self, new_price):
        self.price = new_price


    @classmethod
    def save_to_csv(cls, menu_items, filename):
        # Delete the existing file, if it exists
        if os.path.exists(filename):
            os.remove(filename)

        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ["item_id", 'name', 'price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for menu_item in menu_items:
                writer.writerow({"item_id": menu_item.item_id, 'name': menu_item.name, 'price': menu_item.price})



    @classmethod
    def load_from_csv(cls, filename):
        menu_items = []
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            for row in reader:
                try:
                    menu_item = cls(int(row[0]), row[1], float(row[2]))
                    menu_items.append(menu_item)
                except (IndexError, TypeError, ValueError):
                    # Skip rows with missing or invalid data
                    continue
        return menu_items
    
    
# a welcome sign to the restaurant    
    @staticmethod
    def display_menu(menu_items):
        print("\nWelcome to the BurgerBoss Menu")
        print("************************************")
        print("Menu Items")
        print("----------")
        for i, menu_item in enumerate(menu_items):
            print(f"{i + 1}. {menu_item.name} (${menu_item.price})")


#the menu items lists with order id the name and price
menu_items = [
    MenuItem(1,"Cybernetic Cheeseburger",9.99),
    MenuItem(2,"Virtual Veggie Burger",8.99),
    MenuItem(3,"Techno Chicken Tenders",7.99),
    MenuItem(4,"Nano-Bacon Deluxe Burger",11.99),
    MenuItem(5,"Hologramatic BBQ Pulled Pork Sandwich",10.99),
    MenuItem(6,"Augmented Grilled Chicken Sandwich", 9.99),
    MenuItem(7,"Cyber Chocolate Brownie Sundae",6.99),
    MenuItem(8,"Quantum Milkshake (Vanilla, Chocolate, Strawberry)",4.99),
    MenuItem(9,"Futuristic Apple Pie",5.99)
]

# Save menu items to a CSV file
for menu_item in menu_items:
    MenuItem.save_to_csv(menu_items,'menu_items.csv')

# Load menu items from the CSV file
menu_items = MenuItem.load_from_csv('menu_items.csv')