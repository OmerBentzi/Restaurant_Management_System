import csv
from menu_items import *

class Menu:
    #initialize menu
    def __init__(self):
        self.menu_items = []
    
    #add menu item
    def add_menu_item(self, item_id, name, price):
        menu_item = MenuItem(item_id, name, price)
        self.menu_items.append(menu_item)
    

    #remove menu item
    def remove_menu_item(self, menu_item):
        if menu_item in self.menu_items:
            self.menu_items.remove(menu_item)
    
    #save menu to csv
    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["item_id", "name", "price"])
            for menu_item in self.menu_items:
                writer.writerow([menu_item.item_id, menu_item.name, menu_item.price])


    #load menu from csv
    @classmethod
    def load_from_csv(cls, file_path):
        menu = cls()
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                item_id = row[0]
                name = row[1]
                price = float(row[2])
                menu.add_menu_item(item_id, name, price)

        return menu
