import unittest
from menu import Menu

class TestMenu(unittest.TestCase):
    def test_init(self):
        # Test Menu initialization
        menu = Menu()
        self.assertIsInstance(menu, Menu)
        self.assertEqual(menu.menu_items, [])

    def setUp(self):
        # Set up a Menu instance and some menu items for other test cases
        self.menu = Menu()
        self.menu.add_menu_item("1", "Pizza", 12.99)
        self.menu.add_menu_item("2", "Salad", 8.99)
        self.menu.add_menu_item("3", "Ice Cream", 5.99)

    def test_add_menu_item(self):
        # Test adding a menu item to the menu
        self.assertEqual(len(self.menu.menu_items), 3)
        self.menu.add_menu_item("4", "Burger", 10.99)
        self.assertEqual(len(self.menu.menu_items), 4)
        self.assertEqual(self.menu.menu_items[-1].name, "Burger")

    def test_remove_menu_item(self):
        # Test removing a menu item from the menu
        self.assertEqual(len(self.menu.menu_items), 3)
        self.menu.remove_menu_item(self.menu.menu_items[0])
        self.assertEqual(len(self.menu.menu_items), 2)
        self.assertEqual(self.menu.menu_items[0].name, "Salad")
     


    def test_save_and_load_csv(self):
        # Save menu to CSV file
        file_name = "test_menu.csv"
        self.menu.save_to_csv(file_name)

        # Load menu from CSV file
        loaded_menu = Menu.load_from_csv(file_path=file_name)

        # Compare loaded menu to original menu
        self.assertEqual(len(self.menu.menu_items), len(loaded_menu.menu_items))
        for i in range(len(self.menu.menu_items)):
            self.assertEqual(self.menu.menu_items[i].name, loaded_menu.menu_items[i].name)
            self.assertEqual(self.menu.menu_items[i].price, loaded_menu.menu_items[i].price)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
