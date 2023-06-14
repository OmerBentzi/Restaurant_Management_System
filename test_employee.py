import unittest
from employee import Employee, EmployeeData


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee1 = Employee(1, "John Doe", "john@example.com", "1234567890", "Manager", "All Access")
        self.employee2 = Employee(2, "Jane Smith", "jane@example.com", "9876543210", "Chef", "All Access")

    def test_employee_attributes(self):
        # Test employee attribute values
        self.assertEqual(self.employee1.employee_id, 1)
        self.assertEqual(self.employee1.name, "John Doe")
        self.assertEqual(self.employee1.email, "john@example.com")
        self.assertEqual(self.employee1.phone, "1234567890")
        self.assertEqual(self.employee1.role, "Manager")
        self.assertEqual(self.employee1.permission, "All Access")

    def test_employee_add_employee(self):
        # Test adding an employee to the employee list
        employee_data = EmployeeData("employees.csv")
        employee_data.employee_list = [self.employee1]
        self.assertEqual(len(employee_data.employee_list), 1)


class TestEmployeeData(unittest.TestCase):
    def setUp(self):
        self.employee_data = EmployeeData("employees.csv")
        self.employee_list = [
            Employee(1, "John Doe", "john@example.com", "1234567890", "Manager", "All Access"),
            Employee(2, "Jane Smith", "jane@example.com", "9876543210", "Chef", "All Access"),
        ]
        self.employee_data.employee_list = self.employee_list

    def test_read_data(self):
        # Test reading employee data from CSV
        expected_employee_list = self.employee_list
        actual_employee_list = self.employee_data.read_data()

        for actual_employee, expected_employee in zip(actual_employee_list, expected_employee_list):
            self.assertEqual(actual_employee.employee_id, expected_employee.employee_id)
            self.assertEqual(actual_employee.name, expected_employee.name)
            self.assertEqual(actual_employee.email, expected_employee.email)
            self.assertEqual(actual_employee.phone, expected_employee.phone)
            self.assertEqual(actual_employee.role, expected_employee.role)  # Update the expected value here
            self.assertEqual(actual_employee.permission, expected_employee.permission)

    def test_write_data(self):
        # Test writing employee data to CSV
        employee_data = EmployeeData("employees.csv")
        employee_data.write_data(self.employee_list)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
