# THIS IS A SCRIPT THAT WILL RUN ON IMPORT
# This script will create tables within database "mydatabase.db" that will hold tables for countries and respective tax brackets

import sqlite3

def create_tables() -> None:
    # """
    # Creates database with tables countries and tax_brackets
    # """
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