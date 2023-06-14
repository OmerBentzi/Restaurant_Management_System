import unittest
import csv
from customer import Customer, DataCustomer
from order import Order
from menu import MenuItem


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(1, "John Doe", "1234567890", "johndoe@example.com")

    def test_customer_attributes(self):
        # Test customer attribute values
        self.assertEqual(self.customer.order_id, 1)
        self.assertEqual(self.customer.customer_name, "John Doe")
        self.assertEqual(self.customer.phone_number, "1234567890")
        self.assertEqual(self.customer.email, "johndoe@example.com")

    def test_place_order(self):
        # Test placing an order
        order_id = 1
        menu_items = [MenuItem(1, "Pizza", 10.99), MenuItem(2, "Burger", 8.99)]
        order = Order(order_id, self.customer.order_id, None, menu_items)
        placed_order = self.customer.place_order(order)
        self.assertTrue(placed_order)

    def test_modify_order(self):
        # Test modifying an order
        order_id = 1
        new_items = [MenuItem(1, "Pizza", 10.99), MenuItem(2, "Burger", 8.99)]
        order = Order(order_id, self.customer.order_id, None, new_items)
        self.customer.place_order(order)
        result = self.customer.modify_order(order_id, new_items)
        self.assertTrue(result)

    def test_cancel_order(self):
        # Test canceling an order
        order_id = 1
        menu_items = [MenuItem(1, "Pizza", 10.99), MenuItem(2, "Burger", 8.99)]
        order = Order(order_id, self.customer.order_id, None, menu_items)
        self.customer.place_order(order)
        result = self.customer.cancel_order(order)
        self.assertTrue(result)


class TestDataCustomer(unittest.TestCase):
    def setUp(self):
        self.data_customer = DataCustomer("customers.csv")

    def test_read_data(self):
        # Test reading customer data from CSV
        customer_list = self.data_customer.read_data()
        self.assertIsNotNone(customer_list)
        self.assertEqual(len(customer_list), 2)
        customer = customer_list[0]
        self.assertEqual(customer.order_id, 1)
        self.assertEqual(customer.customer_name, "John Doe")
        self.assertEqual(customer.phone_number, "1234567890")
        self.assertEqual(customer.email, "johndoe@example.com")

    def test_write_data(self):
        # Test writing customer data to CSV
        customer_list = [
            Customer(1, "John Doe", "1234567890", "johndoe@example.com"),
            Customer(2, "Jane Doe", "9876543210", "janedoe@example.com")
        ]
        self.data_customer.write_data(customer_list)
        with open("customers.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                order_id, customer_name, phone_number, email = row
                customer = Customer(int(order_id), customer_name, phone_number, email)
                self.assertEqual(customer.order_id, customer_list[i].order_id)
                self.assertEqual(customer.customer_name, customer_list[i].customer_name)
                self.assertEqual(customer.phone_number, customer_list[i].phone_number)
                self.assertEqual(customer.email, customer_list[i].email)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
