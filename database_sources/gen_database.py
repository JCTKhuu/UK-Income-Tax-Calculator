import sqlite3
from countries import countries
import tax_static_data

def create_tables() -> None:
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS countries (
            id      INTEGER PRIMARY KEY ON CONFLICT IGNORE,
            name    TEXT    UNIQUE      ON CONFLICT IGNORE
        );
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tax_brackets (
            id                  INTEGER PRIMARY KEY ON CONFLICT IGNORE,
            country_id          INTEGER NOT NULL    ON CONFLICT IGNORE,
            tax_year            INTEGER NOT NULL    ON CONFLICT IGNORE,
            name                TEXT,
            rate                NUMBER  NOT NULL    ON CONFLICT IGNORE,
            bracket_upper_bound INTEGER NOT NULL    ON CONFLICT IGNORE,

            UNIQUE(country_id, tax_year, bracket_upper_bound) ON CONFLICT IGNORE
            FOREIGN KEY (country_id) REFERENCES countries(id)
        );
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS personal_allowance_income_limit (
            id                  INTEGER PRIMARY KEY ON CONFLICT IGNORE,
            tax_year            INTEGER NOT NULL    ON CONFLICT IGNORE,
            income_limit        INTEGER NOT NULL    ON CONFLICT IGNORE,

            UNIQUE(tax_year) ON CONFLICT IGNORE
        );
        """
    )

    connection.commit()

    cursor.close()
    connection.close()

def populate_tables() -> None:
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()

    for country in countries:
        cursor.executescript(
            """
            INSERT INTO countries (name) VALUES ('{}');
            """.format(country)
        )

    for tax_bracket in tax_static_data.income_tax_brackets():
        cursor.executescript(
            """
            INSERT INTO tax_brackets (country_id, tax_year, name, rate, bracket_upper_bound)
            VALUES ({}, {}, '{}', {}, '{}');
            """.format(tax_bracket['Country ID'], tax_bracket['Tax Year'], tax_bracket['Name'], tax_bracket['Tax Rate'], tax_bracket['Bracket Upper Bound'])
        )

    for personal_allowance_income_limit in tax_static_data.personal_allowance_income_limit():
        cursor.executescript(
            """
            INSERT INTO personal_allowance_income_limit (tax_year, income_limit)
            VALUES ({}, {});
            """.format(personal_allowance_income_limit['Tax Year'], personal_allowance_income_limit['Income Limit'])
        )
        
    connection.commit()

    cursor.close()
    connection.close()
    
if __name__ == "__main__":
    create_tables()
    populate_tables()