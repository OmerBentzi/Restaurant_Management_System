import unittest
from order import Order
from menu_items import MenuItem

class TestOrder(unittest.TestCase):
    def test_order_init(self):
        # Test Order initialization
        order = Order(1, "John", None, [])
        self.assertEqual(order.order_id, 1)
        self.assertEqual(order.customer_name, "John")
        self.assertEqual(order.menu_items, [])

    def setUp(self):
        # Set up an Order instance for other test cases
        self.order = Order(1, "Alice", None, [])

    def test_add_order_item(self):
        # Test adding an order item to the order
        menu_item = MenuItem(1, "Spaghetti", 15.99)
        self.order.add_order_item(menu_item)
        self.assertEqual(len(self.order.menu_items),1)
        self.assertEqual(self.order.menu_items[0]["menu_item"].name, menu_item.name)

    def test_remove_order_item(self):
        # Test removing an order item from the order
        menu_item = MenuItem(1, "Spaghetti", 15.99)
        self.order.add_order_item(menu_item)
        self.order.remove_order_item(menu_item)
        self.assertEqual(len(self.order.menu_items), 0)

    def test_get_total_price(self):
        # Test calculating the total price of the order
        menu_item1 = MenuItem(3, "Spaghetti", 15.99)
        menu_item2 = MenuItem(4, "Salad", 10.99)
        self.order.add_order_item(menu_item1)
        self.order.add_order_item(menu_item2)
        self.assertAlmostEqual(self.order.get_total_price(), 26.98, places=2)

    def test_contains(self):
        # Test checking if the order contains a specific menu item
        menu_item1 = MenuItem(1, "Pizza", 10.0)
        menu_item2 = MenuItem(2, "Burger", 8.0)
        self.order.add_order_item(menu_item1)
        self.assertTrue(self.order.contains(menu_item1))
        self.assertFalse(self.order.contains(menu_item2))

    def test_save_and_load_csv(self):
        # Create a new order
        order = Order(1, "Alice", None, [])
        order.add_order_item(MenuItem(1, "Pizza", 10.0))
        order.add_order_item(MenuItem(2, "Burger", 8.0))

        # Save the order to a CSV file
        filename = "test_order.csv"
        order.save_to_csv(filename)

        # Load the order from the CSV file
        loaded_order = Order.load_from_csv(filename)

        # Assert that the loaded order is the same as the original order
        self.assertEqual(order.order_id, loaded_order.order_id)
        self.assertEqual(order.customer_name, loaded_order.customer_name)
        self.assertEqual(len(order.menu_items), len(loaded_order.menu_items))
        for i in range(len(order.menu_items)):
            self.assertEqual(order.menu_items[i]["menu_item"].name, loaded_order.menu_items[i]["menu_item"].name)



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
