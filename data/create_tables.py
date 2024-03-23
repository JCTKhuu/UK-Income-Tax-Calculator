# THIS IS A SCRIPT THAT WILL RUN ON IMPORT
# This script will create tables within database "mydatabase.db" that will hold tables for countries and respective tax brackets

import sqlite3

connection = sqlite3.connect('mydatabase.db')
cursor = connection.cursor()

def create_tables(database_cursor):
    # """Creates tables countries and tax_brackets"""
    database_cursor.execute("""
        CREATE TABLE IF NOT EXISTS countries (
            id      INTEGER PRIMARY KEY ON CONFLICT IGNORE,
            name    TEXT    UNIQUE      ON CONFLICT IGNORE,

            UNIQUE(name) ON CONFLICT IGNORE
        );
    """)

    database_cursor.execute("""
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
    """)

create_tables(cursor)
connection.commit
connection.close