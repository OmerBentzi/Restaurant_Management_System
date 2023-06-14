import unittest
from table import *


class TestTable(unittest.TestCase):
    def setUp(self):
        # Set up a Table instance for other test cases
        self.table = Table(1, 4)

    def test_init(self):
        # Test Table initialization
        self.assertEqual(self.table.table_number, 1)
        self.assertEqual(self.table.seating_capacity, 4)

    def test_add_tables(self):
        # Define the tables to add
        tables_to_add = [
            (2, 4),  # Table 2 with seating capacity 4
            (3, 6),  # Table 3 with seating capacity 6
            (4, 2)   # Table 4 with seating capacity 2
        ]

        # Save the existing tables to a temporary CSV file
        existing_file_path = "existing_tables.csv"
        self.table.save(existing_file_path)

        # Add the tables to the existing tables
        Table.add_tables(existing_file_path, [] ,tables_to_add)

        # Load the updated tables from the CSV file
        updated_tables = Table.load(existing_file_path)

        # Assert the correct number of tables
        self.assertEqual(len(updated_tables), 3)

        # Assert the details of the added tables
        self.assertEqual(updated_tables[0].table_number, 2)
        self.assertEqual(updated_tables[0].seating_capacity, 4)
        self.assertEqual(updated_tables[1].table_number, 3)
        self.assertEqual(updated_tables[1].seating_capacity, 6)
        self.assertEqual(updated_tables[2].table_number, 4)
        self.assertEqual(updated_tables[2].seating_capacity, 2)


    def test_assign_employee(self):
        # Test assigning an employee to the table
        self.table.assign_employee(1)
        self.assertEqual(self.table.employee_id, 1)

    def test_save_and_load_csv(self):
        # Create table instances
        table1 = Table(1, 4)
        table2 = Table(2, 6)
        table3 = Table(3, 2)

        # Save tables to CSV file
        file_path = "test_table.csv"
        Table.write_to_csv(file_path, [table1, table2, table3])

        # Load tables from CSV file
        tables = Table.read_from_csv(file_path)

        # Assert tables are loaded correctly
        self.assertEqual(len(tables), 3)
        self.assertEqual(tables[0].table_number, 1)
        self.assertEqual(tables[0].seating_capacity, 4)
        self.assertEqual(tables[1].table_number, 2)
        self.assertEqual(tables[1].seating_capacity, 6)
        self.assertEqual(tables[2].table_number, 3)
        self.assertEqual(tables[2].seating_capacity, 2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)