import sqlite3

def populate_tables():
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()

    from data.countries import countries

    for country in countries:
        cursor.executescript(
            """
            INSERT INTO countries (name) VALUES ('{}');
            """.format(country)
        )

    from data.tax_brackets import tax_brackets

    for tax_bracket in tax_brackets:
        cursor.executescript(
            """
            INSERT INTO tax_brackets (country_id, tax_year, name, rate, bracket_upper_bound)
            VALUES ({}, {}, '{}', {}, '{}');
            """.format(tax_bracket['Country ID'], tax_bracket['Tax Year'], tax_bracket['Name'], tax_bracket['Tax Rate'], tax_bracket['Bracket Upper Bound'])
        )
        
    connection.commit
    connection.close

populate_tables()