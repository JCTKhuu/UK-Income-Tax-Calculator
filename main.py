import matplotlib.pyplot as plt
from math import inf
import sqlite3
import os

class TaxBracket:
    def __init__(self, rate: float, lower_bound: float, upper_bound: float):
        self.rate = rate
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self) -> str:
        return(
            str({
                'Rate': self.rate,
                'Lower bound': self.lower_bound,
                'Upper bound': self.upper_bound
                }
            )
        )

class TaxBrackets:
    def __init__(self, *tax_bracket: TaxBracket, database_name: str):
        self.tax_brackets = []

        for tax_bracket in tax_bracket:
            self.tax_brackets.append(tax_bracket)

        connection = sqlite3.connect(database_name)
        self.cursor = connection.cursor

    def __str__(self):
        tax_bracket_list = []
        
        for tax_bracket in self.tax_brackets:
            tax_bracket_list.append(str(tax_bracket))

        return(
            str(tax_bracket_list)
        )

# def tax_brackets(country_id: int, tax_year: int):
#     connection = sqlite3.connect('mydatabase.db')
#     cursor = connection.cursor

#     cursor.execute("""
#         SELECT *
#         FROM tax_brackets
#         WHERE country_id = {country_id}}
#             and tax_year = {tax_year}
#     """).format(country_id = country_id, tax_year = tax_year)
#     tax_bracket_list = cursor.fetchall

#     for tax_bracket in tax_bracket_list:
#         tax_brackets = TaxBracket()

#     connection.close

if __name__ == '__main__':
    import data.create_tables   # Create a database with tables for country and tax bracket data
    import data.populate_tables # Populate database tables with country and tax bracket data

    if os.path.isfile('data.mydatabase.db'):
        print('hello')
        os.remove('data.mydatabase.db')
