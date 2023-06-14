import unittest
from unittest.mock import patch
from employee_system import *


class TestEmployeeSystem(unittest.TestCase):
    def setUp(self):
        self.employee_file_path = "employees.csv"
        self.employee_system = EmployeeSystem(self.employee_file_path)

    def tearDown(self):
        self.employee_system = None

    @patch('click.prompt')
    def test_add_employee(self, mock_prompt):
        # Set up mock user input
        mock_prompt.side_effect = [
            "password",  # password
            "123",  # employee_id
            "John",  # name 
            "john@example.com",  # email
            "1234567890",  # phone
            "Waiter",  # role
            "kitchen",  # permission
        ]

        self.employee_system.add_employee()

        employees = self.employee_system.load_data()
        self.assertEqual(employees[0].employee_id,123)


    @patch('click.prompt')
    def test_edit_employee(self, mock_prompt):
        # Add an employee
        employee_data = {
            "employee_id": "123",
            "name": "John",
            "email": "john@example.com",
            "phone": "1234567890",
            "role": "Waiter",
            "permission": "kitchen"
        }
        self.employee_system.employee_list.append(Employee(**employee_data))
        self.employee_system.save_data(employee_list=self.employee_system.employee_list)

        # Set up mock user input
        mock_prompt.side_effect = [
            #"password",  # password
            "123",  # employee_id
            "John",  # name
            "john@example.com",  # email
            "9876543210",  # phone
            "Waiter",  # role
            "kitchen",  # permission
        ]

        self.employee_system.edit_employee()

        employees = self.employee_system.load_data()
        self.assertEqual(employees[0].employee_id,123)
        self.assertEqual(employees[0].name, "John")

    @patch('click.prompt')
    def test_delete_employee(self, mock_prompt):
        # Add an employee
        employee_data = {
            "employee_id": "123",
            "name": "John",
            "email": "john@example.com",
            "phone": "1234567890",
            "role": "Waiter",
            "permission": "kitchen"
        }
        self.employee_system.employee_list.append(Employee(**employee_data))
        self.employee_system.save_data( employee_list=self.employee_system.employee_list)

        # Set up mock user input
        mock_prompt.side_effect = [
            #"password",  # password
            "123"  # employee_id
        ]

        self.employee_system.delete_employee()

        employees = self.employee_system.load_data()


if __name__ == "__main__":
    unittest.main()
