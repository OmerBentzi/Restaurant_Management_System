import unittest
from customer_system import CustomerSystem
from menu_items import MenuItem

class TestCustomerSystem(unittest.TestCase):
    def setUp(self):
        self.menu_items = [
            MenuItem(1, "Pizza", 10.99),
            MenuItem(2, "Burger", 8.99)
        ]
        self.test_data_file = 'test_customer_orders.csv'
        self.customer_system = CustomerSystem(self.test_data_file, self.menu_items)

    def tearDown(self):
        # Clean up any test data files created during testing
        self.customer_system.customer_list = []
        self.customer_system.save_data()

    def test_generate_order_id(self):
        # Test generating a unique order ID
        order_id = self.customer_system.generate_order_id()
        self.assertIsInstance(order_id, int)

    def test_add_customer(self):
        # Test adding a customer
        order_items = [
            self.menu_items[0],  # Add Pizza
            self.menu_items[1]  # Add Burger
        ]
        self.customer_system.add_customer("John Doe", "1234567890", order_items)
        self.assertEqual(len(self.customer_system.customer_list), 1)
        self.assertEqual(self.customer_system.customer_list[0].customer_name, "John Doe")
        self.assertEqual(self.customer_system.customer_list[0].phone_number, "1234567890")
        self.assertEqual(self.customer_system.customer_list[0].order.menu_items, order_items)

    def test_get_menu_item_by_id(self):
        # Test retrieving a menu item by ID
        menu_item = self.customer_system.get_menu_item_by_id(1)
        self.assertEqual(menu_item.item_id, 1)
        self.assertEqual(menu_item.name, "Pizza")

    def test_place_order(self):
        # Test placing an order
        self.customer_system.add_customer("John Doe", "1234567890")
        self.customer_system.place_order()
   

    def get_customer_by_id(self, order_id):
        for customer in self.customer_list:
            if customer.order and customer.order.order_id == order_id:
                return customer
        return None



if __name__ == '__main__':
    unittest.main()
