
import csv
from typing import List
import os

# Table class
class Table:
    def __init__(self, table_number, seating_capacity, employee_id=None):
        self.table_number = table_number
        self.seating_capacity = seating_capacity
        self.employee_id = employee_id

    def assign_employee(self, employee_id):
        
      # Assigns an employee to the table.
        
        self.employee_id = employee_id
    
    @staticmethod
    def add_tables(file_path: str, existing_tables: List["Table"], tables_to_add: List[tuple]):
        
       # Adds new tables to the existing list of tables and writes the updated data to a CSV file.
        
        tables = existing_tables[:]
        for table_data in tables_to_add:
            table_number, seating_capacity = table_data
            table = Table(table_number, seating_capacity)
            tables.append(table)

        Table.write_to_csv(file_path, tables)
     
 

    @staticmethod
    def write_to_csv(file_path: str, tables: List["Table"]):
       
       # Writes table data to a CSV file.
        
        fieldnames = ["table_number", "seating_capacity", "employee_id"]
        with open(file_path, mode="w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for table in tables:
                writer.writerow({
                    "table_number": table.table_number,
                    "seating_capacity": table.seating_capacity,
                    "employee_id": table.employee_id
                })

    @staticmethod
    def read_from_csv(file_path: str):
        
       # Reads table data from a CSV file and returns a list of Table objects.
        
        tables = []
        if not os.path.isfile(file_path):
            return tables

        with open(file_path, mode="r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                try:
                    table = Table(
                        table_number=int(row["table_number"]),
                        seating_capacity=int(row["seating_capacity"]),
                        employee_id=int(row["employee_id"]) if row["employee_id"] else None
                    )
                    tables.append(table)
                except ValueError:
                    table = Table(
                        table_number=int(row["table_number"]),
                        seating_capacity=int(row["seating_capacity"]),
                        employee_id=None
                    )
                    tables.append(table)
        return tables

    def save(self, file_path: str):
        
       # Saves the current table object to a CSV file, updating the existing data if the table already exists.
        
        tables = Table.read_from_csv(file_path)
        for i, table in enumerate(tables):
            if table.table_number == self.table_number:
                tables[i] = self
                break
        else:
            tables.append(self)
        Table.write_to_csv(file_path, tables)

    @staticmethod
    def load(file_path: str):
        
       # Loads table data from a CSV file and returns a list of Table objects.
        
        return Table.read_from_csv(file_path)


# Example of adding tables with specific table numbers and seating capacities
tables_to_add = [
    (2, 4),  # Table 2 with seating capacity 4
    (3, 6),  # Table 3 with seating capacity 6
    (4, 2)   # Table 4 with seating capacity 2
]

existing_tables = Table.load("tables.csv")
Table.add_tables("tables.csv", existing_tables, tables_to_add)
