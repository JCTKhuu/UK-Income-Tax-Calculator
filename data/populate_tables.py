import sqlite3
from data.countries import countries
import data.tax_information

def populate_tables() -> None:
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()

    for country in countries:
        cursor.executescript(
            """
            INSERT INTO countries (name) VALUES ('{}');
            """.format(country)
        )

    for tax_bracket in data.tax_information.income_tax_brackets():
        cursor.executescript(
            """
            INSERT INTO tax_brackets (country_id, tax_year, name, rate, bracket_upper_bound)
            VALUES ({}, {}, '{}', {}, '{}');
            """.format(tax_bracket['Country ID'], tax_bracket['Tax Year'], tax_bracket['Name'], tax_bracket['Tax Rate'], tax_bracket['Bracket Upper Bound'])
        )

    for personal_allowance_income_limit in data.tax_information.personal_allowance_income_limit():
        cursor.executescript(
            """
            INSERT INTO personal_allowance_income_limit (tax_year, income_limit)
            VALUES ({}, {});
            """.format(personal_allowance_income_limit['Tax Year'], personal_allowance_income_limit['Income Limit'])
        )
        
    connection.commit()

    cursor.close()
    connection.close()