import unittest
from menu_items import MenuItem


class TestMenuItem(unittest.TestCase):
    def test_init(self):
        # Test MenuItem initialization
        menu_item = MenuItem(1, "Spaghetti", 15.99)
        self.assertEqual(menu_item.name, "Spaghetti")
        self.assertEqual(menu_item.price, 15.99)

    def setUp(self):
        # Set up a MenuItem instance for other test cases
        self.menu_item = MenuItem(1, "Spaghetti", 15.99)

    def test_initial_price(self):
        # Test the initial price of the menu item
        self.assertEqual(self.menu_item.price, 15.99)

    def test_update_price(self):
        # Test updating the price of the menu item
        self.menu_item.update_price(17.99)
        self.assertEqual(self.menu_item.price, 17.99)

    def test_save_and_load_csv(self):
        # Test saving and loading menu items to/from a CSV file
        filename = "menu_items.csv"
        menu_items = [self.menu_item]
        MenuItem.save_to_csv(menu_items, filename)
        loaded_menu_items = MenuItem.load_from_csv(filename)
        self.assertEqual(len(loaded_menu_items), 1)
        loaded_menu_item = loaded_menu_items[0]
        self.assertEqual(loaded_menu_item.name, "Spaghetti")
        self.assertEqual(loaded_menu_item.price, 15.99)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
